import sys
from pathlib import Path

IGNORE = {".git", "__pycache__", ".ipynb_checkpoints", "node_modules", ".venv", "venv"}


def tree(root: Path, lines, prefix: str = ""):
    entries = sorted((e for e in root.iterdir() if e.name not in IGNORE), key=lambda e: (e.is_file(), e.name.lower()))
    for i, e in enumerate(entries):
        last = i == len(entries) - 1
        lines.append(f"{prefix}{'└── ' if last else '├── '}{e.name}")
        if e.is_dir():
            tree(e, lines, prefix + ("    " if last else "│   "))


if __name__ == "__main__":
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    lines = [root.name + "/"]
    tree(root, lines)
    Path("tree.txt").write_text("\n".join(lines) + "\n", encoding = "utf-8")