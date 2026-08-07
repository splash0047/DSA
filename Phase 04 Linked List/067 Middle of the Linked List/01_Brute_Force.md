# Middle of the Linked List

- **Problem Number**: 876
- **Platform**: LeetCode #876
- **Difficulty**: Easy
- **Pattern**: Two-Pass Length Counter

---

## Brute Force Intuition

Pass 1: Count the total number of nodes `N` in the linked list.
Pass 2: Traverse `N / 2` steps from `head` to reach the middle node.

---

## Algorithm

1. `count = 0`, `curr = head`.
2. While `curr != nullptr`:
   a. `count++`.
   b. `curr = curr->next`.
3. `target = count / 2`.
4. `curr = head`.
5. For `i` from `0` to `target - 1`:
   a. `curr = curr->next`.
6. Return `curr`.

---

## Code

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
    ListNode* middleNode(ListNode* head) {
        int count = 0;
        ListNode* curr = head;
        
        while (curr != nullptr) {
            count++;
            curr = curr->next;
        }
        
        int target = count / 2;
        curr = head;
        for (int i = 0; i < target; ++i) {
            curr = curr->next;
        }
        
        return curr;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Pass 1 counts $N$ nodes; Pass 2 traverses $N/2$ nodes. Total time: $1.5 N = \mathcal{O}(N)$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space.

---

## Why This Approach Is Not Optimal

While $\mathcal{O}(N)$ time, it requires **two full passes** over the linked list. Using **Floyd's Fast and Slow Pointer Algorithm**, we can find the middle node in a **single pass**.
