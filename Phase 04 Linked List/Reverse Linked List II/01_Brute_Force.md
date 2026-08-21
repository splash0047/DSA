# Reverse Linked List II - Brute Force (Vector Extraction)

- **Problem Number**: 92
- **Platform**: LeetCode #92
- **Difficulty**: Medium
- **Pattern**: Array Buffer / Value Replacement

---

## Algorithm

Extract node pointers into an array, reverse the sub-array from `left - 1` to `right - 1`, and rewire the `next` pointers.

---

## Code

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if (!head || left == right) return head;
        std::vector<ListNode*> nodes;
        for (ListNode* curr = head; curr; curr = curr->next) {
            nodes.push_back(curr);
        }

        std::reverse(nodes.begin() + left - 1, nodes.begin() + right);

        for (size_t i = 0; i < nodes.size() - 1; i++) {
            nodes[i]->next = nodes[i + 1];
        }
        nodes.back()->next = nullptr;
        return nodes[0];
    }
};
```

---

## Time & Space Complexity

- **Time Complexity**: $\mathcal{O}(N)$
- **Space Complexity**: $\mathcal{O}(N)$
