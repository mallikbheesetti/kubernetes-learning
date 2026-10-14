#!/usr/bin/env python3
"""Add Pluralsight course + hands-on lab links to topics in week pages.

Mirrors ``scripts/add_docs_links.py``. Reads ``pluralsight-links.json`` (an
ordered list of topic matchers + a per-phase course list) and enriches:

* every checklist item inside a ``## Topics`` section of ``plan/weeks/*.md``
  with a ``[Pluralsight · Course]`` link and, when one exists, a
  ``[Pluralsight Lab · Lab]`` link;
* each ``plan/phase-*.md`` file with a ``**Pluralsight:**`` resource line.

Matching is first-match-wins, so specific patterns must precede generic ones.
The script is idempotent: lines already containing a pluralsight.com link and
phase files that already contain a ``**Pluralsight:**`` line are left alone.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WEEKS = ROOT / "plan" / "weeks"
PHASES = ROOT / "plan"
MAPPING = Path(__file__).resolve().parent / "pluralsight-links.json"

TOPIC_RE = re.compile(r"^- \[[ x]\] (.*)$")
FIRST_LINK_RE = re.compile(r"(\s+—\s+\[)")
SECTION_RE = re.compile(r"^##\s+(.*?)\s*$")
RESOURCE_RE = re.compile(r"^\*\*Resources:\*\*", re.MULTILINE)


def load_mapping():
    return json.loads(MAPPING.read_text())


def derive(desc, patterns):
    for rx, entry in patterns:
        if rx.search(desc):
            return entry
    return None


def build_links(entry):
    links = []
    if entry.get("u"):
        links.append(f"[Pluralsight · {entry['t']}]({entry['u']})")
    if entry.get("l"):
        label = entry.get("lt") or "Hands-on Lab"
        links.append(f"[Pluralsight Lab · {label}]({entry['l']})")
    return links


def topic_description(text):
    """Return just the topic text, before any existing `` — [`` resource links."""
    return text.split(" — [", 1)[0].rstrip()


def enrich_topic(line, links):
    """Insert course/lab links right after the topic description."""
    if "pluralsight.com" in line:
        return line
    parts = FIRST_LINK_RE.split(line, maxsplit=1)
    if len(parts) == 1:
        return f"{line.rstrip()} — {' — '.join(links)}"
    desc, sep, rest = parts[0], parts[1], parts[2]
    return f"{desc.rstrip()} — {' — '.join(links)}{sep}{rest}"


def process_week(path, patterns):
    lines = path.read_text().split("\n")
    in_topics = False
    added = 0
    for i, line in enumerate(lines):
        heading = SECTION_RE.match(line)
        if heading:
            in_topics = heading.group(1).strip().lower() == "topics"
            continue
        if not in_topics:
            continue
        topic = TOPIC_RE.match(line)
        if not topic:
            continue
        entry = derive(topic_description(topic.group(1)), patterns)
        if not entry:
            continue
        new = enrich_topic(line, build_links(entry))
        if new != line:
            lines[i] = new
            added += 1
    if added:
        path.write_text("\n".join(lines))
    return added


def process_phase(path, courses):
    text = path.read_text()
    if "**Pluralsight:**" in text:
        return 0
    links = " · ".join(f"[Pluralsight · {c['t']}]({c['u']})" for c in courses)
    line = f"**Pluralsight:** {links}"
    match = RESOURCE_RE.search(text)
    if match:
        end = text.find("\n\n", match.end())
        if end == -1:
            end = len(text)
        text = text[:end] + "\n\n" + line + text[end:]
    else:
        end = text.find("\n---")
        if end == -1:
            return 0
        text = text[:end] + "\n" + line + "\n" + text[end:]
    path.write_text(text)
    return 1


def main():
    mapping = load_mapping()
    patterns = [(re.compile(e["m"], re.IGNORECASE), e) for e in mapping["topics"]]

    total_topics = 0
    changed_weeks = 0
    for path in sorted(WEEKS.glob("*.md")):
        added = process_week(path, patterns)
        if added:
            changed_weeks += 1
            total_topics += added

    changed_phases = 0
    for name, courses in mapping.get("phases", {}).items():
        path = PHASES / name
        if path.exists():
            changed_phases += process_phase(path, courses)

    print(f"Week files updated:  {changed_weeks}")
    print(f"Topics enriched:     {total_topics}")
    print(f"Phase files updated: {changed_phases}")


if __name__ == "__main__":
    main()
