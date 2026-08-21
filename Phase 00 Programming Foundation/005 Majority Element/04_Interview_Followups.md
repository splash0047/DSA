# 04 Interview Follow-ups & System Variations: Majority Element

The classic problem finds the element appearing $> \lfloor N/2 \rfloor$ times. The optimal solution is the **Boyer-Moore Voting Algorithm**, achieving $\mathcal{O}(N)$ time and strictly $\mathcal{O}(1)$ space.

In top-tier interviews, interviewers test your ability to generalize this to $> \lfloor N/k \rfloor$ thresholds (Misra-Gries), handle unverified streams, and distribute the computation across multi-core / MapReduce architectures.

---

## 1. What if We Want Elements Appearing $> \lfloor N/3 \rfloor$ Times (Majority Element II)?

### 🛑 Mathematical Principle
There can be at most **2** elements that appear strictly more than $\lfloor N/3 \rfloor$ times.

### 💡 Boyer-Moore with 2 Candidates & 2 Counters
1. **Pass 1 (Candidate Elimination)**:
   - Maintain `cand1`, `count1`, `cand2`, `count2`.
   - If `x == cand1`, `count1++`.
   - Else if `x == cand2`, `count2++`.
   - Else if `count1 == 0`, `cand1 = x; count1 = 1`.
   - Else if `count2 == 0`, `cand2 = x; count2 = 1`.
   - Else, decrement both `count1--` and `count2--` (triplet cancellation).
2. **Pass 2 (Verification)**:
   - Count exact occurrences of `cand1` and `cand2` across the array.
   - Include any candidate whose count $> \lfloor N/3 \rfloor$.
- **Time Complexity**: $\mathcal{O}(N)$, **Space Complexity**: $\mathcal{O}(1)$.

---

## 2. Generalized Majority Element: Elements Appearing $> \lfloor N/k \rfloor$ Times (Misra-Gries Algorithm)

### 🛑 Mathematical Principle
There can be at most **$k - 1$** distinct elements appearing strictly more than $\lfloor N/k \rfloor$ times.

### 💡 Heavy Hitters / Misra-Gries Algorithm
- Maintain a dynamic map of at most $k - 1$ candidates: `unordered_map<int, int> candidates`.
- For each incoming element $x$:
  - If $x$ is already in `candidates`, increment its counter.
  - Else if `candidates.size() < k - 1`, insert `candidates[x] = 1`.
  - Else, decrement every counter in `candidates` by 1. Remove all keys whose count reaches 0.
- **Pass 2**: Verify remaining candidates against the dataset.
- **Time Complexity**: $\mathcal{O}(N \log k)$ or $\mathcal{O}(N \cdot k)$, **Space Complexity**: $\mathcal{O}(k)$.

---

## 3. How to Parallelize / Distribute Boyer-Moore Across $P$ Machines (MapReduce)?

### 🛑 The Challenge
Can we run Boyer-Moore on partitioned data across $P$ nodes without shuffling the raw items?

### 💡 Parallel Boyer-Moore Merge Rule
Each machine $i$ independently processes its local chunk and outputs a local pair: $(C_i, V_i)$ where $C_i$ is the candidate and $V_i$ is its surviving vote count.

**Merge Function for Two Summaries $(C_1, V_1)$ and $(C_2, V_2)$**:
1. If $C_1 == C_2$: Output $(C_1, V_1 + V_2)$.
2. If $C_1 \neq C_2$:
   - If $V_1 > V_2$: Output $(C_1, V_1 - V_2)$.
   - If $V_2 > V_1$: Output $(C_2, V_2 - V_1)$.
   - If $V_1 == V_2$: Output (None, 0).
3. The root/coordinator node receives the single final candidate and triggers a verification count pass.
- **Communication Cost**: Only $\mathcal{O}(P)$ scalars transmitted over the network!

---

## 4. What if the Input is an Unbounded Real-Time Stream?

### 💡 Streaming Guarantees & Lossy Counting
- In an infinite stream where total size $N$ is unknown or unbounded, we cannot perform a second verification pass.
- The Misra-Gries summary guarantees that if an element's true frequency $> \lfloor N/k \rfloor$, it is **guaranteed to be in the candidate list**.
- For frequency bounds with error $\epsilon$, use the **Space-Saving Algorithm** or **Lossy Counting** using $\mathcal{O}(1/\epsilon)$ memory.

---

## 5. Alternative Perspective: Bit Manipulation (Column-wise Voting)

### 💡 32-Bit Counter Method
- A 32-bit integer consists of 32 individual bits.
- For each bit position $j \in [0, 31]$:
  - Count how many elements in `nums` have their $j$-th bit set.
  - If the count $> \lfloor N/2 \rfloor$, then the majority element MUST have its $j$-th bit set to 1.
- Reconstruct the majority element from the 32 majority bit decisions.
- **Time Complexity**: $\mathcal{O}(32 \cdot N) = \mathcal{O}(N)$, **Space Complexity**: $\mathcal{O}(1)$.
- **Advantage**: Highly parallelizable and requires zero dynamic state branch switches.

---

## Summary Matrix: Trade-offs at a Glance

| Scenario | Candidate Capacity | Technique | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **$> \lfloor N/2 \rfloor$ Guaranteed** | 1 candidate | Boyer-Moore (Single Pass) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **$> \lfloor N/2 \rfloor$ Not Guaranteed** | 1 candidate | Boyer-Moore (2 Passes) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **$> \lfloor N/3 \rfloor$** | 2 candidates | Boyer-Moore (2 Candidates) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **$> \lfloor N/k \rfloor$** | $k - 1$ candidates | Misra-Gries / Frequent Items | $\mathcal{O}(N \log k)$ | $\mathcal{O}(k)$ |
| **Distributed Across $P$ Nodes** | 1 summary/node | Parallel Boyer-Moore Merge | $\mathcal{O}(N/P + P)$ | $\mathcal{O}(P)$ network |
| **Bit-Level Independent** | 32 independent bits | Bit-Voting Accumulator | $\mathcal{O}(32N)$ | $\mathcal{O}(1)$ |
