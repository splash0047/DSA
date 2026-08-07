# Linked List Cycle II

- **Problem Number**: 142
- **Platform**: LeetCode #142
- **Difficulty**: Medium
- **Pattern**: Hash Set Address Tracking

---

## Brute Force Intuition

Traverse the linked list and store visited node memory addresses (pointers) in a Hash Set `visited`. The very first node pointer that is already present in `visited` is the exact starting node of the cycle!

---

## Algorithm

1. `visited = unordered_set<ListNode*>()`.
2. `curr = head`.
3. While `curr != nullptr`:
   a. If `visited.count(curr) > 0`: return `curr`.
   b. `visited.insert(curr)`.
   c. `curr = curr->next`.
4. Return `nullptr`.

---

## Code

```cpp
#include <unordered_set>

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        std::unordered_set<ListNode*> visited;
        ListNode* curr = head;
        
        while (curr != nullptr) {
            if (visited.count(curr)) {
                return curr; // First repeated node is the cycle start
            }
            visited.insert(curr);
            curr = curr->next;
        }
        
        return nullptr;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Hash set lookup and insertion take $\mathcal{O}(1)$ average time per node.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Stores up to $N$ node pointers in Hash Set memory.

---

## Why This Approach Is Not Optimal

Using a Hash Set requires $\mathcal{O}(N)$ auxiliary space. By using **Floyd's Cycle Entry Finding Algorithm**, we can locate the exact cycle starting node in $\mathcal{O}(N)$ time with $\mathcal{O}(1)$ space.
