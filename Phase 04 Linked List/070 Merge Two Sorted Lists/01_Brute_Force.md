# Merge Two Sorted Lists

- **Problem Number**: 21
- **Platform**: LeetCode #21
- **Difficulty**: Easy
- **Pattern**: Array Extraction & Sorting

---

## Brute Force Intuition

Extract all node values from `list1` and `list2` into an array, sort the array, and construct a brand new linked list from the sorted values.

---

## Algorithm

1. Traverse `list1` and `list2`, appending `val` of each node into a vector `v`.
2. Sort vector `v` in non-decreasing order.
3. Construct a new linked list by instantiating new `ListNode` objects for each element in `v`.
4. Return head of the newly created list.

---

## Code

```cpp
#include <vector>
#include <algorithm>

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        std::vector<int> v;
        
        while (list1 != nullptr) {
            v.push_back(list1->val);
            list1 = list1->next;
        }
        while (list2 != nullptr) {
            v.push_back(list2->val);
            list2 = list2->next;
        }
        
        if (v.empty()) return nullptr;
        
        std::sort(v.begin(), v.end());
        
        ListNode* dummy = new ListNode(0);
        ListNode* curr = dummy;
        for (int val : v) {
            curr->next = new ListNode(val);
            curr = curr->next;
        }
        
        return dummy->next;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}((N + M) \log(N + M))$
  - Extracting nodes takes $\mathcal{O}(N + M)$; sorting vector takes $\mathcal{O}((N + M) \log(N + M))$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N + M)$
  - Vector and new linked list nodes require $\mathcal{O}(N + M)$ auxiliary memory.

---

## Why This Approach Is Not Optimal

Sorting takes $\mathcal{O}((N + M) \log(N + M))$ time and ignores the fact that **both input lists are already sorted**. Using **Dummy Head Two-Pointer Splice**, we can merge the existing nodes in-place in linear $\mathcal{O}(N + M)$ time with $\mathcal{O}(1)$ space.
