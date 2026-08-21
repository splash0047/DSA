# Remove Duplicates from Sorted List - Brute Force

- **Problem Number**: 83
- **Platform**: LeetCode #83
- **Difficulty**: Easy
- **Pattern**: Hash Set / Extra List Copy

---

## Algorithm

Store node values in an `unordered_set` or vector. Traverse and construct a new unique list.

---

## Code

```cpp
#include <unordered_set>

class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        std::unordered_set<int> seen;
        ListNode dummy(0);
        ListNode* tail = &dummy;

        for (ListNode* curr = head; curr != nullptr; curr = curr->next) {
            if (!seen.count(curr->val)) {
                seen.insert(curr->val);
                tail->next = new ListNode(curr->val);
                tail = tail->next;
            }
        }
        return dummy.next;
    }
};
```

---

## Time & Space Complexity

- **Time Complexity**: $\mathcal{O}(N)$
- **Space Complexity**: $\mathcal{O}(N)$
