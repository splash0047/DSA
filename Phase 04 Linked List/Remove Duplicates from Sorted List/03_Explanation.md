# Remove Duplicates from Sorted List - Deep Explanation

## Pointer Rewiring Logic
If `1 -> 1 -> 2`, `curr` at first `1` sees `curr->next->val == 1`.
It sets `curr->next = 2`, remaining at the first `1` to verify if subsequent nodes are also duplicates.
Once values differ, `curr = curr->next`.
