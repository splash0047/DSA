# Remove Duplicates from Sorted List - Optimal Approach (In-Place 1-Pass)

- **Problem Number**: 83
- **Platform**: LeetCode #83
- **Difficulty**: Easy
- **Pattern**: Pointer Rewiring ($\mathcal{O}(1)$ Space)

---

## Optimal Intuition

Because the list is already sorted, duplicate elements are strictly adjacent. We can traverse with pointer `curr`: if `curr->val == curr->next->val`, skip `curr->next` by updating `curr->next = curr->next->next`.

---

## Code

```cpp
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* curr = head;
        while (curr && curr->next) {
            if (curr->val == curr->next->val) {
                ListNode* temp = curr->next;
                curr->next = curr->next->next;
                delete temp; // Avoid memory leak in C++
            } else {
                curr = curr->next;
            }
        }
        return head;
    }
};
```

---

## Time & Space Complexity

- **Time Complexity**: $\mathcal{O}(N)$
- **Space Complexity**: strictly $\mathcal{O}(1)$
