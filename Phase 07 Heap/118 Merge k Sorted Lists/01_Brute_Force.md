# Merge k Sorted Lists

- **Problem Number**: 23
- **Platform**: LeetCode #23
- **Difficulty**: Hard
- **Pattern**: Extract All Values + Sort + Rebuild Linked List

---

## Brute Force Intuition

1. Traverse all $k$ linked lists and extract every node value into a vector `vector<int> vals`.
2. Sort the vector using `std::sort`.
3. Create a new linked list by constructing nodes for each sorted value in `vals`.

---

## Algorithm

1. Create `vector<int> vals`.
2. For each head node `list` in `lists`:
   - While `list != nullptr`:
     - `vals.push_back(list->val)`.
     - `list = list->next`.
3. `std::sort(vals.begin(), vals.end())`.
4. Create dummy node `dummy(0)` and `curr = &dummy`.
5. For each `val` in `vals`:
   - `curr->next = new ListNode(val)`.
   - `curr = curr->next`.
6. Return `dummy.next`.

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
    ListNode* mergeKLists(std::vector<ListNode*>& lists) {
        std::vector<int> vals;
        
        for (ListNode* head : lists) {
            while (head != nullptr) {
                vals.push_back(head->val);
                head = head->next;
            }
        }
        
        std::sort(vals.begin(), vals.end());
        
        ListNode dummy(0);
        ListNode* curr = &dummy;
        for (int val : vals) {
            curr->next = new ListNode(val);
            curr = curr->next;
        }
        
        return dummy.next;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N \log N)$
  - Where $N$ is total number of nodes across all $k$ lists.
  - Traversing lists takes $\mathcal{O}(N)$. Sorting takes $\mathcal{O}(N \log N)$. Rebuilding takes $\mathcal{O}(N)$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Vector `vals` and newly allocated nodes consume $\mathcal{O}(N)$ extra space.

---

## Why This Approach Is Not Optimal

This approach ignores the fact that each of the $k$ lists is **already sorted**. Using a **Min-Heap of size $k$** or **Divide-and-Conquer Merge Sort**, we can merge all lists in $\mathcal{O}(N \log k)$ time and $\mathcal{O}(1)$ extra auxiliary space (by reusing existing nodes)!
