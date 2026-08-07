# Reorder List

- **Problem Number**: 143
- **Platform**: LeetCode #143
- **Difficulty**: Medium
- **Pattern**: Vector Pointer Storage

---

## Brute Force Intuition

Traverse the linked list and store pointers to all nodes in a `std::vector<ListNode*> nodes`. Use two pointers `left = 0` and `right = n - 1` on the vector to interleave node connections from opposite ends.

---

## Algorithm

1. Store all node pointers into `vector<ListNode*> nodes`.
2. `left = 0`, `right = nodes.size() - 1`.
3. While `left < right`:
   a. `nodes[left]->next = nodes[right]`.
   b. `left++`.
   c. If `left == right` break.
   d. `nodes[right]->next = nodes[left]`.
   e. `right--`.
4. `nodes[left]->next = nullptr`.

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
public:
    void reorderList(ListNode* head) {
        if (head == nullptr || head->next == nullptr) return;
        
        std::vector<ListNode*> nodes;
        ListNode* curr = head;
        while (curr != nullptr) {
            nodes.push_back(curr);
            curr = curr->next;
        }
        
        int left = 0;
        int right = nodes.size() - 1;
        
        while (left < right) {
            nodes[left]->next = nodes[right];
            left++;
            if (left == right) break;
            nodes[right]->next = nodes[left];
            right--;
        }
        
        nodes[left]->next = nullptr;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Single pass to populate vector and single pass to reconnect pointers.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Vector stores $N$ node pointers.

---

## Why This Approach Is Not Optimal

Using a vector requires $\mathcal{O}(N)$ auxiliary memory. By combining three fundamental linked list operations (**Find Middle**, **Reverse Second Half**, and **Merge Interleave**), we can reorder the list in-place in $\mathcal{O}(N)$ time with $\mathcal{O}(1)$ space.
