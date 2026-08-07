# Reverse Nodes in k-Group

- **Problem Number**: 25
- **Platform**: LeetCode #25
- **Difficulty**: Hard
- **Pattern**: Vector Partition Reversal

---

## Brute Force Intuition

Traverse the linked list and store pointers to all nodes in a `std::vector<ListNode*> nodes`. Process the vector in chunks of size $k$:
- Reverse each group of size $k$ inside the vector.
- Leave the final remainder group ($< k$ nodes) unchanged.
- Re-stitch node `next` pointers based on the modified vector order.

---

## Algorithm

1. Store all node pointers in `vector<ListNode*> nodes`.
2. `n = nodes.size()`.
3. For `i` from `0` to `n - 1` with step `k`:
   - If `i + k <= n`: reverse sub-range `nodes.begin() + i` to `nodes.begin() + i + k`.
4. Reconnect pointers:
   - For `i` from `0` to `n - 2`: `nodes[i]->next = nodes[i + 1]`.
   - `nodes[n - 1]->next = nullptr`.
5. Return `nodes[0]`.

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
    ListNode* reverseKGroup(ListNode* head, int k) {
        if (head == nullptr || k == 1) return head;
        
        std::vector<ListNode*> nodes;
        ListNode* curr = head;
        while (curr != nullptr) {
            nodes.push_back(curr);
            curr = curr->next;
        }
        
        int n = nodes.size();
        for (int i = 0; i + k <= n; i += k) {
            std::reverse(nodes.begin() + i, nodes.begin() + i + k);
        }
        
        for (int i = 0; i < n - 1; ++i) {
            nodes[i]->next = nodes[i + 1];
        }
        nodes[n - 1]->next = nullptr;
        
        return nodes[0];
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Vector extraction, chunk reversal, and pointer re-stitching take $\mathcal{O}(N)$ time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Stores $N$ node pointers in vector memory.

---

## Why This Approach Is Not Optimal

Using a vector requires $\mathcal{O}(N)$ auxiliary space. The problem follow-up explicitly asks for an **in-place $\mathcal{O}(1)$ space solution**. By using **Iterative Subsegment Pointer Reversal**, we can reverse nodes in $K$-groups in-place.
