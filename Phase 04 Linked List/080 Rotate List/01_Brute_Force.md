# Rotate List

- **Problem Number**: 61
- **Platform**: LeetCode #61
- **Difficulty**: Medium
- **Pattern**: Step-by-Step Single Rotations

---

## Brute Force Intuition

Rotate the linked list rightward by 1 position $k$ times. In each single rotation:
- Find the second-to-last node `prev` and the last node `tail`.
- Disconnect `prev->next = nullptr`.
- Attach `tail->next = head`.
- Update `head = tail`.

---

## Algorithm

1. If `head == nullptr || head->next == nullptr || k == 0`, return `head`.
2. Compute length `N`. Set `k = k % N`.
3. Repeat `k` times:
   a. Traverse to second-to-last node `prev`.
   b. `tail = prev->next`.
   c. `prev->next = nullptr`.
   d. `tail->next = head`.
   e. `head = tail`.
4. Return `head`.

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
    ListNode* rotateRight(ListNode* head, int k) {
        if (head == nullptr || head->next == nullptr || k == 0) return head;
        
        int n = 0;
        ListNode* curr = head;
        while (curr != nullptr) {
            n++;
            curr = curr->next;
        }
        
        k = k % n;
        if (k == 0) return head;
        
        for (int i = 0; i < k; ++i) {
            ListNode* prev = head;
            while (prev->next->next != nullptr) {
                prev = prev->next;
            }
            ListNode* tail = prev->next;
            prev->next = nullptr;
            tail->next = head;
            head = tail;
        }
        
        return head;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(K \times N)$
  - Each of the $K$ single-step rotations traverses $N$ nodes.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space.

---

## Why This Approach Is Not Optimal

Performing step-by-step single rotations takes $\mathcal{O}(K \times N)$ time. By using **Circular Ring Closing & Break Cut**, we can rotate the entire list in a single pass in $\mathcal{O}(N)$ time.
