"""CLI for diff-aware-code-distiller."""
import sys
import argparse
from .distiller import DiffAwareCodeDistiller


def main():
    parser = argparse.ArgumentParser(description="Diff-Aware Code Distiller CLI")
    parser.add_argument("--demo", action="store_true", help="Run diff distiller demo")
    args = parser.parse_args()

    if args.demo:
        distiller = DiffAwareCodeDistiller()
        sample_diff = """--- a/app.py
+++ b/app.py
@@ -10,3 +10,6 @@
-def old_handler():
-    pass
+def new_handler(request):
+    return {"status": "ok"}
+class AuthController:
+    pass
"""
        summaries = distiller.distill(sample_diff)
        print(f"[+] Distilled {len(summaries)} file diffs:")
        for s in summaries:
            print(f"    File: {s.filename} (+{s.added_lines}, -{s.removed_lines}) | Symbols: {s.modified_symbols}")
    else:
        parser.print_help()
    sys.exit(0)


if __name__ == "__main__":
    main()
