# Reverse Linked List

- **Problem Number**: 206
- **Platform**: LeetCode #206
- **Difficulty**: Easy
- **Pattern**: Stack / Auxiliary Array

---

## Brute Force Intuition

Traverse the linked list and push all node values into a stack (or vector). Then traverse the linked list a second time and overwrite each node's value by popping elements from the stack (reversing values in-place).

---

## Algorithm

1. If `head == nullptr`, return `head`.
2. Traverse list from `head` and push `node->val` onto a stack `s`.
3. Reset pointer `curr = head`.
4. While `curr != nullptr`:
   a. `curr->val = s.top()`.
   b. `s.pop()`.
   c. `curr = curr->next`.
5. Return `head`.

---

## Code

```cpp
#include <stack>

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        std::stack<int> s;
        ListNode* curr = head;
        
        while (curr != nullptr) {
            s.push(curr->val);
            curr = curr->next;
        }
        
        curr = head;
        while (curr != nullptr) {
            curr->val = s.top();
            s.pop();
            curr = curr->next;
        }
        
        return head;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Two passes over $N$ nodes.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Stores $N$ node values in stack memory.

---

## Why This Approach Is Not Optimal

Using an auxiliary stack requires $\mathcal{O}(N)$ extra space and only swaps node values rather than reversing node pointers. By using **3-Pointer Iterative Reversal**, we can reverse the actual pointer links in-place with $\mathcal{O}(1)$ space.
