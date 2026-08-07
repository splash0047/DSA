# Partition List

- **Problem Number**: 86
- **Platform**: LeetCode #86
- **Difficulty**: Medium
- **Pattern**: Two Auxiliary Arrays / Vectors

---

## Brute Force Intuition

Traverse the linked list and separate node values into two vectors: `less_vals` for values $< x$ and `greater_vals` for values $\ge x$. Then overwrite node values in the linked list sequentially with elements from `less_vals` followed by `greater_vals`.

---

## Algorithm

1. Extract nodes into `vector<int> less_vals` and `vector<int> greater_vals`.
2. Traverse `head` and populate vectors:
   - If `curr->val < x`: `less_vals.push_back(curr->val)`.
   - Else: `greater_vals.push_back(curr->val)`.
3. Reset `curr = head`.
4. Overwrite values from `less_vals`, then from `greater_vals`.
5. Return `head`.

---

## Code

```cpp
#include <vector>

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        std::vector<int> less_vals;
        std::vector<int> greater_vals;
        
        ListNode* curr = head;
        while (curr != nullptr) {
            if (curr->val < x) {
                less_vals.push_back(curr->val);
            } else {
                greater_vals.push_back(curr->val);
            }
            curr = curr->next;
        }
        
        curr = head;
        for (int v : less_vals) {
            curr->val = v;
            curr = curr->next;
        }
        for (int v : greater_vals) {
            curr->val = v;
            curr = curr->next;
        }
        
        return head;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Two passes over $N$ nodes.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Vector storage for $N$ values.

---

## Why This Approach Is Not Optimal

Using vectors requires $\mathcal{O}(N)$ auxiliary memory and mutates node values. By using **Two Dummy Sentinel Lists (Less & Greater)**, we can partition the actual node pointers in-place with $\mathcal{O}(1)$ space.
