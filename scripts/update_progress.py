#!/usr/bin/env python3
"""Compute red/green progress bars from checklist state and inject them.

Progress model:
  * Each week / module / capstone page under `plan/weeks/` is a unit and the
    single source of truth; tick its checkboxes as you go.
  * A unit's weight = number of `- [ ]` tasks on that week page.
  * A phase's progress = completed tasks / total tasks across its units.
  * Overall progress = completed tasks across all phases.

Renders into:
  * learning-plan.md  -> one bar per phase + overall
  * plan/phase-*.md    -> one bar per week/module + phase summary
                         (the duplicated per-week checkbox lists are stripped)

Bars use green squares (done) and red squares (remaining). Idempotent:
content is rewritten between `<!-- PROGRESS:START -->` / `<!-- PROGRESS:END -->`
markers, so re-running is safe.
"""
import glob
import re
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLAN = os.path.join(ROOT, "plan")
START = "<!-- PROGRESS:START -->"
END = "<!-- PROGRESS:END -->"

GREEN = "\U0001F7E9"  # green square
RED = "\U0001F7E5"    # red square
SEGMENTS = 10

PHASE_META = {
    1: ("Kubernetes Revision & Re-Fluency", "Weeks 1\u20135"),
    2: ("Kubernetes Depth & Application Delivery", "Weeks 6\u201314"),
    3: ("GitOps & CI/CD Depth", "Weeks 15\u201322"),
    4: ("Infrastructure as Code", "Weeks 23\u201332"),
    5: ("Observability Platform Ownership", "Weeks 33\u201344"),
    6: ("Kubernetes Security", "Weeks 45\u201350"),
    7: ("Platform Engineering: Owner & Leader", "Months 10\u201312+"),
    8: ("OpenShift: Advanced Cluster Management", "Weeks 51\u201358"),
}

CHECK_RE = re.compile(r"^\s*- \[([ xX])\]")
PAGES_HEAD_RE = re.compile(r"^##\s+\w+\s+Pages\s*$")
LINK_RE = re.compile(r"^-\s+\[(.+?)\]\((weeks/[^)]+)\)")
UNIT_HEAD_RE = re.compile(r"^##\s+(?:Week\s+\d+|Track\s+[A-E]|Capstone)\b.*$", re.M)
EXIT_HEAD_RE = re.compile(r"^##\s+Exit Criteria\b.*$", re.M)


def pct(done, total):
    return round(done / total * 100) if total else 0


def bar(percent, segments=SEGMENTS):
    filled = round(percent / 100 * segments)
    return GREEN * filled + RED * (segments - filled)


def count_tasks(text):
    done = total = 0
    for line in text.splitlines():
        m = CHECK_RE.match(line)
        if m:
            total += 1
            if m.group(1).lower() == "x":
                done += 1
    return done, total


def unit_links(text):
    """Ordered (label, relpath) week/module page links from the '* Pages' section."""
    in_pages, links = False, []
    for line in text.splitlines():
        if PAGES_HEAD_RE.match(line):
            in_pages = True
            continue
        if in_pages:
            m = LINK_RE.match(line)
            if m:
                links.append((m.group(1), m.group(2)))
            elif line.startswith("## "):
                break
    return links


def parse_units(text):
    """Return [(label, done, total)] from the linked week/module pages."""
    units = []
    for label, rel in unit_links(text):
        path = os.path.join(PLAN, rel)
        if not os.path.exists(path):
            continue
        with open(path) as f:
            done, total = count_tasks(f.read())
        units.append((label, done, total))
    return units


def strip_checklists(text):
    """Drop the duplicated per-week/module checkbox lists from a phase file.

    The `* Pages` links above and the week pages themselves remain the only
    checklists. Idempotent: returns the input unchanged once already stripped.
    """
    exit_m = EXIT_HEAD_RE.search(text)
    if not exit_m:
        return text
    head = text[:exit_m.start()]
    unit_m = UNIT_HEAD_RE.search(head)
    if not unit_m:
        return text
    head = head[:unit_m.start()].rstrip("\n")
    return f"{head}\n\n---\n\n{text[exit_m.start():]}"


def phase_file(phase):
    hits = glob.glob(os.path.join(PLAN, f"phase-{phase}-*.md"))
    return hits[0] if hits else None


def phase_block(phase, units):
    done = sum(u[1] for u in units)
    total = sum(u[2] for u in units)
    p = pct(done, total)
    title = PHASE_META[phase][0]
    out = ["## Progress", "",
           f"**{title}** \u2014 **{done} / {total}** tasks complete (**{p}%**)", "",
           bar(p), "",
           "| Week / Module | Tasks | Progress |",
           "| --- | --- | --- |"]
    for label, c, t in units:
        up = pct(c, t)
        out.append(f"| {label} | {c} / {t} | {bar(up)} {up}% |")
    out += ["",
            "_Auto-generated from the linked week pages. Updated by "
            "[`scripts/update_progress.py`](../scripts/update_progress.py)._"]
    return "\n".join(out)


def plan_block(phase_stats):
    done = sum(s["done"] for s in phase_stats.values())
    total = sum(s["total"] for s in phase_stats.values())
    p = pct(done, total)
    out = ["## Progress", "",
           f"**Overall** \u2014 **{done} / {total}** tasks complete (**{p}%**)", "",
           bar(p), "",
           "| Phase | Timeline | Tasks | Progress |",
           "| --- | --- | --- | --- |"]
    for phase in sorted(phase_stats):
        s = phase_stats[phase]
        up = pct(s["done"], s["total"])
        title, timeline = PHASE_META[phase]
        out.append(f"| {phase} \u2014 {title} | {timeline} | "
                   f"{s['done']} / {s['total']} | {bar(up)} {up}% |")
    out += ["",
            "_Auto-generated from checklist state. Run "
            "[`scripts/update_progress.py`](scripts/update_progress.py) (or let the "
            "`Update progress bars` GitHub Action run it) to refresh._"]
    return "\n".join(out)


def inject(text, block, anchor=None):
    wrapped = f"{START}\n{block}\n{END}"
    if START in text and END in text:
        pre = text[:text.index(START)]
        post = text[text.index(END) + len(END):].lstrip("\n")
        return pre + wrapped + "\n\n" + post
    if anchor is None or anchor not in text:
        raise SystemExit("anchor not found and no existing markers")
    i = text.index(anchor)
    return text[:i] + wrapped + "\n\n" + text[i:]


def inject_after_hr(text, block):
    wrapped = f"{START}\n{block}\n{END}"
    if START in text and END in text:
        pre = text[:text.index(START)]
        post = text[text.index(END) + len(END):].lstrip("\n")
        return pre + wrapped + "\n\n" + post
    marker = "\n---\n"
    i = text.index(marker)
    return text[:i + len(marker)] + "\n" + wrapped + "\n" + text[i + len(marker):]


def main():
    phase_stats = {}
    for phase in sorted(PHASE_META):
        path = phase_file(phase)
        if not path:
            continue
        with open(path) as f:
            text = f.read()
        units = parse_units(text)
        phase_stats[phase] = {
            "done": sum(u[1] for u in units),
            "total": sum(u[2] for u in units),
        }
        text = strip_checklists(text)
        new_text = inject_after_hr(text, phase_block(phase, units))
        if new_text != text:
            with open(path, "w") as f:
                f.write(new_text)

    lp = os.path.join(ROOT, "learning-plan.md")
    with open(lp) as f:
        text = f.read()
    new_text = inject(text, plan_block(phase_stats), anchor="## Goal")
    if new_text != text:
        with open(lp, "w") as f:
            f.write(new_text)

    for phase in sorted(PHASE_META):
        s = phase_stats[phase]
        print(f"Phase {phase}: {s['done']}/{s['total']} ({pct(s['done'], s['total'])}%)")
    d = sum(s["done"] for s in phase_stats.values())
    t = sum(s["total"] for s in phase_stats.values())
    print(f"Overall: {d}/{t} ({pct(d, t)}%)")


if __name__ == "__main__":
    main()
