"""Core Diff-Aware Code Distiller implementation."""
import re
from typing import List, Dict, Any


class FileDiffSummary:
    def __init__(self, filename: str, added_lines: int, removed_lines: int, modified_symbols: List[str]):
        self.filename = filename
        self.added_lines = added_lines
        self.removed_lines = removed_lines
        self.modified_symbols = modified_symbols


class DiffAwareCodeDistiller:
    def distill(self, diff_text: str) -> List[FileDiffSummary]:
        summaries: List[FileDiffSummary] = []
        current_file = None
        added = 0
        removed = 0
        symbols = set()

        for line in diff_text.splitlines():
            if line.startswith("+++ b/"):
                if current_file:
                    summaries.append(FileDiffSummary(current_file, added, removed, sorted(list(symbols))))
                current_file = line[6:]
                added = 0
                removed = 0
                symbols = set()
            elif line.startswith("+") and not line.startswith("+++"):
                added += 1
                match = re.search(r'(?:def|class)\s+([a-zA-Z0-9_]+)', line)
                if match:
                    symbols.add(match.group(1))
            elif line.startswith("-") and not line.startswith("---"):
                removed += 1
                match = re.search(r'(?:def|class)\s+([a-zA-Z0-9_]+)', line)
                if match:
                    symbols.add(match.group(1))

        if current_file:
            summaries.append(FileDiffSummary(current_file, added, removed, sorted(list(symbols))))

        return summaries
