#!/usr/bin/env python
\"\"\"
run_pipeline.py
---------------
Convenience wrapper to re-execute the full end-to-end pipeline via Snakemake.

Usage (from project root):
    python run_pipeline.py              # run full pipeline
    python run_pipeline.py --dry-run    # preview without executing
    python run_pipeline.py --forceall   # force re-run all stages
    python run_pipeline.py --cores 4    # specify CPU cores
\"\"\"

import subprocess
import argparse
import sys


def main():
    parser = argparse.ArgumentParser(
        description="Run the Financial Inclusion & Poverty end-to-end pipeline."
    )
    parser.add_argument("--dry-run", "-n", action="store_true",
        help="Preview which rules would run without executing them.")
    parser.add_argument("--forceall", "-F", action="store_true",
        help="Force re-execution of all rules, even if outputs are up-to-date.")
    parser.add_argument("--cores", type=int, default=1,
        help="Number of CPU cores Snakemake may use (default: 1).")
    args = parser.parse_args()

    cmd = ["snakemake", "--cores", str(args.cores)]

    if args.dry_run:
        cmd.append("--dry-run")
        print("DRY RUN — no files will be created or modified.\n")
    if args.forceall:
        cmd.append("--forceall")
        print("FORCE ALL — re-running every stage regardless of timestamps.\n")

    print(f"Executing: {' '.join(cmd)}\n" + "=" * 60)
    result = subprocess.run(cmd)

    if result.returncode != 0:
        print("\nPipeline failed. Check the output above for which rule errored.")
        sys.exit(result.returncode)
    else:
        print("\nPipeline completed successfully.")
        print("  Processed data -> data/processed/")
        print("  Figures        -> output/")


if __name__ == "__main__":
    main()
