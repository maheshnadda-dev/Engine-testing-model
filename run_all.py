"""
=============================================================================
ENGINE ML PROJECT — MASTER RUN SCRIPT
=============================================================================
Runs Tasks 1, 2, and 3 in the correct order.

Usage (from the project root):
    python run_all.py          # run all tasks
    python run_all.py --task 1 # run only Task 1
    python run_all.py --task 2 # run only Task 2
    python run_all.py --gui    # launch GUI only (requires Tasks 1 & 2 done)
=============================================================================
"""

import sys
import os
import argparse
import time

BASE_DIR    = os.path.dirname(os.path.abspath(__file__))
SCRIPTS_DIR = os.path.join(BASE_DIR, "Scripts")
GUI_DIR     = os.path.join(BASE_DIR, "GUI")
sys.path.insert(0, SCRIPTS_DIR)
sys.path.insert(0, GUI_DIR)


def banner(text: str, char: str = "═", width: int = 65):
    print(f"\n{char*width}")
    print(f"  {text}")
    print(f"{char*width}\n")


def run_task1():
    banner("TASK 1: Monte Carlo Simulation & Statistical Analysis")
    t0 = time.time()
    import task1_monte_carlo
    task1_monte_carlo.main()
    print(f"  Task 1 completed in {time.time()-t0:.1f}s\n")


def run_task2():
    banner("TASK 2: Machine Learning Model Training & Evaluation")
    t0 = time.time()
    import task2_ml_models
    task2_ml_models.main()
    print(f"  Task 2 completed in {time.time()-t0:.1f}s\n")


def run_gui():
    banner("TASK 3: Launching Desktop GUI Application")
    import engine_gui
    engine_gui.main()


def main():
    parser = argparse.ArgumentParser(
        description="Engine ML Project — Master Run Script")
    parser.add_argument("--task", type=int, choices=[1, 2],
                        help="Run specific task only (1 or 2)")
    parser.add_argument("--gui",  action="store_true",
                        help="Launch the GUI (Task 3)")
    args = parser.parse_args()

    banner("ENGINE ML PROJECT — MASTER RUNNER", "═")

    if args.gui:
        run_gui()
    elif args.task == 1:
        run_task1()
    elif args.task == 2:
        run_task2()
    else:
        # Run all in sequence
        run_task1()
        run_task2()
        print("\n  All tasks complete. To launch the GUI, run:")
        print("  python run_all.py --gui\n")
        print("  Or directly: python GUI/engine_gui.py\n")


if __name__ == "__main__":
    main()
