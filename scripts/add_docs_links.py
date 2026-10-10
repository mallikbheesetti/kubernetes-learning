#!/usr/bin/env python3
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WEEKS = ROOT / "plan" / "weeks"
MAPPING = Path(__file__).resolve().parent / "docs-links.json"
LINK_RE = re.compile(r"^(.*?)(\s+—\s+\[Docs\]\(([^)]+)\))?\s*$")

def load_mapping():
    return json.loads(MAPPING.read_text())

def derive(desc, patterns):
    for rx, u in patterns:
        if rx.search(desc):
            return u
    return None

def main():
    entries = load_mapping()
    patterns = [(re.compile(e["m"], re.IGNORECASE), e["u"]) for e in entries]

    changed_files = []
    total_added = 0
    total_fixed = 0
    unmatched = []

    for path in sorted(WEEKS.glob("*.md")):
        lines = path.read_text().split("\n")
        added = 0
        fixed = 0
        for i, line in enumerate(lines):
            if not line.startswith("- [ ] "):
                continue
            desc = re.split(r"\s+—\s+\[", line, 1)[0]
            existing = re.search(r"—\s+\[Docs\]\(([^)]+)\)\s*$", line)
            url = derive(desc, patterns)
            if url is None:
                unmatched.append(f"{path.name}: {desc[:70]}")
                continue
            if existing:
                if existing.group(1) != url:
                    lines[i] = re.sub(
                        r"(\s+)—\s+\[Docs\]\([^)]+\)\s*$",
                        r"\1— [Docs](%s)" % url,
                        line,
                    )
                    fixed += 1
                continue
            lines[i] = f"{line.rstrip()} — [Docs]({url})"
            added += 1
        if added or fixed:
            path.write_text("\n".join(lines))
            changed_files.append((path.name, added, fixed))
            total_added += added
            total_fixed += fixed

    print(f"Files updated: {len(changed_files)}")
    print(f"Docs links added: {total_added}")
    print(f"Docs links corrected: {total_fixed}")
    for name, a, f in changed_files:
        print(f"  {name}: +{a} ~{f}")
    if unmatched:
        print(f"\nUnmatched topic lines: {len(unmatched)}")
        for u in unmatched:
            print(f"  {u}")

if __name__ == "__main__":
    main()