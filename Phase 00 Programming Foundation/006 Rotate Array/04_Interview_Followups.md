# 04 Interview Follow-ups & System Variations: Rotate Array

Rotating an array of size $N$ right by $k$ steps has multiple classic solutions: Reversal Algorithm ($\mathcal{O}(N)$ time, $\mathcal{O}(1)$ space), Cyclic Replacements ($\mathcal{O}(N)$ time, $\mathcal{O}(1)$ space), and Extra Buffer ($\mathcal{O}(N)$ space).

In interviews, this problem tests deep understanding of in-place permutation algebra (cyclic decomposition, GCD), low-level cache locality, block swap I/O algorithms, and $\mathcal{O}(1)$ virtual rotations.

---

## 1. Why is the 3-Step Reversal Algorithm Preferred over Cyclic Replacements in Practice?

### 💡 Algorithmic Comparison
1. **Reversal Algorithm**:
   - `reverse(0, n - 1)`
   - `reverse(0, k - 1)`
   - `reverse(k, n - 1)`
   - *Memory Access Pattern*: Pure sequential linear scans. Highly cache-friendly; CPU hardware prefetchers load contiguous cache lines seamlessly.
2. **Cyclic Replacements (Juggling Algorithm)**:
   - Moves elements in $\gcd(n, k)$ cycles: $i \to (i + k) \pmod n$.
   - *Memory Access Pattern*: Strided/random jumps of step $k$. Causes massive CPU L1/L2 cache misses when $N$ is large, running significantly slower in real hardware despite identical theoretical $\mathcal{O}(N)$ time complexity.

---

## 2. What if You Cannot Modify the Array at All (Immutable Buffer)?

### 💡 Virtual Index Mapping ($\mathcal{O}(1)$ Rotation)
- Instead of physically shifting elements in memory, create a lightweight wrapper object (or Ring Buffer view):
  ```cpp
  class RotatedArrayView {
      const vector<int>& data;
      int offset;
  public:
      RotatedArrayView(const vector<int>& arr, int k) 
          : data(arr), offset((arr.size() - (k % arr.size())) % arr.size()) {}

      int get(int index) const {
          return data[(offset + index) % data.size()];
      }
  };
  ```
- **Time Complexity**: $\mathcal{O}(1)$ initialization, $\mathcal{O}(1)$ index access.
- **Space Complexity**: $\mathcal{O}(1)$ extra memory.

---

## 3. What if $N = 10^9$ Elements on Disk (Block Swap / Gries-Mills Algorithm)?

### 🛑 The Problem
Performing single-element cyclic swaps on a massive disk file destroys throughput due to random 4KB sector I/O operations.

### 💡 Block Swap Algorithm (Divide & Conquer)
- Split array into two blocks: $A = \text{nums}[0 \dots n-k-1]$ and $B = \text{nums}[n-k \dots n-1]$.
- We want to transform $AB \to BA$.
- Repeatedly swap the smaller block with a matching-sized sub-block of the larger block:
  - If $|A| == |B|$: Swap $A$ and $B$ in large block chunks (DMA/sequential disk reads) and finish.
  - If $|A| < |B|$: Split $B$ into $B_L$ and $B_R$ where $|B_R| = |A|$. Swap $A$ with $B_R$. Now $A$ is in final position; recurse on $B_L$ and $B_R$.
  - If $|A| > |B|$: Split $A$ into $A_L$ and $A_R$ where $|A_L| = |B|$. Swap $A_L$ with $B$. Recurse on $A_R$ and $B$.
- **Advantage**: Maximizes sequential sector I/O block reads and writes.

---

## 4. What if $k$ is Negative or $k \gg N$?

### 💡 Normalization
- Always compute effective right-shift:
  $$k_{\text{eff}} = ((k \pmod N) + N) \pmod N$$
- Left rotation by $k$ is equivalent to right rotation by $N - (k \pmod N)$.

---

## 5. What if the Data Structure is a Linked List (LeetCode #61)?

### 💡 Circular Re-linking in $\mathcal{O}(1)$ Auxiliary Space
1. Find length $N$ and connect the tail node back to the head node (forming a circular linked list).
2. Move $N - (k \pmod N) - 1$ steps forward from the head to find the new tail.
3. Break the circular link: `new_head = new_tail->next; new_tail->next = nullptr;`.
- **Time Complexity**: $\mathcal{O}(N)$, **Space Complexity**: $\mathcal{O}(1)$.

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Space | Cache Performance | Best Used When |
| :--- | :--- | :--- | :--- |
| **3-Step Reversal** | $\mathcal{O}(1)$ | **Optimal** (Sequential) | In-memory arrays on standard CPUs |
| **Cyclic Replacement** | $\mathcal{O}(1)$ | Poor (Strided jumps) | Minimizing number of write assignments ($N$ writes) |
| **Block Swap** | $\mathcal{O}(1)$ | **High** (Block chunks) | External storage / disk files |
| **Virtual View / Ring Buffer** | $\mathcal{O}(1)$ | **Instant** | Array is read-only / immutable |
| **Circular Re-linking** | $\mathcal{O}(1)$ | Pointer only | Linked list data structures |
