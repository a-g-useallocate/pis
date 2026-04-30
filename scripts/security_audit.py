"""Simple local audit for the educational StylModa project."""
from pathlib import Path
import ast

ROOT = Path(__file__).resolve().parents[1]
DANGEROUS = {"eval", "exec", "compile", "__import__"}


def scan_file(path: Path):
    findings = []
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in DANGEROUS:
            findings.append((node.lineno, f"Use of dangerous function: {node.func.id}"))
    return findings


def main():
    print("StylModa v3 local security audit")
    total = 0
    for path in sorted(ROOT.glob("*.py")):
        findings = scan_file(path)
        if findings:
            total += len(findings)
            print(f"[WARN] {path.name}")
            for line, msg in findings:
                print(f"  line {line}: {msg}")
        else:
            print(f"[OK] {path.name}")
    print(f"Summary: {total} potentially dangerous calls found")


if __name__ == "__main__":
    main()
