import time

def print_header(title):
    print("\n" + "="*50)
    print(f" {title}")
    print("="*50)

def step(msg):
    print(f"\n👉 {msg}")

def show_state(node, count, ans, note=""):
    print(f"   [Node {node}] count={count}, ans={ans}  | {note}")

def main():
    print_header("MANUAL TRACE: Sum of Distances in Tree")
    print("Tree Structure:")
    print("      0")
    print("     / \\")
    print("    1   2")
    print("       /|\\")
    print("      3 4 5")
    print("\nN = 6")
    
    # --- DFS 1 ---
    print_header("PHASE 1: DFS (Bottom-Up) - Gather Subtree Info")
    print("Goal: Calculate 'count' (subtree size) and 'ans' (sum dist) relative to Node 0")

    step("Leaves return 1 (themselves)")
    show_state(1, 1, 0, "Leaf")
    show_state(3, 1, 0, "Leaf")
    show_state(4, 1, 0, "Leaf")
    show_state(5, 1, 0, "Leaf")

    step("Processing Node 2 (Children: 3, 4, 5)")
    print("   count[2] = 1 (self) + 1(3) + 1(4) + 1(5) = 4")
    print("   ans[2]   = (0+1) + (0+1) + (0+1) = 3")
    show_state(2, 4, 3, "Subtree includes 2,3,4,5")

    step("Processing Node 0 (Children: 1, 2)")
    print("   count[0] = 1 (self) + 1(1) + 4(2) = 6")
    print("   ans[0] from child 1: ans[1] + count[1] = 0 + 1 = 1")
    print("   ans[0] from child 2: ans[2] + count[2] = 3 + 4 = 7")
    print("   Total ans[0] = 1 + 7 = 8")
    show_state(0, 6, 8, "Root Answer Calculated!")

    # --- DFS 2 ---
    print_header("PHASE 2: DFS (Top-Down) - Re-Rooting")
    print("Formula: ans[child] = ans[parent] - count[child] + (N - count[child])")
    print("Meaning: closer_nodes = count[child], farther_nodes = N - count[child]")

    step("Move Root 0 -> 1")
    print("   Moving CLOSER to subtree 1 (size 1)")
    print("   Moving FARTHER from others (size 5)")
    print("   ans[1] = 8 - 1 + 5 = 12")
    show_state(1, 1, 12, "Final Answer")

    step("Move Root 0 -> 2")
    print("   Moving CLOSER to subtree 2 (size 4)")
    print("   Moving FARTHER from others (size 2)")
    print("   ans[2] = 8 - 4 + 2 = 6")
    show_state(2, 4, 6, "Final Answer")

    step("Move Root 2 -> 3 (Parent is now 2, ans[2]=6)")
    print("   Moving CLOSER to subtree 3 (size 1)")
    print("   Moving FARTHER from others (size 5)")
    print("   ans[3] = 6 - 1 + 5 = 10")
    show_state(3, 1, 10, "Final Answer")

    step("Move Root 2 -> 4 (Parent is 2)")
    print("   ans[4] = 6 - 1 + 5 = 10")
    
    step("Move Root 2 -> 5 (Parent is 2)")
    print("   ans[5] = 6 - 1 + 5 = 10")

    print_header("FINAL RESULT")
    print("Index:  0   1   2   3   4   5")
    print("Ans:   [8, 12,  6, 10, 10, 10]")

if __name__ == "__main__":
    main()
