# Intersection of Two Linked Lists

- **Problem Number**: 160
- **Platform**: LeetCode #160
- **Difficulty**: Easy
- **Pattern**: Hash Set Address Tracking

---

## Brute Force Intuition

Traverse `listA` completely and insert all node pointers (memory addresses) into a Hash Set `visited`. Then traverse `listB`; the very first node pointer found in `visited` is the intersection node!

---

## Algorithm

1. `visited = unordered_set<ListNode*>()`.
2. `currA = headA`.
3. While `currA != nullptr`:
   a. `visited.insert(currA)`.
   b. `currA = currA->next`.
4. `currB = headB`.
5. While `currB != nullptr`:
   a. If `visited.count(currB) > 0`: return `currB`.
   b. `currB = currB->next`.
6. Return `nullptr`.

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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        std::unordered_set<ListNode*> visited;
        
        ListNode* currA = headA;
        while (currA != nullptr) {
            visited.insert(currA);
            currA = currA->next;
        }
        
        ListNode* currB = headB;
        while (currB != nullptr) {
            if (visited.count(currB)) {
                return currB;
            }
            currB = currB->next;
        }
        
        return nullptr;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(M + N)$
  - Hash set insertions and lookups take $\mathcal{O}(1)$ average time per node.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(M)$
  - Stores up to $M$ node pointers in Hash Set memory.

---

## Why This Approach Is Not Optimal

Using a Hash Set requires $\mathcal{O}(M)$ auxiliary space. By using **Two Pointers Path Equivalence Switching**, we can find the intersection node in $\mathcal{O}(M + N)$ time with $\mathcal{O}(1)$ space.
