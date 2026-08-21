import os

BASE_DIR = r"c:\Users\Pinak chimurkar\DSA\Phase 04 Linked List"

data = {
    "066 Reverse Linked List": """# 04 Interview Follow-ups & System Variations: Reverse Linked List

The problem reverses a singly linked list. The optimal iterative approach uses 3 pointers (`prev`, `curr`, `next`) running in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this is the launchpad for questions on stack overflow hazards in recursion, sublist reversals, doubly linked list variants, and cache memory layout.

---

## 1. Iterative vs. Recursive Reversal

| Dimension | Iterative (3-Pointer) | Recursive |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| **Space Complexity** | $\mathcal{O}(1)$ strictly | $\mathcal{O}(N)$ Call Stack Frames |
| **Stack Overflow Risk**| Zero risk (processes $10^9$ nodes) | **Crashes** for $N > 10^4$ (OS stack limit) |
| **Production Use** | **Industry Standard** | Avoid in systems code |

---

## 2. Generalization: Reverse a Sublist Between Positions $L$ and $R$ (LeetCode #92)

### 💡 1-Pass Head-Insertion Technique
- Navigate to node at position $L - 1$ (`pre`).
- Set `curr = pre->next`.
- For $R - L$ iterations:
  - Detach `next_node = curr->next`.
  - Splice `next_node` directly after `pre`:
    ```cpp
    curr->next = next_node->next;
    next_node->next = pre->next;
    pre->next = next_node;
    ```
- **Time Complexity**: $\mathcal{O}(N)$ 1-pass, **Space Complexity**: $\mathcal{O}(1)$.

---

## 3. Hardware Architecture: Linked List Cache Misses vs. Arrays

### 🛑 The Memory Fragmentation Reality
- Array elements are contiguous in physical RAM; hardware prefetchers load full 64-byte cache lines.
- Linked list nodes are allocated on the heap at arbitrary memory addresses.
- Every `curr = curr->next` pointer chase triggers a CPU L1/L2 cache miss.
- **System Insight**: In high-performance software, contiguous array-backed lists (or Unrolled Linked Lists) are preferred over classic pointer-based linked lists.

---

## Summary Matrix: Trade-offs at a Glance

| Variation | Technique | Time | Space |
| :--- | :--- | :--- | :--- |
| **Full Reverse** | Iterative 3-Pointer (`prev`, `curr`, `next`) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Sublist ($L \dots R$)** | 1-Pass Splice Head-Insertion | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Doubly Linked List** | Swap `curr->prev` and `curr->next` | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
""",

    "067 Middle of the Linked List": """# 04 Interview Follow-ups & System Variations: Middle of the Linked List

The problem finds the middle node of a singly linked list. The optimal approach uses **Fast and Slow Pointers** (`slow` advances 1 step, `fast` advances 2 steps) in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem tests even-length middle conventions (first vs. second middle) and deleting middle nodes in $\mathcal{O}(1)$ space.

---

## 1. Even Length Ambiguity: First Middle vs. Second Middle

### 💡 Pointer Termination Invariants
1. **Return Second Middle (LeetCode #876)**:
   - Loop condition: `while (fast != nullptr && fast->next != nullptr)`
   - For `[1, 2, 3, 4]`, returns node `3`.
2. **Return First Middle (Crucial for Merge Sort / Palindrome splitting)**:
   - Loop condition: `while (fast->next != nullptr && fast->next->next != nullptr)`
   - For `[1, 2, 3, 4]`, returns node `2`.
   - Leaves the left half `[1, 2]` cleanly separated from the right half `[3, 4]`.

---

## 2. Follow-up: Delete the Middle Node (LeetCode #2095)

### 💡 Tracking Previous Pointer
- Initialize `dummy(0, head)`, `slow = &dummy`, `fast = head`.
- Advance `slow` by 1 and `fast` by 2 until `fast == nullptr || fast->next == nullptr`.
- At termination, `slow` points **immediately before the middle node**.
- Delete: `slow->next = slow->next->next`.

---

## Summary Matrix: Trade-offs at a Glance

| Goal | Loop Condition | Even Length Node (e.g., 4 nodes) |
| :--- | :--- | :--- |
| **Second Middle** | `fast && fast->next` | Node 3 (2nd middle) |
| **First Middle** | `fast->next && fast->next->next` | Node 2 (1st middle) |
| **Delete Middle** | `slow` starts at dummy head | Directly unlinks middle node |
""",

    "068 Linked List Cycle": """# 04 Interview Follow-ups & System Variations: Linked List Cycle

The problem detects whether a linked list contains a cycle. Floyd's **Tortoise and Hare Algorithm** (`slow` moves 1 step, `fast` moves 2 steps) achieves $\mathcal{O}(N)$ time and strictly $\mathcal{O}(1)$ space.

In technical interviews, interviewers test mathematical convergence proofs, Hash Set trade-offs, and non-destructive node marking.

---

## 1. Mathematical Proof: Why `fast` is Guaranteed to Catch `slow`

### 💡 The Relative Speed Invariant
- Let the cycle length be $C$.
- Once both `slow` and `fast` are inside the cycle, let the distance between them (measuring clockwise from `slow` to `fast`) be $d$.
- In each step:
  - `slow` moves 1 step clockwise: $+1$.
  - `fast` moves 2 steps clockwise: $+2$.
  - Relative distance increases by $+1$ each step: $(d + 1) \pmod C$.
- Therefore, the remaining gap $C - (d + 1)$ decreases by strictly $1$ on every iteration.
- Because the gap decreases by 1 integer step each time, `fast` cannot "hop over" `slow` without landing on the exact same node. The gap reaches 0 in at most $C$ steps.

---

## 2. Floyd's Algorithm vs. Hash Set vs. Node Modification

| Method | Time | Space | Modifies List? |
| :--- | :--- | :--- | :--- |
| **Floyd's Tortoise & Hare** | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | **No (Safe & Optimal)** |
| **Hash Set of Addresses** | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ | No |
| **Node Value Sentinel Tag** | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | Destructive (Corrupts data) |
| **Reversing Pointers Visited**| $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | Destructive |

---

## Summary Matrix: Trade-offs at a Glance

| Parameter | Value |
| :--- | :--- |
| **Time Complexity** | $\mathcal{O}(N + C)$ where $N$ is tail length and $C$ is cycle size |
| **Space Complexity** | Strictly $\mathcal{O}(1)$ |
| **Cycle Entrance Found?** | No (Only detects boolean presence; use Cycle II for node) |
""",

    "069 Linked List Cycle II": """# 04 Interview Follow-ups & System Variations: Linked List Cycle II

The problem finds the exact node where a cycle begins in a singly linked list. Floyd's Cycle Algorithm combined with a second phase of pointers moving from `head` and `meeting_point` finds the entrance in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this is the standard mathematical derivation test in pointer algorithms.

---

## 1. Mathematical Derivation of Cycle Entrance Equality

### 💡 The Distance Equation
- Let:
  - $L$ = distance from `head` to cycle entrance.
  - $C$ = circumference (length) of the cycle.
  - $x$ = distance from cycle entrance to meeting point inside the cycle.
- Total distance traveled by `slow` when they meet:
  $$D_{\text{slow}} = L + x$$
- Total distance traveled by `fast` when they meet (with $k$ full cycle loops):
  $$D_{\text{fast}} = L + k \cdot C + x$$
- Because `fast` travels at twice the speed of `slow`:
  $$D_{\text{fast}} = 2 \cdot D_{\text{slow}}$$
  $$L + k \cdot C + x = 2(L + x)$$
  $$L + k \cdot C + x = 2L + 2x$$
  $$L = k \cdot C - x = (k - 1) \cdot C + (C - x)$$
- **Conclusion**: The distance from `head` to the cycle entrance ($L$) is mathematically identical to the distance from the `meeting_point` to the cycle entrance ($C - x$) plus $(k - 1)$ full cycle loops.
- **Algorithm Phase 2**: Reset `p1 = head`, keep `p2 = meeting_point`. Advance both 1 step at a time; they will collide precisely at the cycle entrance!

---

## 2. Calculating the Exact Length of the Cycle $C$

### 💡 Simple Pointer Loop
- After finding `meeting_point`:
  - Keep `curr = meeting_point->next`, `length = 1`.
  - While `curr != meeting_point`: `curr = curr->next; length++;`.
- Returns exact number of nodes in the cycle in $\mathcal{O}(C)$ time.

---

## Summary Matrix: Trade-offs at a Glance

| Phase | Purpose | Pointers | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Phase 1** | Detect collision | `slow` (1x), `fast` (2x) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Phase 2** | Find entrance | `head` (1x), `meeting` (1x)| $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Cycle Length** | Count nodes in cycle | Advance until return to meeting | $\mathcal{O}(C)$ | $\mathcal{O}(1)$ |
""",

    "070 Merge Two Sorted Lists": """# 04 Interview Follow-ups & System Variations: Merge Two Sorted Lists

The problem merges two sorted singly linked lists into one sorted list. The optimal approach uses a **Dummy Head Node** and iterative pointer splicing in $\mathcal{O}(M + N)$ time and $\mathcal{O}(1)$ auxiliary space.

In technical interviews, this problem is compared with recursive merges, array merges, and $K$-list extensions.

---

## 1. Why Iterative Pointer Splicing is Superior to Allocating New Nodes

### 🛑 Zero Memory Allocation Invariant
- Naive solutions create new `new ListNode(val)` nodes for the merged list.
- **Optimal Splicing**: Simply rewire existing `next` pointers from `list1` and `list2`.
- Zero heap allocation overhead; zero memory leaks.

---

## 2. Iterative vs. Recursive Merge

```cpp
// Iterative with Dummy Node: O(1) Space
ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
    ListNode dummy(0);
    ListNode* tail = &dummy;
    while (l1 && l2) {
        if (l1->val <= l2->val) { tail->next = l1; l1 = l1->next; }
        else { tail->next = l2; l2 = l2->next; }
        tail = tail->next;
    }
    tail->next = l1 ? l1 : l2;
    return dummy.next;
}
```
- **Recursive Space**: $\mathcal{O}(M + N)$ stack frames $\implies$ risky for large lists.

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Time | Space | Memory Allocation |
| :--- | :--- | :--- | :--- |
| **Iterative + Dummy Node** | $\mathcal{O}(M+N)$ | $\mathcal{O}(1)$ | **0 allocations (Rewires pointers)** |
| **Recursive** | $\mathcal{O}(M+N)$ | $\mathcal{O}(M+N)$ | Call stack allocations |
""",

    "071 Merge k Sorted Lists": """# 04 Interview Follow-ups & System Variations: Merge k Sorted Lists

The problem merges $K$ sorted linked lists of total $N$ nodes. Optimal solutions include Min-Heap ($\mathcal{O}(N \log K)$ time, $\mathcal{O}(K)$ space) and Divide & Conquer Tournament Merge ($\mathcal{O}(N \log K)$ time, $\mathcal{O}(1)$ space).

In technical interviews, this is the prime template for external distributed merges, multi-way streaming, and priority queue tuning.

---

## 1. Min-Heap vs. Divide & Conquer Tournament Merge

| Metric | Min-Heap Priority Queue | Divide & Conquer (Pairwise) |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(N \log K)$ | $\mathcal{O}(N \log K)$ |
| **Space Complexity** | $\mathcal{O}(K)$ Heap memory | $\mathcal{O}(1)$ iterative / $\mathcal{O}(\log K)$ stack |
| **Streaming Feasibility**| **Optimal for live streams** | Requires all lists upfront |
| **Hardware Cache** | Pointer heap hopping | Sequential linked list traversal |

---

## 2. Distributed Scale: Merging $K = 1,000$ Files from Disk / Cloud Storage

### 💡 External $K$-Way Merge Engine
- In database external sort (e.g., PostgreSQL / Apache Spark):
  - Open 1 stream buffer per file in RAM.
  - Maintain an in-memory Min-Heap of size $K$.
  - Pop smallest record, stream to output file, fetch next record from the corresponding stream buffer.
  - When a buffer empties, read the next 64KB block from disk.

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Space Model | Best Used When |
| :--- | :--- | :--- |
| **Min-Heap (size $K$)** | $\mathcal{O}(K)$ | Dynamic real-time streams |
| **Divide & Conquer** | $\mathcal{O}(1)$ auxiliary | In-memory linked lists |
| **External $K$-Way Merge**| $\mathcal{O}(K \times \text{Buffer})$ | Multi-gigabyte disk files |
""",

    "072 Remove Nth Node From End of List": """# 04 Interview Follow-ups & System Variations: Remove Nth Node From End of List

The problem deletes the $N$-th node from the end of a linked list in a single pass using two pointers separated by $N$ steps and a dummy head in $\mathcal{O}(L)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem tests boundary dummy invariants, manual memory deallocation, and concurrent deletions.

---

## 1. Single-Pass Pointer Separation Invariant

```cpp
ListNode* removeNthFromEnd(ListNode* head, int n) {
    ListNode dummy(0, head);
    ListNode* fast = &dummy;
    ListNode* slow = &dummy;
    
    for (int i = 0; i <= n; i++) {
        fast = fast->next;
    }
    while (fast != nullptr) {
        fast = fast->next;
        slow = slow->next;
    }
    ListNode* to_delete = slow->next;
    slow->next = slow->next->next;
    delete to_delete; // Free memory in C++
    return dummy.next;
}
```

---

## Summary Matrix: Trade-offs at a Glance

| Scenario | Strategy | Time | Space |
| :--- | :--- | :--- | :--- |
| **Delete Head Node** | Handled by Dummy Head | $\mathcal{O}(L)$ | $\mathcal{O}(1)$ |
| **C++ Heap Deallocation** | Explicit `delete` | $\mathcal{O}(L)$ | $\mathcal{O}(1)$ |
""",

    "073 Reorder List": """# 04 Interview Follow-ups & System Variations: Reorder List

The problem reorders a singly linked list from $L_0 \to L_1 \to \dots \to L_{n-1} \to L_n$ into $L_0 \to L_n \to L_1 \to L_{n-1} \to L_2 \dots$ in-place. The optimal approach uses a 3-step pipeline in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this is the ultimate composite linked list problem, combining middle-finding, list reversal, and two-way list interleaving.

---

## 1. The 3-Step Pipeline ($\mathcal{O}(N)$ Time, $\mathcal{O}(1)$ Space)

### 💡 Step-by-Step Architecture
1. **Find First Middle**:
   - `while (fast->next && fast->next->next)`
   - Disconnect halves: `ListNode* second = slow->next; slow->next = nullptr;`.
2. **Reverse the Second Half**:
   - In-place reversal of `second` to produce reversed list `l2`.
3. **Interleave / Merge Alternate Nodes**:
   ```cpp
   ListNode* l1 = head;
   while (l2) {
       ListNode* next1 = l1->next;
       ListNode* next2 = l2->next;
       
       l1->next = l2;
       l2->next = next1;
       
       l1 = next1;
       l2 = next2;
   }
   ```

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Space Model | Time | Extra Memory |
| :--- | :--- | :--- | :--- |
| **Array of Pointers** | Buffer all nodes | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ extra space |
| **3-Step In-Place Splicing**| Pure pointer rewiring | $\mathcal{O}(N)$ | strictly $\mathcal{O}(1)$ |
""",

    "074 Intersection of Two Linked Lists": """# 04 Interview Follow-ups & System Variations: Intersection of Two Linked Lists

The problem finds the node where two singly linked lists intersect. The optimal two-pointer approach switches heads (`pA = (pA == nullptr) ? headB : pA->next`) in $\mathcal{O}(M + N)$ time and strictly $\mathcal{O}(1)$ space.

In technical interviews, this problem tests path length normalization proofs and intersection scenarios when cycles exist.

---

## 1. Mathematical Proof of the Head-Switch Traversal

### 💡 The Commutative Distance Invariant
- Let:
  - $a$ = length of non-shared prefix of List A.
  - $b$ = length of non-shared prefix of List B.
  - $c$ = length of shared intersection tail.
- Pointer A traverses: $a + c + b$.
- Pointer B traverses: $b + c + a$.
- Since $a + c + b = b + c + a$, both pointers traverse the exact same total distance!
- If the lists intersect, they will collide at the intersection node on the second pass.
- If the lists do not intersect ($c = 0$), both reach `nullptr` simultaneously ($a + b = b + a$) and terminate safely.

---

## 2. What if the Linked Lists May Contain CYCLES?

### 💡 3 Cycle Topology Scenarios
1. **Neither list has a cycle**: Standard intersection algorithm applies.
2. **Only one list has a cycle**: Mathematical impossibility for intersection; return `nullptr`.
3. **Both lists have cycles**:
   - Case 3A (Intersect before cycle): Intersection entrance found before cycle entry.
   - Case 3B (Intersect at cycle entrance / inside cycle): Pointers traverse the shared cycle; both loop entries are valid intersection points.
   - Case 3C (Disjoint cycles): Lists do not share the cycle; return `nullptr`.

---

## Summary Matrix: Trade-offs at a Glance

| Topology | Approach | Time | Space |
| :--- | :--- | :--- | :--- |
| **Acyclic Lists** | Head-switch Two Pointers | $\mathcal{O}(M+N)$ | $\mathcal{O}(1)$ |
| **Acyclic Lists (Length Diff)**| Compute lengths $\Delta = |M - N|$ | $\mathcal{O}(M+N)$ | $\mathcal{O}(1)$ |
| **Cyclic Lists** | Floyd's Cycle II + Topology Case Check | $\mathcal{O}(M+N)$ | $\mathcal{O}(1)$ |
""",

    "075 Palindrome Linked List": """# 04 Interview Follow-ups & System Variations: Palindrome Linked List

The problem determines if a singly linked list is a palindrome. The optimal in-place solution finds the middle, reverses the second half, compares in lockstep, and restores the list in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem is used to test safe in-place restoration and rolling hashes for read-only streams.

---

## 1. Clean 4-Step In-Place Implementation with List Restoration

```cpp
bool isPalindrome(ListNode* head) {
    if (!head || !head->next) return true;
    
    // 1. Find first middle
    ListNode *slow = head, *fast = head;
    while (fast->next && fast->next->next) {
        slow = slow->next;
        fast = fast->next->next;
    }
    
    // 2. Reverse second half
    ListNode *prev = nullptr, *curr = slow->next;
    while (curr) {
        ListNode* next_node = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next_node;
    }
    
    // 3. Compare first and second half
    ListNode *p1 = head, *p2 = prev;
    bool is_pal = true;
    while (p2) {
        if (p1->val != p2->val) { is_pal = false; break; }
        p1 = p1->next;
        p2 = p2->next;
    }
    
    // 4. Restore list back to original shape (Good Engineering!)
    curr = prev; prev = nullptr;
    while (curr) {
        ListNode* next_node = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next_node;
    }
    slow->next = prev;
    
    return is_pal;
}
```

---

## Summary Matrix: Trade-offs at a Glance

| Approach | List Mutation | Time | Space |
| :--- | :--- | :--- | :--- |
| **In-Place Reverse + Restore** | Modifies & Restores | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Array Copy** | Immutable | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ memory |
| **Forward/Backward Rolling Hash**| Immutable | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ (probabilistic) |
""",

    "076 Copy List with Random Pointer": """# 04 Interview Follow-ups & System Variations: Copy List with Random Pointer

The problem creates a deep copy of a linked list where each node contains an additional `random` pointer. While a Hash Map achieves $\mathcal{O}(N)$ time and $\mathcal{O}(N)$ space, the optimal **Node Interweaving Algorithm** runs in $\mathcal{O}(N)$ time and strictly $\mathcal{O}(1)$ extra space.

In technical interviews, this problem is the gold standard for in-place cloning algorithms and general directed graph deep copying.

---

## 1. The 3-Pass Node Interweaving Algorithm ($\mathcal{O}(1)$ Extra Space)

### 💡 Step-by-Step Architecture
1. **Pass 1 (Interweave Clones)**:
   - For each node $A$, create clone $A'$ and insert it directly after $A$:
     $$A \to A' \to B \to B' \to C \to C'$$
2. **Pass 2 (Assign Random Pointers)**:
   - For each original node `curr`:
     ```cpp
     if (curr->random) {
         curr->next->random = curr->random->next;
     }
     ```
3. **Pass 3 (Separate Original and Cloned Lists)**:
   - Unweave the lists to restore the original list and extract the deep copy.
- **Space Complexity**: strictly $\mathcal{O}(1)$ auxiliary space.

---

## 2. Generalization: Deep Copy of Arbitrary Graph with Cycles (LeetCode #133)

### 💡 Graph Cloning Template
- For general directed graphs with cycles, interweaving is impossible because nodes have arbitrary outgoing edges.
- **Solution**: DFS / BFS with an `unordered_map<Node*, Node*> visited` to map original nodes to their cloned copies.
- **Time Complexity**: $\mathcal{O}(V + E)$, **Space Complexity**: $\mathcal{O}(V)$.

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Space Model | Time | Extra Memory |
| :--- | :--- | :--- | :--- |
| **Hash Map (`orig -> clone`)** | Dynamic Map | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ heap |
| **Node Interweaving (Optimal)**| In-place Splicing | $\mathcal{O}(N)$ | strictly $\mathcal{O}(1)$ |
| **General Graph Clone (#133)** | Graph DFS/BFS Map | $\mathcal{O}(V+E)$ | $\mathcal{O}(V)$ |
""",

    "077 Reverse Nodes in k-Group": """# 04 Interview Follow-ups & System Variations: Reverse Nodes in k-Group

The problem reverses nodes of a singly linked list $k$ at a time (Hard). If the number of nodes is not a multiple of $k$, left-out nodes remain as they are. The optimal solution runs in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this is the most notorious pointer-manipulation question. Interviewers test boundary counting, head splicing, and remainder handling variations.

---

## 1. Iterative Pointer Splicing Template

```cpp
ListNode* reverseKGroup(ListNode* head, int k) {
    ListNode dummy(0, head);
    ListNode* group_prev = &dummy;
    
    while (true) {
        // 1. Check if k nodes exist in current group
        ListNode* kth = group_prev;
        for (int i = 0; i < k && kth != nullptr; i++) {
            kth = kth->next;
        }
        if (kth == nullptr) break; // Less than k nodes remain
        
        ListNode* group_next = kth->next;
        
        // 2. Reverse current k nodes
        ListNode* prev = group_next;
        ListNode* curr = group_prev->next;
        while (curr != group_next) {
            ListNode* tmp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = tmp;
        }
        
        // 3. Connect previous group to new group head
        ListNode* tmp = group_prev->next;
        group_prev->next = kth;
        group_prev = tmp;
    }
    return dummy.next;
}
```

---

## 2. Variation: What if Leftover Nodes $(< k)$ MUST ALSO Be Reversed?

### 💡 Reversal Without Pre-Counting Check
- In this variation, we simply reverse nodes as they come without breaking on incomplete groups.
- If $N = 7, k = 3$: groups are reversed as $[3, 2, 1], [6, 5, 4], [7]$.

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Space Model | Time | Extra Memory |
| :--- | :--- | :--- | :--- |
| **Iterative Splicing** | Pointer Rewiring | $\mathcal{O}(N)$ | strictly $\mathcal{O}(1)$ |
| **Recursive** | Call Stack | $\mathcal{O}(N)$ | $\mathcal{O}(N/k)$ stack |
""",

    "078 Add Two Numbers": """# 04 Interview Follow-ups & System Variations: Add Two Numbers

The problem adds two numbers represented by linked lists in reverse order (Least Significant Digit first). The optimal single-pass approach uses a `carry` accumulator and dummy head in $\mathcal{O}(\max(M, N))$ time and $\mathcal{O}(\max(M, N))$ output space.

In technical interviews, this problem is extended to MSB-first addition (Add Two Numbers II) and database BigInt arithmetic engines.

---

## 1. What if Digits Are Stored in Forward Order (MSB First / LeetCode #445)?

### 💡 Two Optimal Solutions
1. **Stack-Based Evaluation**:
   - Push digits of List 1 onto `Stack1` and List 2 onto `Stack2`.
   - Pop from stacks to add least significant digits first.
   - Build result linked list **backwards** using head-insertions (`newNode->next = head; head = newNode;`).
   - **Time**: $\mathcal{O}(M + N)$, **Space**: $\mathcal{O}(M + N)$.
2. **Reverse Lists First (if mutation is permitted)**:
   - In-place reverse both input lists in $\mathcal{O}(1)$ space.
   - Run standard Add Two Numbers.
   - Reverse inputs and output back to original order.
   - **Time**: $\mathcal{O}(M + N)$, **Space**: $\mathcal{O}(1)$ extra space.

---

## 2. Long Carry Propagation Chains (`9999 + 1`)

### 🛑 Potential Inefficiency
When adding 1 to a chain of 9s, the carry propagates all the way to the end, creating a new leading node (`10000`).
- The loop condition `while (l1 || l2 || carry)` handles this edge case without special post-loop conditionals.

---

## Summary Matrix: Trade-offs at a Glance

| Digit Order | Permitted Actions | Strategy | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **LSB First (#2)** | Output allocation | Single-pass pointer traverse | $\mathcal{O}(\max(M, N))$ | $\mathcal{O}(1)$ auxiliary |
| **MSB First (#445)**| Cannot modify input| 2 Stacks + Head insertion | $\mathcal{O}(M+N)$ | $\mathcal{O}(M+N)$ |
| **MSB First (#445)**| Can modify input | Reverse $\to$ Add $\to$ Reverse | $\mathcal{O}(M+N)$ | $\mathcal{O}(1)$ auxiliary |
""",

    "079 Flatten a Multilevel Doubly Linked List": """# 04 Interview Follow-ups & System Variations: Flatten a Multilevel Doubly Linked List

The problem flattens a multilevel doubly linked list containing `child` pointers into a single-level doubly linked list in preorder traversal order. The optimal iterative approach splices child sublists in-place in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem tests bidirectional pointer consistency (`prev` and `next`), stack-based DFS vs. in-place splicing, and tree preorder flattening.

---

## 1. In-Place Child Splicing Template ($\mathcal{O}(1)$ Extra Space)

```cpp
Node* flatten(Node* head) {
    Node* curr = head;
    while (curr != nullptr) {
        if (curr->child != nullptr) {
            Node* next_node = curr->next;
            Node* child = curr->child;
            
            // Find tail of child list
            while (child->next != nullptr) child = child->next;
            
            // Splice child list between curr and next_node
            curr->next = curr->child;
            curr->child->prev = curr;
            curr->child = nullptr;
            
            if (next_node != nullptr) {
                child->next = next_node;
                next_node->prev = child;
            }
        }
        curr = curr->next;
    }
    return head;
}
```

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Space Model | Time | Space |
| :--- | :--- | :--- | :--- |
| **In-Place Splicing** | Rewire child tails | $\mathcal{O}(N)$ | strictly $\mathcal{O}(1)$ |
| **Stack-Based DFS** | Recursive / Stack | $\mathcal{O}(N)$ | $\mathcal{O}(D)$ depth |
""",

    "080 Rotate List": """# 04 Interview Follow-ups & System Variations: Rotate List

The problem rotates a linked list to the right by $k$ places. The optimal approach computes length $L$, forms a circular ring by connecting tail to head, and breaks the ring at $(L - (k \pmod L) - 1)$ in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem tests modular rotation normalization, circular list manipulation, and pointer decoupling.

---

## 1. Circular Ring Algorithm

```cpp
ListNode* rotateRight(ListNode* head, int k) {
    if (!head || !head->next || k == 0) return head;
    
    // 1. Compute length and find tail
    int len = 1;
    ListNode* tail = head;
    while (tail->next) {
        tail = tail->next;
        len++;
    }
    
    // 2. Connect tail to head (form ring)
    tail->next = head;
    
    // 3. Find new tail at (len - (k % len) - 1)
    k = k % len;
    int steps_to_new_tail = len - k - 1;
    ListNode* new_tail = head;
    for (int i = 0; i < steps_to_new_tail; i++) {
        new_tail = new_tail->next;
    }
    
    // 4. Break the ring
    ListNode* new_head = new_tail->next;
    new_tail->next = nullptr;
    
    return new_head;
}
```

---

## Summary Matrix: Trade-offs at a Glance

| Parameter | Value |
| :--- | :--- |
| **Length Normalization** | $k_{\text{eff}} = k \pmod L$ |
| **Time Complexity** | $\mathcal{O}(N)$ (At most 2 passes) |
| **Space Complexity** | Strictly $\mathcal{O}(1)$ |
""",

    "081 Partition List": """# 04 Interview Follow-ups & System Variations: Partition List

The problem partitions a linked list such that all nodes with value $< x$ come before nodes with value $\ge x$ while preserving original relative order (Stable Partition). Using two dummy head chains (`less` and `greater`) runs in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem tests stable partitioning, dummy head management, and the fatal cyclic loop pointer trap.

---

## 1. The Fatal Cyclic Loop Bug: `greater->next = nullptr`

### 🛑 The Hazard
If the last node in the original list has a value $< x$, the `greater` list's tail pointer still points to that node!
- If you connect `less->next = greater_head.next` without clearing `greater->next`, you create a **closed cycle** in the list, causing an infinite loop.
- **Mandatory Invariant**: Always terminate the greater chain:
  ```cpp
  greater->next = nullptr; // Critical!
  ```

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Stability | Time | Space |
| :--- | :--- | :--- | :--- |
| **2 Dummy Chains (Optimal)** | Stable | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Array Buffer** | Stable | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ heap |
""",

    "082 LRU Cache": """# 04 Interview Follow-ups & System Variations: LRU Cache

The LRU (Least Recently Used) Cache problem designs a data structure with `get(key)` and `put(key, value)` operating in strictly $\mathcal{O}(1)$ average time. The optimal solution uses a **Hash Map** combined with a **Doubly Linked List (DLL)** with dummy head and tail nodes.

In system design and senior engineering interviews, LRU Cache is the absolute centerpiece. Interviewers test concurrency, sharded caches, lock-free eviction, and Redis-style approximations.

---

## 1. Why a Doubly Linked List (DLL) Instead of a Singly Linked List?

### 🛑 The Deletion Bottleneck
- In a Singly Linked List, deleting a node requires finding its **previous node**, which takes $\mathcal{O}(N)$ traversal time.
- In a Doubly Linked List, given a pointer to a node `Node*`, we can unlink it in strictly $\mathcal{O}(1)$ time:
  ```cpp
  node->prev->next = node->next;
  node->next->prev = node->prev;
  ```

---

## 2. Multi-Threading & Concurrency in High-Scale Systems

### 🛑 Global Lock Contention
In high-throughput systems, protecting an LRU Cache with a single global mutex creates a severe performance bottleneck.

### 💡 3 Production Concurrency Strategies
1. **Sharded / Partitioned LRU (e.g., Guava Cache / Caffeine)**:
   - Partition keys across $S$ independent LRU segments via `hash(key) % S`.
   - Each shard has its own independent mutex, reducing lock contention by $S\times$.
2. **Read-Write Lock (Shared Mutex)**:
   - `get()` acquires shared read lock; `put()` acquires exclusive write lock.
   - *Gotcha*: In strict LRU, `get()` updates node position (write operation!), requiring promotion queues (read buffers) drained asynchronously.
3. **Approximated LRU (Redis Algorithm)**:
   - Instead of maintaining a strict DLL (which consumes 24 bytes of pointer overhead per entry), sample $K = 5$ random keys and evict the one with the oldest timestamp.

---

## Summary Matrix: Trade-offs at a Glance

| Architecture | Strategy | Get / Put Latency | Concurrency | Memory Overhead |
| :--- | :--- | :--- | :--- | :--- |
| **Standard In-Memory** | Map + Doubly Linked List | $\mathcal{O}(1)$ | Single Thread | Map + 2 Pointers / node |
| **Sharded LRU** | $N$ Independent Strips | $\mathcal{O}(1)$ | High (Segmented Locks) | Moderate |
| **Sampled LRU (Redis)**| Random $K$-Sampling | $\mathcal{O}(1)$ | Lock-free / High | **0 Pointers (Ultra Low)** |
""",

    "083 LFU Cache": """# 04 Interview Follow-ups & System Variations: LFU Cache

The LFU (Least Frequently Used) Cache evicts the least frequently used key, breaking frequency ties using LRU. The optimal design uses two Hash Maps: `key_to_node` and `freq_to_dll` alongside a `min_freq` scalar, achieving $\mathcal{O}(1)$ time for both `get` and `put`.

In top-tier technical interviews (FAANG Hard), this is the ultimate cache eviction design test. Interviewers probe frequency promotions, minimum frequency invariants, and W-TinyLFU (Caffeine Cache).

---

## 1. The Dual-Map Architecture & `min_freq` Invariant

### 💡 The Structural Components
1. **`key_map`**: `unordered_map<int, Node>` mapping `key -> {val, freq, ...}`.
2. **`freq_map`**: `unordered_map<int, DoublyLinkedList>` mapping `frequency -> DLL of nodes`.
3. **`min_freq` Scalar**: Tracks the global minimum frequency across all stored items.

### 💡 Frequency Increment Step (`updateFreq`)
- When a key is accessed via `get` or updated via `put`:
  - Remove node from `freq_map[node.freq]`.
  - If `freq_map[node.freq]` becomes empty AND `node.freq == min_freq`:
    - Increment `min_freq++`.
  - Increment `node.freq++`.
  - Insert node into head of `freq_map[node.freq]`.

### 💡 Eviction Step (When Cache is Full)
- Pop the tail node (LRU node) from `freq_map[min_freq]`.
- Erase its key from `key_map`.
- Set `min_freq = 1` for the new incoming key.

---

## 2. Real-World Systems Limitation of Pure LFU & Modern Evolution (W-TinyLFU)

### 🛑 The Historical Bias Flaw in Pure LFU
If an old key received 1,000,000 requests during a burst 1 hour ago and is never requested again, its frequency counter remains at 1,000,000, preventing newer useful keys from entering the cache.

### 💡 Modern Solution: W-TinyLFU (Used in Caffeine Cache)
- Combines a small **Window LRU** for burst items with a **Count-Min Sketch** frequency tracker with periodic aging (decaying all frequency counters over time).

---

## Summary Matrix: Trade-offs at a Glance

| Cache Type | Eviction Policy | Data Structures | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **LRU Cache** | Recency only | Map + 1 DLL | $\mathcal{O}(1)$ | $\mathcal{O}(C)$ |
| **LFU Cache** | Frequency + Recency tie-break | Map + Map of DLLs + `min_freq` | $\mathcal{O}(1)$ | $\mathcal{O}(C)$ |
| **W-TinyLFU** | Recency Window + Count-Min Sketch | Window LRU + Slotted Probabilistic Map | $\mathcal{O}(1)$ | Sublinear frequency memory |
"""
}

for folder_name, content in data.items():
    folder_path = os.path.join(BASE_DIR, folder_name)
    if os.path.exists(folder_path):
        target_file = os.path.join(folder_path, "04_Interview_Followups.md")
        with open(target_file, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
        print(f"Written: {target_file}")
    else:
        print(f"Folder NOT found: {folder_path}")
