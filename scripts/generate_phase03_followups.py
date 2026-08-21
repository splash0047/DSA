import os

BASE_DIR = r"c:\Users\Pinak chimurkar\DSA\Phase 03 Binary Search"

data = {
    "044 Binary Search": """# 04 Interview Follow-ups & System Variations: Binary Search

The classic binary search locates a target value in a sorted array in $\mathcal{O}(\log N)$ time and $\mathcal{O}(1)$ space. 

In top-tier technical interviews, this is the foundational problem used to probe low-level CPU branch prediction, 64-bit integer overflow, searching unbounded streams (Galloping Search), and disk-based external search.

---

## 1. The Famous Midpoint Integer Overflow Bug

### 🛑 The Problem
```cpp
int mid = (left + right) / 2; // Dangerous!
```
- If `left` and `right` are large positive integers (e.g., in a 2-billion element array where `left = 1.5 * 10^9` and `right = 2 * 10^9`), their sum exceeds $2^{31} - 1 = 2,147,483,647$.
- This results in a negative integer overflow and crashes with `IndexOutOfBounds`.

### 💡 The Production Solutions
1. **Subtraction Safe Formula**:
   ```cpp
   int mid = left + (right - left) / 2;
   ```
2. **Unsigned Bitwise Shift**:
   ```cpp
   int mid = (left + right) >> 1; // In languages with unsigned ints / uint
   // Or in Java: int mid = (left + right) >>> 1;
   ```

---

## 2. What if $N = 10^9$ Elements on Disk / Storage?

### 🛑 Memory Bottleneck
- An array of $10^9$ 64-bit integers takes 8 GB.
- If storage is on SSD / HDD, every `nums[mid]` probe triggers a random sector read.

### 💡 Disk-Optimized B-Trees & Block Probing
- A standard binary search takes $\log_2(10^9) \approx 30$ random disk seeks (slow on spinning disks).
- **Optimization (B-Tree / Multi-way Search)**:
  - Read disk blocks of size 4KB (containing 512 integers).
  - Perform 512-way branching per disk read.
  - Reduces disk I/O from 30 seeks to $\log_{512}(10^9) \approx 3\text{--}4$ block reads.

---

## 3. What if the Array Length is UNKNOWN or INFINITE (Stream / Unbounded)?

### 💡 Exponential / Galloping Search
- Start with `bound = 1`.
- While `array[bound] < target`:
  - `bound *= 2` (check $1, 2, 4, 8, 16 \dots$).
- Once `array[bound] >= target` (or out of bounds exception occurs), binary search within the range `[bound / 2, bound]`.
- **Time Complexity**: $\mathcal{O}(\log P)$ where $P$ is the target's actual position in the stream.

---

## 4. Hardware Optimization: Branchless Binary Search (Eytzinger Layout)

### 🛑 CPU Branch Mispredictions
Standard binary search causes frequent CPU branch mispredictions because the comparison `nums[mid] < target` is unpredictable (~50% probability).

### 💡 Branchless Ternary Step
```cpp
while (len > 1) {
    int half = len / 2;
    left += (nums[left + half] < target) * half;
    len -= half;
}
return (nums[left] == target) ? left : -1;
```
- Uses conditional move instructions (`CMOV`) without branching, maximizing CPU instruction pipeline throughput.

---

## Summary Matrix: Trade-offs at a Glance

| Scenario | Challenge | Technique | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Standard Array** | Basic search | Left + (Right - Left)/2 | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| **Unbounded / Stream** | Unknown $N$ | Exponential Galloping Search | $\mathcal{O}(\log P)$ | $\mathcal{O}(1)$ |
| **Disk Block Storage** | High seek latency | B-Tree / Multi-way branching | $\mathcal{O}(\log_B N)$ I/O | $\mathcal{O}(B)$ |
| **High Frequency CPU** | Branch stall | Branchless CMOV Step | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
""",

    "045 Search Insert Position": """# 04 Interview Follow-ups & System Variations: Search Insert Position

The problem finds the index of `target` in a sorted array, or the index where it would be if inserted in order. The optimal binary search maintains `left <= right` and returns `left` in $\mathcal{O}(\log N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem is equivalent to implementing `std::lower_bound` in C++ or `bisect_left` in Python. Interviewers probe boundary invariants, dynamic insertion cost trade-offs, and multi-set duplicates.

---

## 1. Why Returning `left` is Guaranteed to Be the Exact Insertion Point

### 💡 Loop Termination Invariant
- The search space invariant is `[left, right]`.
- When the while loop `while (left <= right)` terminates:
  - `right = left - 1`.
  - All elements at indices $< left$ are strictly $< \text{target}$.
  - All elements at indices $\ge left$ are strictly $\ge \text{target}$.
- Therefore, `left` is always the first index whose value is $\ge \text{target}$ (the exact insertion position).

---

## 2. Lower Bound vs. Upper Bound (Bisect Left vs. Bisect Right)

| Function | Condition | Description |
| :--- | :--- | :--- |
| **`lower_bound` (`bisect_left`)** | `nums[mid] >= target` $\to$ `right = mid - 1` | First element $\ge \text{target}$ |
| **`upper_bound` (`bisect_right`)** | `nums[mid] > target` $\to$ `right = mid - 1` | First element strictly $> \text{target}$ |

- If target contains duplicates (`[1, 2, 2, 2, 3]`, target = 2):
  - `lower_bound` returns index 1 (start of duplicates).
  - `upper_bound` returns index 4 (one past end of duplicates).

---

## 3. Dynamic Array Insertion Bottlenecks: $\mathcal{O}(\log N)$ Search vs. $\mathcal{O}(N)$ Shift

### 🛑 The Memory Bottleneck
While binary search finds the insertion index in $\mathcal{O}(\log N)$, physically inserting an element into a dynamic array (like `std::vector` or Python `list`) requires shifting all subsequent elements to the right ($\mathcal{O}(N)$ memory move).

### 💡 Scalable Alternatives for Frequent Insertions
1. **Balanced Binary Search Tree (AVL / Red-Black Tree)**:
   - Search: $\mathcal{O}(\log N)$, Insert: $\mathcal{O}(\log N)$.
2. **B+ Tree / Skip List**:
   - Cache-friendly block insertions in $\mathcal{O}(\log N)$.

---

## Summary Matrix: Trade-offs at a Glance

| Goal | Operation | Time | Space |
| :--- | :--- | :--- | :--- |
| **Find Insertion Index** | Binary Search (`lower_bound`) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| **Physical Array Insert** | Binary Search + Memory Shift | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Dynamic Insert + Search** | Red-Black Tree / B-Tree | $\mathcal{O}(\log N)$ | $\mathcal{O}(N)$ |
""",

    "046 Find First and Last Position of Element in Sorted Array": """# 04 Interview Follow-ups & System Variations: Find First and Last Position

The problem finds the starting and ending position of a given `target` in a sorted array with duplicates. The optimal approach runs two separate binary searches (`lower_bound` and `upper_bound - 1`) in $\mathcal{O}(\log N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem is used to test boundary binary search templates, counting element frequencies in $\mathcal{O}(\log N)$, and distributed inverted index search.

---

## 1. Single Reusable Binary Search Template for Both Left and Right Bounds

### 💡 Generalized Helper Function
```cpp
int findBound(vector<int>& nums, int target, bool isFirst) {
    int left = 0, right = nums.size() - 1, ans = -1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) {
            ans = mid;
            if (isFirst) right = mid - 1; // Keep searching left for first occurrence
            else left = mid + 1;         // Keep searching right for last occurrence
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return ans;
}
```

---

## 2. Follow-up: Count Frequency of Target in $\mathcal{O}(\log N)$ Time

### 💡 Constant-Time Count from Range Boundaries
- Instead of linearly scanning duplicates in $\mathcal{O}(K)$ time:
  $$\text{Count}(\text{target}) = \text{last\_pos} - \text{first\_pos} + 1$$
- If `first_pos == -1`, count is 0.
- Guarantees strictly $\mathcal{O}(\log N)$ runtime even if all $10^9$ elements in the array are equal to `target`.

---

## 3. What if $N = 10^9$ on Distributed Inverted Indices?

### 💡 Search Engine Postings List
- In search engines (Lucene / ElasticSearch), terms point to sorted lists of document IDs.
- To find all documents containing a term within a timestamp range $[T_1, T_2]$, run `lower_bound(T1)` and `upper_bound(T2)` on the postings list.

---

## Summary Matrix: Trade-offs at a Glance

| Variation | Strategy | Time | Space |
| :--- | :--- | :--- | :--- |
| **First & Last Position** | Two Binary Searches (Left & Right) | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| **Count Target Frequency** | `(last - first + 1)` formula | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| **Linear Duplicates Scan** | Find one + Scan both ways | $\mathcal{O}(\log N + K)$ | $\mathcal{O}(1)$ |
""",

    "047 Search in Rotated Sorted Array": """# 04 Interview Follow-ups & System Variations: Search in Rotated Sorted Array

The problem searches for `target` in an array of distinct integers rotated at an unknown pivot. The optimal approach identifies which half (`[left...mid]` or `[mid...right]`) is sorted and discards the other half in $\mathcal{O}(\log N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem is a classic test of partitioned search space invariants and edge cases in rotated topologies.

---

## 1. The Core Sorted-Half Decision Tree

### 💡 The Fundamental Invariant
In any rotated sorted array with distinct elements, splitting at `mid` **always results in at least one half being strictly sorted**:
1. **If `nums[left] <= nums[mid]` (Left Half is Sorted)**:
   - If `nums[left] <= target && target < nums[mid]`: target is in the left half $\implies$ `right = mid - 1`.
   - Else: target must be in the right half $\implies$ `left = mid + 1`.
2. **Else (`nums[mid] < nums[right]`, Right Half is Sorted)**:
   - If `nums[mid] < target && target <= nums[right]`: target is in the right half $\implies$ `left = mid + 1`.
   - Else: target must be in the left half $\implies$ `right = mid - 1`.

---

## 2. 2-Pass Approach vs. 1-Pass Approach

### 💡 Comparison
1. **2-Pass Approach**:
   - Pass 1: Find the pivot index (minimum element) using binary search in $\mathcal{O}(\log N)$.
   - Pass 2: Binary search either the left segment `[0 ... pivot-1]` or right segment `[pivot ... N-1]`.
2. **1-Pass Approach (Optimal)**:
   - Determine the sorted half on the fly in a single while-loop.
   - Requires fewer lines of code and fewer comparison operations.

---

## 3. What if Array is Rotated by $0$ (Not Rotated at All)?

### 💡 Natural Compatibility
- If array is not rotated, `nums[left] <= nums[mid]` is always true for the left half.
- The algorithm seamlessly degenerates into standard classic binary search without needing special-case checks.

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Passes | Time | Space | Edge Cases |
| :--- | :--- | :--- | :--- | :--- |
| **1-Pass Sorted Half** | 1 | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ | Clean single loop |
| **2-Pass (Find Min First)**| 2 | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ | Extra boundary conditionals |
""",

    "048 Search in Rotated Sorted Array II": """# 04 Interview Follow-ups & System Variations: Search in Rotated Sorted Array II

The problem searches for `target` in a rotated sorted array that **may contain duplicates**. The optimal approach shrinks boundaries when `nums[left] == nums[mid] == nums[right]` by incrementing `left++` and decrementing `right--`, achieving $\mathcal{O}(\log N)$ average time and $\mathcal{O}(N)$ worst-case time with $\mathcal{O}(1)$ space.

In technical interviews, this is the definitive question for proving why duplicates break sub-linear worst-case time complexity.

---

## 1. Why Duplicates Force $\mathcal{O}(N)$ Worst-Case Time (Mathematical Proof)

### 🛑 The Ambiguity Hazard
Consider the input:
$$\text{nums} = [1, 1, 1, 1, 1, 2, 1, 1], \quad \text{target} = 2$$
- `left = 0` (`nums[0] = 1`), `right = 7` (`nums[7] = 1`), `mid = 3` (`nums[3] = 1`).
- Notice that:
  $$\text{nums}[left] == \text{nums}[mid] == \text{nums}[right] == 1$$
- Is the left half sorted? Yes (`[1, 1, 1, 1]`).
- Is the right half sorted? Yes (`[1, 2, 1, 1]` is rotated, but `[1, 1]` is sorted).
- **The Dilemma**: It is mathematically impossible to know whether the single target element `2` is in the left half or right half without examining elements sequentially.
- Therefore, in the worst case (all elements identical except one), any deterministic algorithm must degrade to $\mathcal{O}(N)$ linear scan.

---

## 2. The Duplicate Resolution Step

```cpp
if (nums[left] == nums[mid] && nums[mid] == nums[right]) {
    left++;
    right--; // Safely eliminate duplicate boundaries
}
```

---

## Summary Matrix: Trade-offs at a Glance

| Feature | Rotated Array I (#33) | Rotated Array II (#81) |
| :--- | :--- | :--- |
| **Duplicate Elements** | Strictly Forbidden (Distinct) | Allowed |
| **Average Time Complexity** | $\mathcal{O}(\log N)$ | $\mathcal{O}(\log N)$ |
| **Worst-Case Time Complexity** | $\mathcal{O}(\log N)$ guaranteed | $\mathcal{O}(N)$ worst-case |
| **Space Complexity** | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ |
""",

    "049 Find Minimum in Rotated Sorted Array": """# 04 Interview Follow-ups & System Variations: Find Minimum in Rotated Sorted Array

The problem finds the minimum element (the rotation pivot) in a rotated sorted array of unique integers. The optimal binary search compares `nums[mid]` with `nums[right]` in $\mathcal{O}(\log N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem tests boundary comparison selection (`nums[right]` vs. `nums[left]`) and calculating the exact rotation count.

---

## 1. Why Compare `nums[mid]` with `nums[right]` instead of `nums[left]`?

### 🛑 The Asymmetry of Unrotated Arrays
Consider an array that is not rotated (or already sorted): `nums = [1, 2, 3, 4, 5]`.
- `left = 0` (`nums[left] = 1`), `mid = 2` (`nums[mid] = 3`), `right = 4` (`nums[right] = 5`).
- If you compare with `nums[left]`: `nums[mid] > nums[left]` ($3 > 1$). In a rotated array, this means the minimum is in the right half, but here the minimum is at index 0 (left half)!
- **If you compare with `nums[right]`**:
  - If `nums[mid] > nums[right]`: Minimum MUST be in the right half `[mid + 1 ... right]`.
  - If `nums[mid] < nums[right]`: Minimum MUST be in `[left ... mid]` (note: include `mid`!).
- Comparing with `nums[right]` works universally across both rotated and unrotated arrays without special checks.

---

## 2. Finding the Exact Rotation Count $K$

### 💡 Rotation Count Formula
- The index of the minimum element `min_idx` represents exactly how many times the array was rotated right.
- For example: `[4, 5, 1, 2, 3]` $\to$ minimum is at index 2 $\implies$ rotated right by 2 steps.

---

## 3. What if Duplicates Are Allowed (LeetCode #154)?

### 💡 Shrinking `right--` on Equality
- If `nums[mid] == nums[right]`, we cannot know which side holds the pivot.
- Action: `right--` (decrement right boundary by 1).
- Time Complexity: $\mathcal{O}(\log N)$ average, $\mathcal{O}(N)$ worst case.

---

## Summary Matrix: Trade-offs at a Glance

| Scenario | Elements | Comparison | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Distinct (#153)** | Unique | `nums[mid]` vs `nums[right]` | $\mathcal{O}(\log N)$ strictly | $\mathcal{O}(1)$ |
| **Duplicates (#154)** | With Duplicates | `nums[mid] == nums[right] ? right--` | $\mathcal{O}(\log N)$ avg / $\mathcal{O}(N)$ worst | $\mathcal{O}(1)$ |
""",

    "050 Single Element in a Sorted Array": """# 04 Interview Follow-ups & System Variations: Single Element in a Sorted Array

The problem finds the single unique element in a sorted array where every other element appears exactly twice. The optimal binary search uses the **Even-Odd Index Pairing Invariant** in $\mathcal{O}(\log N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem is used to compare Bitwise XOR ($\mathcal{O}(N)$) vs. Binary Search ($\mathcal{O}(\log N)$) and bitwise XOR index mapping (`mid ^ 1`).

---

## 1. Why Bitwise XOR is Sub-Optimal Here ($\mathcal{O}(N)$ vs. $\mathcal{O}(\log N)$)

### 💡 XOR Technique
- XORing all elements together cancels out duplicate pairs: $x \oplus x = 0$.
- Result is the single element.
- **Limitation**: Requires visiting all $N$ elements ($\mathcal{O}(N)$ time), completely ignoring the fact that the array is **sorted**.

---

## 2. The Even-Odd Index Invariant & The `mid ^ 1` Bitwise Trick

### 💡 The Pairing Pattern
- **Before the unique element**: Pairs start at EVEN indices and end at ODD indices:
  - $(0, 1), (2, 3), (4, 5) \dots$
  - Invariant: `nums[even] == nums[even + 1]`.
- **After the unique element**: The shift causes pairs to start at ODD indices and end at EVEN indices:
  - $(1, 2), (3, 4), (5, 6) \dots$
  - Invariant: `nums[odd] == nums[odd + 1]`.

### 💡 Elegant `mid ^ 1` Implementation
```cpp
int singleNonDuplicate(vector<int>& nums) {
    int left = 0, right = nums.size() - 1;
    while (left < right) {
        int mid = left + (right - left) / 2;
        // mid ^ 1 toggles even to odd (mid + 1) and odd to even (mid - 1)
        if (nums[mid] == nums[mid ^ 1]) {
            left = mid + 1; // Invariant holds; single element is to the right
        } else {
            right = mid;    // Invariant broken; single element is at mid or to the left
        }
    }
    return nums[left];
}
```

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Array Sorted? | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| **Bitwise XOR** | Not required | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Binary Search (`mid ^ 1`)**| Must be sorted | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
""",

    "051 Find Peak Element": """# 04 Interview Follow-ups & System Variations: Find Peak Element

The problem finds a peak element (an element strictly greater than its neighbors) in an unsorted array. The optimal binary search follows the discrete upward gradient in $\mathcal{O}(\log N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem is a classic demonstration of binary search on unsorted arrays, 2D matrix peak finding, and hill-climbing optimization.

---

## 1. Why Binary Search Works on an UNSORTED Array

### 💡 The Gradient Ascent Invariant
- Even though the array is unsorted, compare `nums[mid]` with `nums[mid + 1]`:
  1. **If `nums[mid] < nums[mid + 1]`**:
     - The slope is rising to the right.
     - Because `nums[n] = -\infty`, the slope must eventually decline. Therefore, **at least one peak is guaranteed to exist in the right half `[mid + 1 ... right]`**.
  2. **If `nums[mid] > nums[mid + 1]`**:
     - The slope is declining to the right (or rising to the left).
     - A peak is guaranteed to exist in the left half `[left ... mid]`.
- Always moving towards the ascending slope guarantees converging to a local maximum in $\mathcal{O}(\log N)$.

---

## 2. Generalization: 2D Matrix Peak Finding (LeetCode #1901)

### 🛑 The Challenge
Find a peak in an $R \times C$ matrix where a peak is greater than its top, bottom, left, and right neighbors.

### 💡 Divide & Conquer on Matrix Columns
1. Select middle column `mid_col = C / 2`.
2. Find the global maximum element in this column at row $r_{\max}$ in $\mathcal{O}(R)$ time.
3. Compare `matrix[r_max][mid_col]` with its horizontal neighbors `mid_col - 1` and `mid_col + 1`:
   - If greater than both: found a 2D peak!
   - If `matrix[r_max][mid_col + 1] > matrix[r_max][mid_col]`: recurse on right sub-matrix.
   - Else: recurse on left sub-matrix.
- **Time Complexity**: $\mathcal{O}(R \log C)$, **Space Complexity**: $\mathcal{O}(1)$.

---

## Summary Matrix: Trade-offs at a Glance

| Variation | Dimension | Optimal Strategy | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **1D Array Peak** | 1D | Gradient Binary Search | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| **2D Matrix Peak (#1901)** | 2D ($R \times C$) | Column Max + Binary Search | $\mathcal{O}(R \log C)$ | $\mathcal{O}(1)$ |
""",

    "052 Peak Index in a Mountain Array": """# 04 Interview Follow-ups & System Variations: Peak Index in a Mountain Array

The problem finds the peak index in a strictly increasing then strictly decreasing mountain array. The optimal binary search checks `nums[mid] < nums[mid + 1]` in $\mathcal{O}(\log N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem is compared with general peak finding, Ternary Search on unimodal functions, and Golden Section Search.

---

## 1. Binary Search vs. Ternary Search on Unimodal Functions

| Method | Probes Per Step | Shrink Factor | Recurrence | Total Iterations |
| :--- | :--- | :--- | :--- | :--- |
| **Binary Search (Gradient)** | 2 probes (`mid`, `mid+1`) | $1/2$ (halved) | $T(N) = T(N/2) + \mathcal{O}(1)$ | $\approx \log_2 N$ |
| **Ternary Search** | 2 probes ($m_1, m_2$) | $2/3$ (tri-section)| $T(N) = T(2N/3) + \mathcal{O}(1)$ | $\approx 2 \log_{1.5} N$ |

- **Conclusion**: Binary search via slope gradient requires fewer comparison operations than ternary search.

---

## 2. Search in Mountain Array (LeetCode #1095)

### 💡 3-Phase Search with Restricted Probes
- You are given a `MountainArray` interface with at most 100 calls allowed:
  1. **Phase 1**: Find the peak index using Binary Search ($\approx 30$ calls).
  2. **Phase 2**: Binary search target in the increasing left slope `[0 ... peak]` ($\approx 30$ calls).
  3. **Phase 3**: If not found, binary search target in the decreasing right slope `[peak + 1 ... n - 1]` with reverse comparator ($\approx 30$ calls).
- **Total API Calls**: $\le 90 \ll 100$.

---

## Summary Matrix: Trade-offs at a Glance

| Problem | Strategy | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| **Find Mountain Peak** | Binary Search on slope | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| **Search Target in Mountain (#1095)**| Find Peak $\to$ 2 Binary Searches | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
""",

    "053 Search a 2D Matrix": """# 04 Interview Follow-ups & System Variations: Search a 2D Matrix

The problem searches for `target` in an $M \times N$ matrix where each row is sorted and the first integer of each row is greater than the last integer of the previous row. Treating the 2D matrix as a virtual flattened 1D sorted array of size $M \times N$ runs in $\mathcal{O}(\log(M \times N))$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem tests virtual coordinate projection, preventing 32-bit index overflow, and cache layout analysis.

---

## 1. Virtual 1D-to-2D Coordinate Mapping

### 💡 The Mapping Formulas
- Total virtual elements: $T = M \times N$.
- Range: `left = 0`, `right = M * N - 1`.
- For any 1D index `mid`:
  $$\text{row} = \lfloor \text{mid} / N \rfloor, \quad \text{col} = \text{mid} \pmod N$$
- Access element: `matrix[row][col]`.

---

## 2. Integer Overflow Hazard on Virtual 1D Bounds

### 🛑 The Hazard
If $M = 50,000$ and $N = 50,000$, $M \times N = 2.5 \times 10^9 > 2^{31} - 1$.
- `right = M * N - 1` overflows 32-bit signed `int`.
- **Solution**: Use `long long` for virtual pointers:
  ```cpp
  long long left = 0, right = (long long)m * n - 1;
  ```
- Or perform two 1D binary searches: First binary search to find the candidate row ($\mathcal{O}(\log M)$), second binary search inside that row ($\mathcal{O}(\log N)$).

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Pointers | Time | Space | Overflow Risk |
| :--- | :--- | :--- | :--- | :--- |
| **Virtual 1D Flatten** | `long long` 1D | $\mathcal{O}(\log(MN))$ | $\mathcal{O}(1)$ | Handled via 64-bit |
| **2-Step Binary Search** | Row BS $\to$ Col BS | $\mathcal{O}(\log M + \log N)$ | $\mathcal{O}(1)$ | Zero overflow risk |
""",

    "054 Search a 2D Matrix II": """# 04 Interview Follow-ups & System Variations: Search a 2D Matrix II

The problem searches for `target` in an $M \times N$ matrix where rows and columns are independently sorted in ascending order. The optimal **Saddleback Search** starts at the top-right corner $(0, N - 1)$ or bottom-left corner in $\mathcal{O}(M + N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem is used to compare Saddleback elimination against Quad-Tree Divide & Conquer and row-wise binary search.

---

## 1. Why Start at the Top-Right (or Bottom-Left) Corner?

### 💡 The Asymmetric Decision Property
- **Top-Left $(0, 0)$**: Both right and down increase $\implies$ ambiguous decision when `target > matrix[0][0]`.
- **Bottom-Right $(M-1, N-1)$**: Both left and up decrease $\implies$ ambiguous decision when `target < matrix[M-1][N-1]`.
- **Top-Right $(0, N-1)$ (Optimal Saddle Point)**:
  - Moving **Left** strictly decreases value.
  - Moving **Down** strictly increases value.
  - If `matrix[r][c] == target`: return `true`.
  - If `matrix[r][c] > target`: eliminate current column (`c--`).
  - If `matrix[r][c] < target`: eliminate current row (`r++`).
- **Time Complexity**: At most $M + N$ steps.

---

## 2. 3 Algorithmic Approaches Compared

| Approach | Strategy | Time Complexity | Best Scenario |
| :--- | :--- | :--- | :--- |
| **Row-wise Binary Search** | Binary search all $M$ rows | $\mathcal{O}(M \log N)$ | $M \ll N$ (e.g., $2 \times 10^6$) |
| **Saddleback Search** | Step from Top-Right corner | $\mathcal{O}(M + N)$ | Square matrices ($M \approx N$) |
| **Quad-Tree Divide & Conquer**| Split into 4 submatrices | $\mathcal{O}((MN)^{\log_4 3}) \approx \mathcal{O}(N^{1.58})$ | Extremely large sparse matrices |

---

## Summary Matrix: Trade-offs at a Glance

| Matrix Shape | Recommended Algorithm | Time Complexity | Space |
| :--- | :--- | :--- | :--- |
| **Square ($M \approx N$)** | Top-Right Saddleback | $\mathcal{O}(M + N)$ | $\mathcal{O}(1)$ |
| **Wide ($M \ll N$)** | Binary Search on each Row | $\mathcal{O}(M \log N)$ | $\mathcal{O}(1)$ |
| **Tall ($M \gg N$)** | Binary Search on each Col | $\mathcal{O}(N \log M)$ | $\mathcal{O}(1)$ |
""",

    "055 Koko Eating Bananas": """# 04 Interview Follow-ups & System Variations: Koko Eating Bananas

The problem finds the minimum integer eating speed $k$ such that Koko can eat all bananas within $h$ hours. The optimal approach uses **Binary Search on the Answer** in the range $[1, \max(\text{piles})]$ with a greedy feasibility check in $\mathcal{O}(N \log(\max(\text{piles})))$ time and $\mathcal{O}(1)$ space.

In technical interviews, this is the archetypal template for monotonic search spaces. Interviewers test ceiling division formulas without floating-point errors, 64-bit integer overflow, and extreme constraint scaling.

---

## 1. Avoiding Floating-Point Division (Ceiling Division Formula)

### 🛑 The Hazard of `ceil((double)pile / k)`
Floating-point conversions introduce precision errors and slower runtime execution on CPUs.

### 💡 Pure Integer Ceiling Division
$$\lceil \text{pile} / k \rceil = \lfloor (\text{pile} + k - 1) / k \rfloor = \frac{\text{pile} + k - 1}{k}$$

---

## 2. Preventing 64-bit Accumulator Overflow

### 🛑 The Bug
If `piles` has $10^5$ elements of size $10^9$, and testing $k = 1$, the total hours required is $10^{14}$, which overflows standard 32-bit signed `int`.
- Always accumulate `long long total_hours = 0`.

---

## 3. The Universal Binary Search on Answer Template

```cpp
int minEatingSpeed(vector<int>& piles, int h) {
    int left = 1, right = *max_element(piles.begin(), piles.end());
    int ans = right;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        long long hours = 0;
        for (int p : piles) {
            hours += (p + mid - 1) / mid;
        }
        
        if (hours <= h) {
            ans = mid;         // Feasible; try smaller speed
            right = mid - 1;
        } else {
            left = mid + 1;    // Infeasible; increase speed
        }
    }
    return ans;
}
```

---

## Summary Matrix: Trade-offs at a Glance

| Component | Choice | Rationale |
| :--- | :--- | :--- |
| **Search Space** | $[1, \max(\text{piles})]$ | Min possible speed is 1; max speed needs at most largest pile |
| **Feasibility Test** | $\mathcal{O}(N)$ linear pass | Monotonically decreasing hours with increasing $k$ |
| **Total Complexity** | $\mathcal{O}(N \log(\max P))$ | Guaranteed sub-second execution for $10^5$ items |
""",

    "056 Capacity To Ship Packages Within D Days": """# 04 Interview Follow-ups & System Variations: Capacity To Ship Packages Within D Days

The problem finds the least ship capacity to transport all packages within $D$ days in contiguous conveyor order. Using Binary Search on the Answer in range $[\max(\text{weights}), \sum \text{weights}]$, the optimal approach runs in $\mathcal{O}(N \log(\sum W))$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem is structurally identical to Book Allocation Problem and Split Array Largest Sum.

---

## 1. Search Space Boundary Invariants

### 💡 Why `left = max(weights)` and `right = sum(weights)`
1. **Lower Bound (`left = max(weights)`)**: The ship MUST be capable of carrying the single heaviest package. Any capacity $< \max(W)$ can never ship that package.
2. **Upper Bound (`right = sum(weights)`)**: A ship with capacity $\sum W$ can ship all packages in exactly 1 day.

---

## 2. Equivalence Trinity in Computer Science Interviews

These 3 classic problems share the **exact same code and mathematical reduction**:
1. **Capacity to Ship Packages Within D Days (LeetCode #1011)**
2. **Split Array Largest Sum (LeetCode #410)**
3. **Book Allocation Problem / Painter's Partition Problem**

---

## Summary Matrix: Trade-offs at a Glance

| Parameter | Value |
| :--- | :--- |
| **Search Range** | $[\max(weights), \sum weights]$ |
| **Check Monotonicity** | Larger capacity $\implies$ fewer or equal days needed |
| **Time Complexity** | $\mathcal{O}(N \log(\sum W))$ |
| **Space Complexity** | $\mathcal{O}(1)$ |
""",

    "057 Split Array Largest Sum": """# 04 Interview Follow-ups & System Variations: Split Array Largest Sum

The problem splits `nums` into $k$ contiguous subarrays such that the largest subarray sum is minimized. While 2D Dynamic Programming solves this in $\mathcal{O}(k \cdot N^2)$, the optimal Binary Search on the Answer achieves $\mathcal{O}(N \log(\sum \text{nums}))$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem tests DP vs. Binary Search trade-offs and fractional relaxations.

---

## 1. Binary Search on Answer ($\mathcal{O}(N \log S)$) vs. Dynamic Programming ($\mathcal{O}(k N^2)$)

| Approach | Recurrence / State | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| **Dynamic Programming** | $DP[i][j] = \min_{p} \max(DP[p][j-1], \text{sum}(p \dots i))$ | $\mathcal{O}(k \cdot N^2)$ | $\mathcal{O}(k \cdot N)$ |
| **Binary Search on Answer** | Guess max sum $M \in [\max(A), \sum A]$ | $\mathcal{O}(N \log(\sum A))$ | $\mathcal{O}(1)$ |

- **Takeaway**: Always recognize when a minimax/maximin optimization problem has a monotonic feasibility predicate, allowing an exponential speedup from $\mathcal{O}(k N^2) \to \mathcal{O}(N \log S)$.

---

## Summary Matrix: Trade-offs at a Glance

| Dimension | Min Value | Max Value | Optimal Algorithm |
| :--- | :--- | :--- | :--- |
| **Search Range** | $\max(\text{nums})$ | $\sum \text{nums}$ | Binary Search on Max Subarray Sum |
| **Feasibility Pass**| Subarrays needed $\le k$ | Greedy contiguous accumulator | $\mathcal{O}(N)$ time, $\mathcal{O}(1)$ space |
""",

    "058 Minimum Number of Days to Make m Bouquets": """# 04 Interview Follow-ups & System Variations: Minimum Number of Days to Make m Bouquets

The problem finds the minimum day $D$ to make $m$ bouquets of $k$ adjacent flowers from `bloomDay`. The optimal approach uses Binary Search on the Answer in range $[\min(\text{bloomDay}), \max(\text{bloomDay})]$ in $\mathcal{O}(N \log(\max - \min))$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem tests adjacency counting, impossibility edge cases, and integer overflow on $m \times k$.

---

## 1. 64-Bit Integer Overflow in Impossibility Check

### 🛑 The Hazard
If $m = 10^5$ and $k = 10^5$, total flowers required is $m \times k = 10^{10} > 2^{31} - 1$.
- `if (m * k > n)` will overflow 32-bit signed integers and fail to return `-1`.
- **Solution**: `if ((long long)m * k > nums.size()) return -1;`

---

## 2. Greedy Adjacent Flower Counting Feasibility

```cpp
bool canMake(vector<int>& bloomDay, int m, int k, int day) {
    int bouquets = 0, consecutive = 0;
    for (int b : bloomDay) {
        if (b <= day) {
            consecutive++;
            if (consecutive == k) {
                bouquets++;
                consecutive = 0;
            }
        } else {
            consecutive = 0; // Adjacency streak broken
        }
    }
    return bouquets >= m;
}
```

---

## Summary Matrix: Trade-offs at a Glance

| Scenario | Search Range | Feasibility Check | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Standard** | $[\min(bloom), \max(bloom)]$ | Contiguous streak reset | $\mathcal{O}(N \log(\text{Range}))$ | $\mathcal{O}(1)$ |
""",

    "059 Find the Smallest Divisor Given a Threshold": """# 04 Interview Follow-ups & System Variations: Find the Smallest Divisor Given a Threshold

The problem finds the smallest positive divisor such that the sum of division results is $\le \text{threshold}$. The optimal Binary Search on the Answer runs in range $[1, \max(\text{nums})]$ in $\mathcal{O}(N \log(\max(\text{nums})))$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem reinforces integer ceiling division and monotonic step functions.

---

## 1. Monotonicity Analysis

- As divisor $D$ increases:
  $$\text{Result}(D) = \sum \lceil \text{nums}[i] / D \rceil$$
  monotonically **decreases**.
- Range: `left = 1` (maximum possible sum), `right = max(nums)` (minimum possible sum = $N$).

---

## Summary Matrix: Trade-offs at a Glance

| Range | Feasibility Formula | Time | Space |
| :--- | :--- | :--- | :--- |
| $[1, \max(\text{nums})]$ | $\sum (x + d - 1) / d \le \text{threshold}$ | $\mathcal{O}(N \log(\max A))$ | $\mathcal{O}(1)$ |
""",

    "060 Aggressive Cows": """# 04 Interview Follow-ups & System Variations: Aggressive Cows

The problem places $C$ cows into $N$ stalls such that the minimum distance between any two cows is maximized. The optimal approach sorts the stall coordinates and uses **Binary Search on the Answer (Max-Min Distance)** in $\mathcal{O}(N \log(\text{stalls}[N-1] - \text{stalls}[0]))$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem is the foundational template for Maximize-the-Minimum placement constraints.

---

## 1. Why Sort Stalls First?

### 💡 Greedy Nearest-Neighbor Placement
- In an unsorted array of positions, checking distance feasibility requires combinatorial search.
- Once sorted, the optimal greedy strategy to place cows with at least distance $D$ is:
  1. Always place the 1st cow at `stalls[0]`.
  2. Place the next cow at the first stall `stalls[i]` where $\text{stalls}[i] - \text{last\_stall} \ge D$.
  3. If $\ge C$ cows can be placed, distance $D$ is feasible.

---

## Summary Matrix: Trade-offs at a Glance

| Parameter | Value |
| :--- | :--- |
| **Search Space** | $[1, \text{stalls}[N-1] - \text{stalls}[0]]$ |
| **Feasibility Test** | Greedy placement from stall 0 in $\mathcal{O}(N)$ |
| **Time Complexity** | $\mathcal{O}(N \log N + N \log(\text{Range}))$ |
| **Space Complexity** | $\mathcal{O}(1)$ / $\mathcal{O}(\log N)$ sort space |
""",

    "061 Book Allocation Problem": """# 04 Interview Follow-ups & System Variations: Book Allocation Problem

The problem allocates $N$ books to $M$ students such that the maximum pages assigned to a student is minimized (books must be allocated in contiguous order). The optimal Binary Search on the Answer achieves $\mathcal{O}(N \log(\sum \text{pages}))$ time and $\mathcal{O}(1)$ space.

In technical interviews, this is the classic Indian campus placement / FAANG interview benchmark.

---

## 1. Boundary & Impossibility Conditions

1. **If $M > N$ (Students > Books)**:
   - Each student must receive at least 1 book; impossible $\implies$ return `-1`.
2. **Lower Bound**: `max(pages)` (one student must receive the largest book).
3. **Upper Bound**: `sum(pages)` (all books given to 1 student).

---

## Summary Matrix: Trade-offs at a Glance

| Feature | Details |
| :--- | :--- |
| **Problem Type** | Minimax Contiguous Allocation |
| **Search Space** | $[\max(\text{pages}), \sum \text{pages}]$ |
| **Time Complexity** | $\mathcal{O}(N \log(\sum P))$ |
| **Space Complexity** | $\mathcal{O}(1)$ |
""",

    "062 Painter's Partition Problem": """# 04 Interview Follow-ups & System Variations: Painter's Partition Problem

The problem partitions $N$ boards of lengths `boards[i]` among $K$ painters such that the total time taken is minimized (each unit length takes $T$ units of time). The optimal approach runs Binary Search on the Answer in $\mathcal{O}(N \log(\sum \text{boards}))$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem highlights multiplier factoring to prevent intermediate arithmetic overflow.

---

## 1. The Multiplier Optimization: Factoring Out Unit Time $T$

### 🛑 Potential 64-Bit Overflow
If board lengths are $10^9$ and $T = 10^9$, multiplying by $T$ inside the binary search loop causes values to reach $10^{18}$, risking arithmetic overflow.

### 💡 Factor $T$ Out
- Run the binary search entirely on **raw board units**: Find `min_board_units`.
- Multiply by $T$ (and apply modulo if required) **only once at the very end**:
  $$\text{Total Time} = (\text{min\_board\_units} \times T) \pmod M$$

---

## Summary Matrix: Trade-offs at a Glance

| Parameter | Value |
| :--- | :--- |
| **Search Space** | $[\max(\text{boards}), \sum \text{boards}]$ |
| **Time Multiplier** | Factor out $T$ until final return |
| **Time Complexity** | $\mathcal{O}(N \log(\sum B))$ |
| **Space Complexity** | $\mathcal{O}(1)$ |
""",

    "063 Median of Two Sorted Arrays": """# 04 Interview Follow-ups & System Variations: Median of Two Sorted Arrays

The problem finds the median of two sorted arrays of sizes $M$ and $N$ in $\mathcal{O}(\log(\min(M, N)))$ time and $\mathcal{O}(1)$ space.

In top-tier technical interviews (FAANG Hard), this is considered the definitive binary search mastery test. Interviewers probe partition equations, infinite boundary guards, and distributed multi-machine medians.

---

## 1. The Dual Partitioning Equation

### 💡 The Balance Invariant
- Let the total combined elements in the left half be:
  $$\text{left\_half\_size} = \frac{M + N + 1}{2}$$
- Binary search for partition point $P_1 \in [0, M]$ in the smaller array `nums1`.
- The partition point $P_2$ in `nums2` is strictly determined:
  $$P_2 = \text{left\_half\_size} - P_1$$
- Define the 4 boundary elements:
  - $L_1 = (P_1 == 0) \;?\; -\infty : \text{nums1}[P_1 - 1]$
  - $R_1 = (P_1 == M) \;?\; +\infty : \text{nums1}[P_1]$
  - $L_2 = (P_2 == 0) \;?\; -\infty : \text{nums2}[P_2 - 1]$
  - $R_2 = (P_2 == N) \;?\; +\infty : \text{nums2}[P_2]$
- **Valid Partition Condition**:
  $$L_1 \le R_2 \quad \text{AND} \quad L_2 \le R_1$$
- **Median Formula**:
  - If $(M + N)$ is odd: $\text{Median} = \max(L_1, L_2)$.
  - If $(M + N)$ is even: $\text{Median} = \frac{\max(L_1, L_2) + \min(R_1, R_2)}{2.0}$.

---

## 2. Why Always Binary Search on the SMALLER Array?

### 💡 2 Critical Benefits
1. **Guaranteed Valid $P_2$ Bounds**: Because $M \le N$, $P_2 = \frac{M + N + 1}{2} - P_1$ is guaranteed to stay within valid range $[0, N]$.
2. **Minimal Time Complexity**: $\mathcal{O}(\log(\min(M, N)))$. If $M = 10$ and $N = 10^9$, the search finishes in $\log_2(10) \approx 4$ iterations!

---

## Summary Matrix: Trade-offs at a Glance

| Array Sizes | Binary Search Target | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| $M \le N$ | Smaller array ($M$) | $\mathcal{O}(\log(\min(M, N)))$ | $\mathcal{O}(1)$ |
| $M \gg N$ | Swap arrays $\implies$ Search $N$ | $\mathcal{O}(\log(\min(M, N)))$ | $\mathcal{O}(1)$ |
""",

    "064 K-th Element of Two Sorted Arrays": """# 04 Interview Follow-ups & System Variations: K-th Element of Two Sorted Arrays

The problem finds the $k$-th smallest element in two sorted arrays of sizes $M$ and $N$. The optimal approach uses Binary Search Partitioning in $\mathcal{O}(\log(\min(M, N)))$ or recursive $k/2$ elimination in $\mathcal{O}(\log k)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem is the generalization of the Median problem.

---

## 1. Dual Partitioning with Target Rank $k$

### 💡 Search Space Bounds
- When searching for rank $k$, partition $P_1$ cannot exceed $k$ or $M$, and cannot be smaller than $\max(0, k - N)$:
  $$\text{low} = \max(0, k - N), \quad \text{high} = \min(k, M)$$
  $$P_2 = k - P_1$$
- Invariant: $L_1 \le R_2$ and $L_2 \le R_1 \implies \text{Result} = \max(L_1, L_2)$.

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Invariant | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| **Binary Search Partition** | $P_1 + P_2 = k$ | $\mathcal{O}(\log(\min(M, N)))$ | $\mathcal{O}(1)$ |
| **Recursive $k/2$ Elimination**| Compare $\text{arr1}[k/2]$ vs $\text{arr2}[k/2]$ | $\mathcal{O}(\log k)$ | $\mathcal{O}(\log k)$ stack |
""",

    "065 Find K Closest Elements": """# 04 Interview Follow-ups & System Variations: Find K Closest Elements

The problem finds the $k$ closest integers to $x$ in a sorted array. While Two Pointers from ends runs in $\mathcal{O}(N - k)$, the optimal Binary Search for the **starting index of the window** runs in $\mathcal{O}(\log(N - k) + k)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem tests comparing window edges (`x - arr[mid]` vs `arr[mid + k] - x`) to eliminate sliding window loops.

---

## 1. Binary Search for Window Start Index ($\mathcal{O}(\log(N - k))$)

### 💡 The Edge Comparison Trick
- The target window of size $k$ must start at some index in range $[0, N - k]$.
- Binary search `mid \in [0, N - k]`:
  - Compare the distance of the element just outside the window on the right `arr[mid + k]` with the element at the left boundary `arr[mid]`:
    $$\text{if } (x - \text{arr}[mid] > \text{arr}[mid + k] - x) \implies \text{left} = \text{mid} + 1$$
    $$\text{else} \implies \text{right} = \text{mid}$$
- **Result**: `left` is the optimal start index of the $k$-element window.

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Strategy | Time Complexity | Space |
| :--- | :--- | :--- | :--- |
| **Two Pointers from Ends** | Shrink $N \to k$ by removing farthest | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **BS for Window Start (Optimal)**| Compare `arr[mid]` vs `arr[mid + k]` | $\mathcal{O}(\log(N - k) + k)$ | $\mathcal{O}(1)$ |
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
