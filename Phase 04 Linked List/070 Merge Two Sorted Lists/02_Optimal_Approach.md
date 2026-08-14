# Merge Two Sorted Lists

## Pattern Used

- **Pattern**: **Dummy Head Node Pointer Splicing (Two-Pointer In-Place)**
- **Concept**: Create a sentinel `dummy` node. Maintain a tail pointer `tail` pointing to `dummy`. Compare current nodes of `list1` and `list2`, linking `tail->next` to the smaller node and advancing the chosen list pointer.

---

## Observation

1. Both input lists are pre-sorted in non-decreasing order.
2. Using a `dummy` node eliminates special-case logic for initializing the head of the merged list.
3. When one list becomes empty (`nullptr`), directly attach the remaining non-empty list to `tail->next` in $\mathcal{O}(1)$ time.

---

## Intuition

Zip the two sorted lists together by sequentially comparing the front node of each list and stitching `next` pointers in-place.

---

## Algorithm

1. `dummy = ListNode(0)`, `tail = &dummy`.
2. While `list1 != nullptr` and `list2 != nullptr`:
   a. If `list1->val <= list2->val`:
      - `tail->next = list1`.
      - `list1 = list1->next`.
   b. Else:
      - `tail->next = list2`.
      - `list2 = list2->next`.
   c. `tail = tail->next`.
3. If `list1 != nullptr`: `tail->next = list1`.
4. If `list2 != nullptr`: `tail->next = list2`.
5. Return `dummy.next`.

---

## Clean C++17 Solution

```cpp
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

        ListNode dummy(0);
        ListNode* temp = &dummy;

        while (list1 != nullptr && list2 != nullptr) {

            if (list1->val <= list2->val) {
                temp->next = list1;
                list1 = list1->next;
            }
            else {
                temp->next = list2;
                list2 = list2->next;
            }

            temp = temp->next;
        }

        if (list1 != nullptr) {
            temp->next = list1;
        }
        else {
            temp->next = list2;
        }

        return dummy.next;
    }
};
```

---

## Dry Run

### Input
- `list1 = [1 -> 2 -> 4]`, `list2 = [1 -> 3 -> 4]`

### Execution Trace

| Step | `list1` head val | `list2` head val | Comparison | `tail->next` Attached Node | `tail` moves to |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Init | `1` | `1` | `1 <= 1` | Node `1` (from list1) | Node `1` (list1) |
| 1 | `2` | `1` | `2 > 1` | Node `1` (from list2) | Node `1` (list2) |
| 2 | `2` | `3` | `2 <= 3` | Node `2` (from list1) | Node `2` (list1) |
| 3 | `4` | `3` | `4 > 3` | Node `3` (from list2) | Node `3` (list2) |
| 4 | `4` | `4` | `4 <= 4` | Node `4` (from list1) | Node `4` (list1) |
| End | `nullptr` | `4` | `list1 == nullptr` | Attach remaining `list2` (`[4]`) | - |

### Result
- Merged List: `1 -> 1 -> 2 -> 3 -> 4 -> 4`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N + M)$
  - At each step, 1 node is attached. Total operations equal $N + M$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Reuses existing node pointers in-place with zero extra memory allocation.

---

## Why This is Optimal

- Merges pre-sorted lists in linear $\mathcal{O}(N + M)$ time.
- Uses zero extra node memory ($\mathcal{O}(1)$ space).

---

## Common Mistakes

1. **Allocating New Memory Nodes**: Instantiating `new ListNode(val)` instead of rewiring existing node pointers `tail->next = list1`.
2. **Missing Tail Remainder Attachment**: Loop ends when one list runs out; forgetting to attach `tail->next = (list1 != nullptr) ? list1 : list2`.
