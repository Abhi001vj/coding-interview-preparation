#!/usr/bin/env python3
"""
DSA Practice Progress Tracker

Tracks problem attempts, success rates, and identifies weak areas.
"""

import argparse
import json
from pathlib import Path
from datetime import datetime, timedelta
from collections import defaultdict

SCRIPT_DIR = Path(__file__).parent
PROGRESS_FILE = SCRIPT_DIR / "progress.json"
LOG_FILE = SCRIPT_DIR / "practice_log.json"


def load_data(filepath):
    if filepath.exists():
        with open(filepath) as f:
            return json.load(f)
    return {}


def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)


def log_attempt(problem_id, pattern, difficulty, time_taken, result, bugs=None, notes=None):
    """Log a problem attempt."""
    log = load_data(LOG_FILE)
    if "attempts" not in log:
        log["attempts"] = []

    attempt = {
        "date": datetime.now().isoformat(),
        "problem_id": problem_id,
        "pattern": pattern,
        "difficulty": difficulty,
        "time_taken": time_taken,
        "result": result,  # "solved", "partial", "failed"
        "bugs": bugs or [],
        "notes": notes or ""
    }

    log["attempts"].append(attempt)
    save_data(LOG_FILE, log)

    # Update progress
    progress = load_data(PROGRESS_FILE)
    if "solved" not in progress:
        progress["solved"] = []
    if "failed" not in progress:
        progress["failed"] = []
    if "pattern_stats" not in progress:
        progress["pattern_stats"] = {}

    if result == "solved":
        if problem_id not in progress["solved"]:
            progress["solved"].append(problem_id)
        if problem_id in progress["failed"]:
            progress["failed"].remove(problem_id)
    elif result == "failed":
        if problem_id not in progress["failed"]:
            progress["failed"].append(problem_id)

    # Update pattern stats
    if pattern not in progress["pattern_stats"]:
        progress["pattern_stats"][pattern] = {"attempts": 0, "solved": 0, "total_time": 0}

    progress["pattern_stats"][pattern]["attempts"] += 1
    progress["pattern_stats"][pattern]["total_time"] += time_taken
    if result == "solved":
        progress["pattern_stats"][pattern]["solved"] += 1

    save_data(PROGRESS_FILE, progress)
    print(f"Logged: {problem_id} - {result}")


def show_stats(period="all"):
    """Show practice statistics."""
    log = load_data(LOG_FILE)
    progress = load_data(PROGRESS_FILE)

    if not log.get("attempts"):
        print("No practice data yet. Start practicing!")
        return

    attempts = log["attempts"]

    # Filter by period
    if period == "week":
        cutoff = datetime.now() - timedelta(days=7)
        attempts = [a for a in attempts if datetime.fromisoformat(a["date"]) > cutoff]
    elif period == "month":
        cutoff = datetime.now() - timedelta(days=30)
        attempts = [a for a in attempts if datetime.fromisoformat(a["date"]) > cutoff]

    if not attempts:
        print(f"No practice data for the past {period}")
        return

    # Calculate stats
    total = len(attempts)
    solved = sum(1 for a in attempts if a["result"] == "solved")
    failed = sum(1 for a in attempts if a["result"] == "failed")
    partial = total - solved - failed

    avg_time = sum(a["time_taken"] for a in attempts) / total

    # Pattern breakdown
    pattern_stats = defaultdict(lambda: {"total": 0, "solved": 0, "time": 0})
    for a in attempts:
        pattern_stats[a["pattern"]]["total"] += 1
        pattern_stats[a["pattern"]]["time"] += a["time_taken"]
        if a["result"] == "solved":
            pattern_stats[a["pattern"]]["solved"] += 1

    # Bug frequency
    bug_counts = defaultdict(int)
    for a in attempts:
        for bug in a.get("bugs", []):
            bug_counts[bug] += 1

    # Display
    print("\n" + "=" * 60)
    print(f"PRACTICE STATISTICS ({period.upper()})")
    print("=" * 60)

    print(f"\nOverall:")
    print(f"  Total attempts: {total}")
    print(f"  Solved: {solved} ({100*solved/total:.1f}%)")
    print(f"  Partial: {partial} ({100*partial/total:.1f}%)")
    print(f"  Failed: {failed} ({100*failed/total:.1f}%)")
    print(f"  Average time: {avg_time:.1f} minutes")

    print(f"\nBy Pattern:")
    for pattern, stats in sorted(pattern_stats.items(), key=lambda x: -x[1]["total"]):
        success_rate = 100 * stats["solved"] / stats["total"] if stats["total"] > 0 else 0
        avg_pattern_time = stats["time"] / stats["total"] if stats["total"] > 0 else 0
        status = "OK" if success_rate >= 70 else "NEEDS WORK"
        print(f"  {pattern}: {stats['solved']}/{stats['total']} ({success_rate:.0f}%) "
              f"avg {avg_pattern_time:.0f}min [{status}]")

    if bug_counts:
        print(f"\nCommon Bugs:")
        for bug, count in sorted(bug_counts.items(), key=lambda x: -x[1])[:5]:
            print(f"  {bug}: {count} times")

    # Recommendations
    print(f"\nRecommendations:")
    weak_patterns = [p for p, s in pattern_stats.items()
                    if s["total"] >= 2 and s["solved"]/s["total"] < 0.7]
    if weak_patterns:
        print(f"  Focus on: {', '.join(weak_patterns)}")

    slow_patterns = [p for p, s in pattern_stats.items()
                    if s["total"] >= 2 and s["time"]/s["total"] > 30]
    if slow_patterns:
        print(f"  Speed up: {', '.join(slow_patterns)}")

    total_solved = len(progress.get("solved", []))
    print(f"\nTotal unique problems solved: {total_solved}")
    print("=" * 60 + "\n")


def find_problems(pattern=None, difficulty=None, status=None):
    """Find problems matching criteria."""
    from generate_problem import PROBLEM_BANK

    progress = load_data(PROGRESS_FILE)
    solved = set(progress.get("solved", []))
    failed = set(progress.get("failed", []))

    results = []

    patterns_to_check = [pattern] if pattern else PROBLEM_BANK.keys()
    difficulties = [difficulty] if difficulty else ["easy", "medium", "hard"]

    for p in patterns_to_check:
        if p not in PROBLEM_BANK:
            continue
        for d in difficulties:
            for problem in PROBLEM_BANK[p].get(d, []):
                problem_status = "solved" if problem["id"] in solved else \
                               "failed" if problem["id"] in failed else "unsolved"

                if status and problem_status != status:
                    continue

                results.append({
                    "id": problem["id"],
                    "name": problem["name"],
                    "pattern": p,
                    "difficulty": d,
                    "status": problem_status
                })

    print(f"\nFound {len(results)} problems:")
    for r in results:
        status_symbol = "✓" if r["status"] == "solved" else \
                       "✗" if r["status"] == "failed" else "○"
        print(f"  [{status_symbol}] {r['id']}: {r['name']} ({r['pattern']}, {r['difficulty']})")


def interactive_log():
    """Interactive logging of a practice session."""
    print("\n=== Log Practice Session ===\n")

    problem_id = input("Problem ID (e.g., LC721): ").strip()

    print("\nPatterns: snapshot-versioning, union-find, sliding-window, monotonic-stack,")
    print("          binary-search, dynamic-programming, graph-bfs-dfs, tree-traversal,")
    print("          heap-priority-queue, backtracking, two-pointers, linked-list")
    pattern = input("Pattern: ").strip()

    difficulty = input("Difficulty (easy/medium/hard): ").strip()

    time_taken = int(input("Time taken (minutes): "))

    result = input("Result (solved/partial/failed): ").strip()

    print("\nCommon bugs: off-by-one, wrong-init, mutation-bug, reference-vs-copy,")
    print("             wrong-variable, missing-return, boundary-error, logic-error")
    bugs_input = input("Bugs (comma-separated, or empty): ").strip()
    bugs = [b.strip() for b in bugs_input.split(",")] if bugs_input else []

    notes = input("Notes (optional): ").strip()

    log_attempt(problem_id, pattern, difficulty, time_taken, result, bugs, notes)
    print("\nSession logged successfully!")


def main():
    parser = argparse.ArgumentParser(description="Track DSA practice progress")
    subparsers = parser.add_subparsers(dest="command", help="Command")

    # Log command
    log_parser = subparsers.add_parser("log", help="Log a practice session")
    log_parser.add_argument("--problem", "-p", help="Problem ID")
    log_parser.add_argument("--pattern", help="Pattern")
    log_parser.add_argument("--difficulty", "-d", help="Difficulty")
    log_parser.add_argument("--time", "-t", type=int, help="Time taken")
    log_parser.add_argument("--result", "-r", choices=["solved", "partial", "failed"])

    # Stats command
    stats_parser = subparsers.add_parser("stats", help="Show statistics")
    stats_parser.add_argument("--week", action="store_true", help="Last 7 days")
    stats_parser.add_argument("--month", action="store_true", help="Last 30 days")

    # Find command
    find_parser = subparsers.add_parser("find", help="Find problems")
    find_parser.add_argument("--pattern", "-p", help="Filter by pattern")
    find_parser.add_argument("--difficulty", "-d", help="Filter by difficulty")
    find_parser.add_argument("--status", "-s", choices=["solved", "failed", "unsolved"])

    args = parser.parse_args()

    if args.command == "log":
        if args.problem and args.pattern and args.time and args.result:
            log_attempt(args.problem, args.pattern, args.difficulty or "medium",
                       args.time, args.result)
        else:
            interactive_log()

    elif args.command == "stats":
        period = "week" if args.week else "month" if args.month else "all"
        show_stats(period)

    elif args.command == "find":
        find_problems(args.pattern, args.difficulty, args.status)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
