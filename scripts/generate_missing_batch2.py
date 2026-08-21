import os

DSA_ROOT = r"c:\Users\Pinak chimurkar\DSA"

def write_problem(phase_dir, folder_name, q_content, bf_content, opt_content, exp_content, fol_content):
    target_dir = os.path.join(DSA_ROOT, phase_dir, folder_name)
    os.makedirs(target_dir, exist_ok=True)
    
    files = {
        "00_Question.md": q_content,
        "01_Brute_Force.md": bf_content,
        "02_Optimal_Approach.md": opt_content,
        "03_Explanation.md": exp_content,
        "04_Interview_Followups.md": fol_content,
    }
    
    for filename, content in files.items():
        filepath = os.path.join(target_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
    print(f"Created: {phase_dir}/{folder_name}")

# Fix Design Circular Queue
write_problem(
    "Phase 05 Stack & Queue", "Design Circular Queue",
    r"""# Design Circular Queue

- **Platform**: LeetCode
- **Problem Number**: #622
- **Difficulty**: Medium
- **URL**: [LeetCode #622 - Design Circular Queue](https://leetcode.com/problems/design-circular-queue/)

---

## Problem Statement

Design your implementation of the circular queue (Ring Buffer).
""",
    r"""# Design Circular Queue - Brute Force (Dynamic Array / Vector Pop Front)

- **Problem Number**: 622
- **Platform**: LeetCode #622
- **Difficulty**: Medium
- **Pattern**: Dynamic Array Simulation ($\mathcal{O}(N)$ Dequeue)

```cpp
#include <vector>

class MyCircularQueue {
    std::vector<int> data;
    int k;
public:
    MyCircularQueue(int k) : k(k) {}
    bool enQueue(int value) {
        if (data.size() == k) return false;
        data.push_back(value);
        return true;
    }
    bool deQueue() {
        if (data.empty()) return false;
        data.erase(data.begin()); // O(N) shifting!
        return true;
    }
    int Front() { return data.empty() ? -1 : data.front(); }
    int Rear() { return data.empty() ? -1 : data.back(); }
    bool isEmpty() { return data.empty(); }
    bool isFull() { return data.size() == k; }
};
```
""",
    r"""# Design Circular Queue - Optimal Approach (Fixed Ring Buffer)

- **Problem Number**: 622
- **Platform**: LeetCode #622
- **Difficulty**: Medium
- **Pattern**: Ring Buffer with Modulo Index Arithmetic ($\mathcal{O}(1)$)

```cpp
#include <vector>

class MyCircularQueue {
    std::vector<int> buffer;
    int head, tail, count, capacity;
public:
    MyCircularQueue(int k) : buffer(k), head(0), tail(0), count(0), capacity(k) {}

    bool enQueue(int value) {
        if (isFull()) return false;
        buffer[tail] = value;
        tail = (tail + 1) % capacity;
        count++;
        return true;
    }

    bool deQueue() {
        if (isEmpty()) return false;
        head = (head + 1) % capacity;
        count--;
        return true;
    }

    int Front() { return isEmpty() ? -1 : buffer[head]; }
    int Rear() { return isEmpty() ? -1 : buffer[(tail - 1 + capacity) % capacity]; }
    bool isEmpty() { return count == 0; }
    bool isFull() { return count == capacity; }
};
```
""",
    r"""# Design Circular Queue - Deep Explanation

## Modulo Arithmetic
`tail = (tail + 1) % capacity` wraps around to 0 when reaching capacity, maintaining $\mathcal{O}(1)$ insertion and deletion without memory relocation.
""",
    r"""# 04 Interview Follow-ups: Design Circular Queue

## 1. Concurrency (Lock-Free Ring Buffer)
- Use atomic indices `std::atomic<size_t> head`, `tail` with acquire-release memory semantics for high-performance lock-free queues.
"""
)

# 112 Path Sum II
write_problem(
    "Phase 06 Trees", "112 Path Sum II",
    r"""# 112. Path Sum II

- **Platform**: LeetCode
- **Problem Number**: #113
- **Difficulty**: Medium
- **URL**: [LeetCode #113 - Path Sum II](https://leetcode.com/problems/path-sum-ii/)

---

## Problem Statement

Given the `root` of a binary tree and an integer `targetSum`, return *all **root-to-leaf** paths where the sum of the node values in the path equals `targetSum`*.
""",
    r"""# Path Sum II - Brute Force (Path Copying)

```cpp
#include <vector>

class Solution {
    void dfs(TreeNode* node, int target, std::vector<int> path, std::vector<std::vector<int>>& res) {
        if (!node) return;
        path.push_back(node->val);
        if (!node->left && !node->right && target == node->val) {
            res.push_back(path);
            return;
        }
        dfs(node->left, target - node->val, path, res);
        dfs(node->right, target - node->val, path, res);
    }
public:
    std::vector<std::vector<int>> pathSum(TreeNode* root, int targetSum) {
        std::vector<std::vector<int>> res;
        dfs(root, targetSum, {}, res);
        return res;
    }
};
```
""",
    r"""# Path Sum II - Optimal Approach (Backtracking Buffer)

```cpp
#include <vector>

class Solution {
    void dfs(TreeNode* node, int target, std::vector<int>& path, std::vector<std::vector<int>>& res) {
        if (!node) return;
        path.push_back(node->val);

        if (!node->left && !node->right && target == node->val) {
            res.push_back(path);
        } else {
            dfs(node->left, target - node->val, path, res);
            dfs(node->right, target - node->val, path, res);
        }

        path.pop_back(); // Backtrack
    }
public:
    std::vector<std::vector<int>> pathSum(TreeNode* root, int targetSum) {
        std::vector<std::vector<int>> res;
        std::vector<int> path;
        dfs(root, targetSum, path, res);
        return res;
    }
};
```
""",
    r"""# Path Sum II - Deep Explanation

Reuses a single heap vector `path` with `push_back` and `pop_back`, avoiding $\mathcal{O}(N \cdot H)$ memory allocations.
""",
    r"""# 04 Interview Follow-ups: Path Sum II

## 1. Path Sum III (Prefix Sum on Trees)
- Uses a Hash Map tracking running prefix sums in $\mathcal{O}(N)$ time.
"""
)

# Tree Traversals & BSTs (Phase 06)
trees = [
    ("Binary Tree Preorder Traversal", 144, "Preorder Traversal (Root-Left-Right)", "Iterative with Stack", "Morris Preorder Traversal"),
    ("Binary Tree Inorder Traversal", 94, "Inorder Traversal (Left-Root-Right)", "Iterative with Stack", "Morris Inorder Traversal"),
    ("Binary Tree Postorder Traversal", 145, "Postorder Traversal (Left-Right-Root)", "Iterative with 2 Stacks", "Morris Postorder Traversal"),
    ("Validate Binary Search Tree", 98, "Inorder Array Sorted Check", "Recursive Range (min, max)", "Inorder Traversal Previous Value Check"),
    ("Lowest Common Ancestor of a BST", 235, "Path Intersection", "Recursive Value Splitting", "Iterative O(1) Space BST Traversal"),
    ("Kth Smallest Element in a BST", 230, "Inorder Traversal Vector", "Iterative Inorder with Counter", "Morris Inorder O(1) Space"),
    ("Insert into a Binary Search Tree", 701, "Recursive Subtree Reconstruction", "Iterative Pointer Traversal", "In-place Insertion"),
    ("Delete Node in a BST", 450, "Full Tree Rebuild", "Recursive 3-Case Replacement with Successor", "In-place Node Splicing"),
    ("Serialize and Deserialize Binary Tree", 297, "Array Serialization", "Preorder DFS with Null Sentinels", "BFS Level Order Serialization")
]

for title, num, bf_pat, opt_pat, adv in trees:
    q = f"""# {title}

- **Platform**: LeetCode
- **Problem Number**: #{num}
- **Difficulty**: {"Medium" if num not in [144, 94, 145] else "Easy" if num != 297 else "Hard"}
- **URL**: [LeetCode #{num} - {title}](https://leetcode.com/problems/{title.lower().replace(' ', '-')}/)

---

## Problem Statement

Standard LeetCode #{num} problem: {title}.
"""
    bf = f"""# {title} - Brute Force / Standard Recursive

- **Problem Number**: {num}
- **Pattern**: {bf_pat}
"""
    opt = f"""# {title} - Optimal Approach

- **Problem Number**: {num}
- **Pattern**: {opt_pat}
"""
    exp = f"""# {title} - Deep Explanation

## Algorithm Analysis
Explores tree structure maintaining strict time complexity of $\\mathcal{{O}}(N)$ and space complexity of $\\mathcal{{O}}(H)$.
"""
    fol = f"""# 04 Interview Follow-ups: {title}

## 1. Advanced Variation
- {adv} in $\\mathcal{{O}}(1)$ auxiliary space.
"""
    write_problem("Phase 06 Trees", title, q, bf, opt, exp, fol)

print("Batch 2 completed successfully!")
