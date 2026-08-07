# Linked List Cycle

- **Problem Number**: 141
- **Platform**: LeetCode #141
- **Difficulty**: Easy
- **Pattern**: Hash Set / Address Tracking

---

## Brute Force Intuition

Traverse the linked list while storing visited node memory addresses (pointers) in a Hash Set `visited`. If we encounter a node pointer that already exists in `visited`, a cycle is detected! If `curr` reaches `nullptr`, there is no cycle.

---

## Algorithm

1. Create a `std::unordered_set<ListNode*> visited`.
2. `curr = head`.
3. While `curr != nullptr`:
   a. If `visited.count(curr) > 0`: return `true`.
   b. `visited.insert(curr)`.
   c. `curr = curr->next`.
4. Return `false`.

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
    bool hasCycle(ListNode *head) {
        std::unordered_set<ListNode*> visited;
        ListNode* curr = head;
        
        while (curr != nullptr) {
            if (visited.count(curr)) {
                return true;
            }
            visited.insert(curr);
            curr = curr->next;
        }
        
        return false;
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
  - Stores up to $N$ node pointers in the Hash Set.

---

## Why This Approach Is Not Optimal

Using a Hash Set requires $\mathcal{O}(N)$ auxiliary space. By using **Floyd's Cycle Detection Algorithm (Tortoise and Hare)**, we can detect cycles in $\mathcal{O}(N)$ time with $\mathcal{O}(1)$ space.
