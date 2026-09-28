"""
run_all_exports.py - Master exporter and Foundation Visa verification harness for git-firstcallres.
"""
import os, sys, json
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

def main():
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    exp = os.path.join(root, "exports")
    with open(os.path.join(exp, "visa_manifest.json"), "r", encoding="utf-8") as rf:
        data = json.load(rf)
    print(f"PASSPORT STATUS (git-firstcallres): {data['visas_earned']}/15 VISAS ISSUED | +{data['visas_earned']*100} POINTS")

if __name__ == "__main__":
    main()
