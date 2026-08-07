# Rotate List

## Pattern Used

- **Pattern**: **Circular Ring Closing & Break Cut**
- **Concept**:
  1. Compute total length $N$ and find the tail node `tail`.
  2. Connect `tail->next = head` to form a **circular linked list**.
  3. Calculate effective rotation $k = k \pmod N$.
  4. The new tail node is located at position $(N - k)$ from the original head.
  5. Traverse $N - k$ steps to reach `new_tail`, record `new_head = new_tail->next`, and break the ring `new_tail->next = nullptr`.

---

## Observation

1. Rotating a list right by $k$ places means the last $k$ nodes become the new prefix of the list!
2. The node at position $N - k$ from the start becomes the **new tail**, and the node at position $N - k + 1$ becomes the **new head**.
3. Connecting `tail->next = head` temporarily simplifies finding and cutting the new tail!

---

## Intuition

Form a circular ring by linking the last node to the first node. Then walk $N - k$ steps along the ring and snip the link to open a new linear list.

---

## Algorithm

1. If `head == nullptr || head->next == nullptr || k == 0`, return `head`.
2. Compute list length $N$ and locate tail pointer `tail`:
   - `n = 1`, `tail = head`.
   - While `tail->next != nullptr`: `n++`, `tail = tail->next`.
3. `k = k % n`. If `k == 0`, return `head`.
4. Connect tail to head: `tail->next = head` (circular ring).
5. `steps_to_new_tail = n - k`.
6. `new_tail = head`.
7. For `i` from `1` to `steps_to_new_tail - 1`:
   - `new_tail = new_tail->next`.
8. `new_head = new_tail->next`.
9. Break ring: `new_tail->next = nullptr`.
10. Return `new_head`.

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
    ListNode* rotateRight(ListNode* head, int k) {
        if (head == nullptr || head->next == nullptr || k == 0) return head;
        
        // Step 1: Compute length and locate tail
        int n = 1;
        ListNode* tail = head;
        while (tail->next != nullptr) {
            n++;
            tail = tail->next;
        }
        
        // Step 2: Modulo k with length n
        k = k % n;
        if (k == 0) return head;
        
        // Step 3: Form circular ring
        tail->next = head;
        
        // Step 4: Find new tail (N - k steps from head)
        int steps_to_new_tail = n - k;
        ListNode* new_tail = head;
        for (int i = 1; i < steps_to_new_tail; ++i) {
            new_tail = new_tail->next;
        }
        
        // Step 5: Break ring and set new head
        ListNode* new_head = new_tail->next;
        new_tail->next = nullptr;
        
        return new_head;
    }
};
```

---

## Dry Run

### Input
- `head = [1 -> 2 -> 3 -> 4 -> 5]`, `k = 2`

### Execution Trace

1. `n = 5`, `tail` points to node `5`.
2. `k = 2 % 5 = 2`.
3. Circular Ring: `5->next = 1` (`1 -> 2 -> 3 -> 4 -> 5 -> 1`).
4. `steps_to_new_tail = 5 - 2 = 3`.
5. Walk 3 steps from head `1`:
   - Step 1: `1`
   - Step 2: `2`
   - Step 3: `3` (`new_tail` = Node `3`).
6. `new_head = 3->next` (Node `4`).
7. `3->next = nullptr`.

### Result
- Output List: `4 -> 5 -> 1 -> 2 -> 3`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Pass 1 computes length $N$; Pass 2 traverses $N - k$ steps. Total operations $\le 2N$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space.

---

## Why This is Optimal

- Rotates list in linear $\mathcal{O}(N)$ time regardless of $K$ magnitude ($K \le 2 \times 10^9$).
- Uses zero extra memory ($\mathcal{O}(1)$ space).

---

## Common Mistakes

1. **Not Applying `k = k % n`**: Attempting to loop $K$ times when $K = 2 \times 10^9$, causing TLE.
2. **Incorrect Off-by-One Step Count**: Walking $N - k + 1$ steps instead of $N - k$ steps to locate `new_tail`.
