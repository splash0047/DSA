# 04 Interview Follow-ups & System Variations: Find All Anagrams in a String

The problem finds all start indices of $P$'s anagrams in $S$. The optimal solution maintains a fixed sliding window of size $|P|$ with frequency matching in $\mathcal{O}(|S|)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem tests boundary-overlap handling in distributed systems, multiset rolling hashing, and real-time packet stream inspection.

---

## 1. How to Handle Distributed Partition Boundaries (MapReduce / Multi-threading)?

### 🛑 The Boundary Split Bug
If a 100MB text file is split across 4 worker machines (25MB each), an anagram of length $|P|$ may start on Machine 1 and end on Machine 2 across the partition boundary.

### 💡 The Halo / Overlap Strategy
- Each partition $i$ must read an extra **halo of length $|P| - 1$ characters** from the start of partition $i + 1$:
  $$\text{Chunk}_i = \text{Data}[L_i \dots R_i + |P| - 1]$$
- Each worker processes its extended chunk independently.
- Guarantees zero missed anagrams and zero inter-machine communication during execution.

---

## 2. Order-Independent Multiset Rolling Hash

### 💡 Polynomial Character Hash
- Instead of maintaining 26 frequency counters, map each character $c$ to a large pseudo-random weight $W[c]$.
- The hash of any window is the commutative sum:
  $$H(\text{window}) = \sum_{c \in \text{window}} W[c] \pmod M$$
- Slide window: $H_{\text{new}} = (H_{\text{old}} - W[s[\text{out}]] + W[s[\text{in}]]) \pmod M$.
- Anagram match occurs if and only if $H(\text{window}) == H(P)$.
- **Time Complexity**: 1 integer add and 1 integer subtract per character slide.

---

## Summary Matrix: Trade-offs at a Glance

| Variation | Architecture | Strategy | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Standard In-Memory** | Single Thread | Sliding Window + Match Scalar | $\mathcal{O}(|S|)$ | $\mathcal{O}(1)$ |
| **Distributed Text** | $M$ Machines | Halo / Overlap of $(|P| - 1)$ chars | $\mathcal{O}(|S|/M)$ | $\mathcal{O}(|P|)$ |
| **Multiset Hash** | Low-latency stream | Commutative Additive Hash | $\mathcal{O}(|S|)$ | $\mathcal{O}(1)$ |
