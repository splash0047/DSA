# 04 Interview Follow-ups & System Variations: Longest Common Prefix

The standard problem finds the longest common prefix string among an array of strings. Standard approaches include Horizontal Scanning, Vertical Scanning ($\mathcal{O}(S)$ time where $S$ is sum of all characters, $\mathcal{O}(1)$ space), and Sorting the array to compare only the first and last elements ($\mathcal{O}(N \cdot L \log N)$ time).

In senior interviews, this problem expands into dynamic Trie lookups, massive-scale distributed text processing, suffix arrays, and fault-tolerant prefix matching.

---

## 1. Vertical Scanning vs. Sorting: Which is Better in Practice?

### 💡 The Comparison
1. **Vertical Scanning**:
   - Compares character by character across all strings at column index $i$.
   - **Best Case**: $\mathcal{O}(N)$ if the first character already mismatches (e.g., `["apple", "banana", "cherry"]`).
   - **Worst Case**: $\mathcal{O}(S)$ where $S = N \times L_{\min}$.
2. **Sorting the Array (`min` and `max` strings)**:
   - Comparing only `strs[0]` and `strs[n-1]` after sorting.
   - **Drawback**: Sorting costs $\mathcal{O}(N \log N \cdot L_{\text{avg}})$, which is significantly slower when $N$ is large and the prefix is short.
- **Rule of Thumb**: Vertical scanning is strictly superior for standard static prefix queries.

---

## 2. What if There Are Frequent Insertions, Deletions, and Prefix Queries (Dynamic Trie)?

### 💡 Trie (Prefix Tree) Data Structure
When strings are added dynamically over time and we must frequently query the common prefix of all currently active strings:
- **Trie Structure**:
  - Each node stores: `children[26]`, `pass_count` (how many active strings pass through this node).
- **Prefix Query**:
  - Traverse down from root as long as `node->pass_count == total_strings`.
  - The moment a node has `pass_count < total_strings` (or branching $> 1$), stop.
- **Complexity**:
  - Insertion: $\mathcal{O}(L)$
  - Prefix Query: $\mathcal{O}(L_{\text{prefix}})$ instantaneous lookup.

---

## 3. How to Find Longest Common Prefix for 1 Billion Distributed Strings (MapReduce)?

### 🛑 The Challenge
1B strings distributed across 1,000 worker nodes.

### 💡 Associative Chunk Reduction (Divide & Conquer)
- LCP is strictly associative: $\text{LCP}(A, B, C) = \text{LCP}(\text{LCP}(A, B), C)$.
- **Worker Phase**:
  - Each worker node computes the local LCP of its partitioned chunk of strings: $P_i = \text{LCP}(\text{Partition}_i)$.
- **Tree Reduction Phase**:
  - Coordinator aggregates the 1,000 prefix strings:
    $$\text{Global LCP} = \text{LCP}(P_1, P_2, \dots, P_{1000})$$
- **Network Transfer**: Only small prefix strings are sent across the network instead of raw terabytes of data.

---

## 4. What if 1 Typo / Mismatch is Allowed (Fuzzy Common Prefix)?

### 💡 $K$-Mismatch Prefix Search
- Traverse column by column.
- Maintain a count of mismatches `errors`.
- If `errors <= K`, continue; the moment mismatches exceed $K$, truncate prefix.

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Best Scenario | Time | Space |
| :--- | :--- | :--- | :--- |
| **Vertical Scanning** | Short common prefixes / quick mismatch | $\mathcal{O}(S)$ worst, $\mathcal{O}(N)$ best | $\mathcal{O}(1)$ |
| **Sort & Compare Ends** | Small $N$, simple code | $\mathcal{O}(N \log N \cdot L)$ | $\mathcal{O}(1)$ or $\mathcal{O}(N)$ |
| **Trie (Prefix Tree)** | Dynamic inserts/deletes & repeated queries | $\mathcal{O}(L)$ per query | $\mathcal{O}(\text{Total Nodes} \cdot 26)$ |
| **Divide & Conquer / Spark** | Distributed parallel data | $\mathcal{O}(S/P + \log P)$ | $\mathcal{O}(P)$ network |
