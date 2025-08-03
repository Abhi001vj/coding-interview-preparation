# Exhaustive Stack Trace: LCA of Nodes 3 and 5

Tree structure:
```
    6
   / \
  4   8
 / \
3   5
```

## Complete Recursion Stack Trace

|__ Call 1: `lca(root=6, node1=3, node2=5)`
    |__ Line 7: `def lca(root: Node, node1: Node, node2: Node) -> Node:`
    |__ Line 8: `if not root:` → False (root=6 exists)
    |__ Line 12: `if root in (node1, node2):` → False (6 is neither 3 nor 5)
    |__ Line 15: `left = lca(root.left, node1, node2)` → Recursive call
    |   |
    |   |__ Call 2: `lca(root=4, node1=3, node2=5)`
    |       |__ Line 7: `def lca(root: Node, node1: Node, node2: Node) -> Node:`
    |       |__ Line 8: `if not root:` → False (root=4 exists)
    |       |__ Line 12: `if root in (node1, node2):` → False (4 is neither 3 nor 5)
    |       |__ Line 15: `left = lca(root.left, node1, node2)` → Recursive call
    |       |   |
    |       |   |__ Call 3: `lca(root=3, node1=3, node2=5)`
    |       |       |__ Line 7: `def lca(root: Node, node1: Node, node2: Node) -> Node:`
    |       |       |__ Line 8: `if not root:` → False (root=3 exists)
    |       |       |__ Line 12: `if root in (node1, node2):` → True (3 is node1)
    |       |       |__ Line 13: `return root` → Returns Node(3)
    |       |
    |       |__ Line 15: ← Received return value `left = Node(3)`
    |       |__ Line 16: `right = lca(root.right, node1, node2)` → Recursive call
    |       |   |
    |       |   |__ Call 4: `lca(root=5, node1=3, node2=5)`
    |       |       |__ Line 7: `def lca(root: Node, node1: Node, node2: Node) -> Node:`
    |       |       |__ Line 8: `if not root:` → False (root=5 exists)
    |       |       |__ Line 12: `if root in (node1, node2):` → True (5 is node2)
    |       |       |__ Line 13: `return root` → Returns Node(5)
    |       |
    |       |__ Line 16: ← Received return value `right = Node(5)`
    |       |__ Line 19: `if left and right:` → True (left=Node(3), right=Node(5))
    |       |__ Line 20: `return root` → Returns Node(4)
    |
    |__ Line 15: ← Received return value `left = Node(4)`
    |__ Line 16: `right = lca(root.right, node1, node2)` → Recursive call
    |   |
    |   |__ Call 5: `lca(root=8, node1=3, node2=5)`
    |       |__ Line 7: `def lca(root: Node, node1: Node, node2: Node) -> Node:`
    |       |__ Line 8: `if not root:` → False (root=8 exists)
    |       |__ Line 12: `if root in (node1, node2):` → False (8 is neither 3 nor 5)
    |       |__ Line 15: `left = lca(root.left, node1, node2)` → Recursive call
    |       |   |
    |       |   |__ Call 6: `lca(root=None, node1=3, node2=5)`
    |       |       |__ Line 7: `def lca(root: Node, node1: Node, node2: Node) -> Node:`
    |       |       |__ Line 8: `if not root:` → True (root is None)
    |       |       |__ Line 9: `return None` → Returns None
    |       |
    |       |__ Line 15: ← Received return value `left = None`
    |       |__ Line 16: `right = lca(root.right, node1, node2)` → Recursive call
    |       |   |
    |       |   |__ Call 7: `lca(root=None, node1=3, node2=5)`
    |       |       |__ Line 7: `def lca(root: Node, node1: Node, node2: Node) -> Node:`
    |       |       |__ Line 8: `if not root:` → True (root is None)
    |       |       |__ Line 9: `return None` → Returns None
    |       |
    |       |__ Line 16: ← Received return value `right = None`
    |       |__ Line 19: `if left and right:` → False (left=None, right=None)
    |       |__ Line 24: `if left:` → False (left=None)
    |       |__ Line 26: `if right:` → False (right=None)
    |       |__ Line 30: `return None` → Returns None
    |
    |__ Line 16: ← Received return value `right = None`
    |__ Line 19: `if left and right:` → False (left=Node(4), right=None)
    |__ Line 24: `if left:` → True (left=Node(4))
    |__ Line 25: `return left` → Returns Node(4)

Final result: LCA is Node(4)

## State Of Variables During Each Call

### Call 1: `lca(root=6, node1=3, node2=5)`
- Variables at start: `root=6, node1=3, node2=5, left=undefined, right=undefined`
- After line 15: `root=6, node1=3, node2=5, left=Node(4), right=undefined`
- After line 16: `root=6, node1=3, node2=5, left=Node(4), right=None`
- Return value: Node(4) via line 25

### Call 2: `lca(root=4, node1=3, node2=5)`
- Variables at start: `root=4, node1=3, node2=5, left=undefined, right=undefined`
- After line 15: `root=4, node1=3, node2=5, left=Node(3), right=undefined`
- After line 16: `root=4, node1=3, node2=5, left=Node(3), right=Node(5)`
- Return value: Node(4) via line 20

### Call 3: `lca(root=3, node1=3, node2=5)`
- Variables at start: `root=3, node1=3, node2=5`
- No recursive calls made - early return
- Return value: Node(3) via line 13

### Call 4: `lca(root=5, node1=3, node2=5)`
- Variables at start: `root=5, node1=3, node2=5`
- No recursive calls made - early return
- Return value: Node(5) via line 13

### Call 5: `lca(root=8, node1=3, node2=5)`
- Variables at start: `root=8, node1=3, node2=5, left=undefined, right=undefined`
- After line 15: `root=8, node1=3, node2=5, left=None, right=undefined`
- After line 16: `root=8, node1=3, node2=5, left=None, right=None`
- Return value: None via line 30

### Call 6: `lca(root=None, node1=3, node2=5)`
- Variables at start: `root=None, node1=3, node2=5`
- No recursive calls made - early return
- Return value: None via line 9

### Call 7: `lca(root=None, node1=3, node2=5)`
- Variables at start: `root=None, node1=3, node2=5`
- No recursive calls made - early return
- Return value: None via line 9

## Value Propagation Chain

1. Call 3 returns Node(3) to Call 2 via line 13
2. Call 4 returns Node(5) to Call 2 via line 13
3. Call 2 returns Node(4) to Call 1 via line 20 (both left and right non-null)
4. Call 6 returns None to Call 5 via line 9
5. Call 7 returns None to Call 5 via line 9
6. Call 5 returns None to Call 1 via line 30 (both left and right null)
7. Call 1 returns Node(4) via line 25 (only left is non-null)

## Memory Stack Visualization for Critical Moments

### After Call 3 executes but before it returns:
```
Memory Stack:
+-------------------------------------+
| Call 1 (Paused at line 15)         |
| root=6, node1=3, node2=5           |
| left=?, right=?                    |
+-------------------------------------+
| Call 2 (Paused at line 15)         |
| root=4, node1=3, node2=5           |
| left=?, right=?                    |
+-------------------------------------+
| Call 3 (About to return Node(3))   |
| root=3, node1=3, node2=5           |
+-------------------------------------+
```

### After Call 2 receives both left and right values but before it returns:
```
Memory Stack:
+-------------------------------------+
| Call 1 (Paused at line 15)         |
| root=6, node1=3, node2=5           |
| left=?, right=?                    |
+-------------------------------------+
| Call 2 (About to execute line 19)  |
| root=4, node1=3, node2=5           |
| left=Node(3), right=Node(5)        |
+-------------------------------------+
```

### Final stack state before returning the answer:
```
Memory Stack:
+-------------------------------------+
| Call 1 (About to execute line 25)  |
| root=6, node1=3, node2=5           |
| left=Node(4), right=None           |
+-------------------------------------+
```