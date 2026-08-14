# Merge k Sorted Lists

- **Problem Number**: 23
- **Platform**: LeetCode #23
- **Difficulty**: Hard
- **Pattern**: Sequential 2-List Merge

---

## Brute Force Intuition

Sequentially merge `lists` one by one:
1. Start with `merged_list = lists[0]`.
2. Loop `i` from `1` to `k - 1`:
   - `merged_list = mergeTwoLists(merged_list, lists[i])`.

---

## Algorithm

1. If `lists` is empty, return `nullptr`.
2. `merged = lists[0]`.
3. Loop `i` from `1` to `k - 1`:
   - `merged = mergeTwoLists(merged, lists[i])`.
4. Return `merged`.

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
private:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode dummy(0);
        ListNode* tail = &dummy;
        while (l1 && l2) {
            if (l1->val <= l2->val) {
                tail->next = l1;
                l1 = l1->next;
            } else {
                tail->next = l2;
                l2 = l2->next;
            }
            tail = tail->next;
        }
        tail->next = l1 ? l1 : l2;
        return dummy.next;
    }
public:
    ListNode* mergeKLists(const std::vector<ListNode*>& lists) {
        if (lists.empty()) return nullptr;
        
        ListNode* merged = lists[0];
        for (size_t i = 1; i < lists.size(); ++i) {
            merged = mergeTwoLists(merged, lists[i]);
        }
        
        return merged;
    }
};
----------------------------------------------------------------------------------------------------------------
Another solution

class Solution {

private:

    ListNode* mergeTwoSortedLists(ListNode* l1, ListNode* l2) {

        if (!l1) return l2;
        if (!l2) return l1;

        if (l1->val <= l2->val) {
            l1->next = mergeTwoSortedLists(l1->next, l2);
            return l1;
        }
        else {
            l2->next = mergeTwoSortedLists(l1, l2->next);
            return l2;
        }
    }

    ListNode* partitionAndMerge(
        int start,
        int end,
        vector<ListNode*>& lists
    ) {

        if (start > end) {
            return NULL;
        }

        if (start == end) {
            return lists[start];
        }

        int mid = start + (end - start) / 2;

        ListNode* L1 = partitionAndMerge(start, mid, lists);
        ListNode* L2 = partitionAndMerge(mid + 1, end, lists);

        return mergeTwoSortedLists(L1, L2);
    }

public:

    ListNode* mergeKLists(vector<ListNode*>& lists) {

        int k = lists.size();

        if (k == 0) {
            return NULL;
        }

        return partitionAndMerge(0, k - 1, lists);
    }
};

```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(K \times N)$
  - Where $N$ is the total number of nodes across all lists.
  - Merging list 1 ($N/K$ nodes) with list 2 ($N/K$ nodes), then with list 3 ($2N/K$ nodes)... sums to $\mathcal{O}(K \times N)$ operations.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$ auxiliary space.

---

## Why This Approach Is Not Optimal

Sequential merging takes $\mathcal{O}(K \times N)$ time. Using **Min-Heap (Priority Queue)** or **Divide and Conquer**, we can merge all $K$ sorted lists in $\mathcal{O}(N \log K)$ time.
