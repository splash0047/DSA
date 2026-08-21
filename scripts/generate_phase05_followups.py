import os

BASE_DIR = r"c:\Users\Pinak chimurkar\DSA\Phase 05 Stack & Queue"

data = {
    "084 Valid Parentheses": """# 04 Interview Follow-ups & System Variations: Valid Parentheses

The problem determines if a bracket string is valid. The standard Stack solution pushes open brackets and matches closing brackets in $\mathcal{O}(N)$ time and $\mathcal{O}(N)$ space.

In technical interviews, this problem is extended to wildcards (`*`), 1-way streams with bounded memory, Longest Valid Parentheses, and custom bracket matching rules.

---

## 1. What if the String Contains Wildcards `*` (LeetCode #678: Valid Parenthesis String)?

### 🛑 Why a Standard Stack Fails
A wildcard `'*'` can act as `'('`, `')'`, or an empty string `""`. A single stack cannot branch on all 3 possibilities without exponential $\mathcal{O}(3^N)$ backtracking.

### 💡 Two-Counter Greedy Range `[min_open, max_open]`
- Maintain the range of possible open bracket counts:
  - If `c == '('`: `min_open++`, `max_open++`.
  - If `c == ')'`: `min_open = max(0, min_open - 1)`, `max_open--`.
  - If `c == '*'`: `min_open = max(0, min_open - 1)` (treated as `)`), `max_open++` (treated as `(`).
- If `max_open < 0`: Too many closing brackets $\implies$ return `false`.
- At the end, return `min_open == 0`.
- **Time Complexity**: $\mathcal{O}(N)$, **Space Complexity**: strictly $\mathcal{O}(1)$!

---

## 2. Generalization: Longest Valid Parentheses (LeetCode #32 / Hard)

### 💡 2-Pass $\mathcal{O}(1)$ Space Counter Method
1. **Left-to-Right Pass**:
   - Maintain `left_count` and `right_count`.
   - If `left == right`: `max_len = max(max_len, 2 * right)`.
   - If `right > left`: reset `left = right = 0`.
2. **Right-to-Left Pass**:
   - Same logic in reverse (resets when `left > right`).
- **Time Complexity**: $\mathcal{O}(N)$, **Space Complexity**: strictly $\mathcal{O}(1)$.

---

## 3. What if Bracket Stream is 10GB Long Over a Network Socket?

### 🛑 Memory Bound
If there are 5GB of `'('` before any `')'`, an in-memory stack will run out of memory.
- If there is only **1 bracket type** (`(` and `)`): Use a single integer counter `open_count` in $\mathcal{O}(1)$ RAM.
- If there are **multiple bracket types**: Spill stack frames to disk in 64MB blocks or reject inputs exceeding maximum nesting depth quota.

---

## Summary Matrix: Trade-offs at a Glance

| Variation | Bracket Types | Strategy | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Standard Parentheses** | `()`, `{}`, `[]` | Character Stack | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| **Single Type Stream** | `()` only | Single integer counter | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Wildcards `*` (#678)** | `()`, `*` | `[min_open, max_open]` Range | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Longest Valid (#32)** | `()` only | 2-Pass Left/Right Counters | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
""",

    "085 Min Stack": """# 04 Interview Follow-ups & System Variations: Min Stack

The Min Stack problem designs a stack supporting `push`, `pop`, `top`, and `getMin` in strictly $\mathcal{O}(1)$ time. Standard implementations use Two Stacks ($\mathcal{O}(N)$ space) or Single Stack with Math Encoding ($2x - \text{min}$).

In technical interviews, interviewers test math encoding proofs, 64-bit integer overflow protection, and Max Stack with $\mathcal{O}(\log N)$ `popMax`.

---

## 1. Mathematical Derivation: Single Stack with Math Encoding ($\mathcal{O}(1)$ Extra Space)

### 💡 Encoding Formula
- Let `min_val` be the current minimum.
- When pushing $x$:
  - If $x \ge \text{min\_val}$: Push $x$ directly.
  - If $x < \text{min\_val}$: Push encoded value $E = 2x - \text{min\_val}$ and update $\text{min\_val} = x$.
  - *Proof that $E < x$*: Since $x < \text{min\_val}$, $x - \text{min\_val} < 0 \implies 2x - \text{min\_val} < x$. The encoded value is strictly smaller than the new minimum!
- When popping:
  - If `stack.top() < min_val`: The original minimum was $\text{old\_min} = 2 \times \text{min\_val} - \text{stack.top()}$. Restore $\text{min\_val} = \text{old\_min}$.

### 🛑 64-Bit Integer Overflow Safeguard
$2x - \text{min\_val}$ can overflow 32-bit signed integers if $x = -2 \times 10^9$.
- Always use `long long` for the underlying stack.

---

## 2. Generalization: Max Stack with `popMax()` (LeetCode #716)

### 💡 Doubly Linked List + Balanced BST (`std::map`)
- To support `popMax()` in $\mathcal{O}(\log N)$ while keeping `push`, `pop`, `top`, `peekMax` in $\mathcal{O}(\log N)$ or $\mathcal{O}(1)$:
  - Maintain a **Doubly Linked List** of values (for stack order).
  - Maintain a **`map<int, vector<Node*>>`** (for quick access to maximum values).
  - When `popMax()` is called: Erase maximum entry from map, and unlink node from DLL in $\mathcal{O}(1)$.

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Push / Pop | GetMin | Extra Memory Overhead |
| :--- | :--- | :--- | :--- |
| **Two Stacks** | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | $2N$ stack entries |
| **Value-Min Pair Stack** | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | $2N$ integers |
| **Math Encoding ($2x - \text{min}$)**| $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | **$N$ 64-bit integers (Lowest memory)** |
| **Max Stack (`popMax`)** | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ | DLL + TreeMap ($\mathcal{O}(N)$) |
""",

    "086 Evaluate Reverse Polish Notation": """# 04 Interview Follow-ups & System Variations: Evaluate Reverse Polish Notation

The problem evaluates an arithmetic expression in Reverse Polish Notation (Postfix). The optimal stack-based approach runs in $\mathcal{O}(N)$ time and $\mathcal{O}(N)$ space.

In technical interviews, this problem is compared with Infix-to-Postfix conversion (Dijkstra's Shunting-Yard Algorithm), integer truncation quirks across languages, and AST Expression Tree parsing.

---

## 1. The Integer Truncation Towards Zero Bug (C++ vs. Python)

### 🛑 The Hazard of `//` in Python
In Python, `//` performs **floor division** (rounds towards $-\infty$):
- `-3 // 2 = -2` in Python.
- But RPN specifications require **truncating towards zero**: $-3 / 2 = -1$.
- **Python Fix**: Use `int(a / b)` or `math.trunc(a / b)`.
- In C++ and Java, `/` natively truncates towards zero.

---

## 2. Infix to Postfix Conversion: Dijkstra's Shunting-Yard Algorithm

### 💡 Operator Precedence Stack
- Operands go directly to output queue.
- Operators $\in \{+, -, \times, /\}$:
  - While top of operator stack has $\ge$ precedence, pop to output.
  - Push current operator.
- `'('`: Push to stack; `')'`: Pop operators to output until `'('` is reached.

---

## Summary Matrix: Trade-offs at a Glance

| Expression Form | Evaluation Method | Time | Space |
| :--- | :--- | :--- | :--- |
| **Postfix (RPN)** | Single Operand Stack | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| **Infix (Standard)** | Shunting-Yard Algorithm | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| **Prefix (Polish)** | Right-to-Left Stack Scan | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
""",

    "087 Daily Temperatures": """# 04 Interview Follow-ups & System Variations: Daily Temperatures

The problem finds the number of days you have to wait after the $i$-th day to get a warmer temperature. The optimal approach uses a **Monotonic Decreasing Stack** in $\mathcal{O}(N)$ time and $\mathcal{O}(N)$ space.

In technical interviews, this problem is the foundational entry point to Monotonic Stack patterns, eliminating dynamic stack memory allocations, and streaming temperatures.

---

## 1. High-Performance Optimization: Array-Backed Stack

### 🛑 `std::stack` Deque Overhead
In C++, `std::stack<int>` wraps `std::deque`, causing block allocations.

### 💡 Flat Array Stack
```cpp
vector<int> dailyTemperatures(vector<int>& temperatures) {
    int n = temperatures.size();
    vector<int> ans(n, 0);
    vector<int> stk(n);
    int top = -1;
    
    for (int i = 0; i < n; i++) {
        while (top >= 0 && temperatures[i] > temperatures[stk[top]]) {
            int prev_idx = stk[top--];
            ans[prev_idx] = i - prev_idx;
        }
        stk[++top] = i;
    }
    return ans;
}
```
- **Performance**: Runs in pure contiguous memory with 0 heap fragmentations.

---

## 2. 1-Billion Temperature Readings Stream on Disk

### 💡 Chunked Monotonic Spill Stack
- As temperature records stream from disk, maintain the monotonic stack in RAM.
- Stack entries only persist until their warmer day arrives; in typical weather patterns, stack size stays small ($< 100$ entries).

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Data Structure | Time Complexity | Cache Locality |
| :--- | :--- | :--- | :--- |
| **Standard Stack** | `std::stack<int>` | $\mathcal{O}(N)$ | Moderate |
| **Flat Array Stack**| `vector<int>` with `top` index | $\mathcal{O}(N)$ | **Optimal (L1 Cache)** |
""",

    "088 Next Greater Element I": """# 04 Interview Follow-ups & System Variations: Next Greater Element I

The problem finds the Next Greater Element for elements of `nums1` in `nums2`. The optimal approach preprocesses `nums2` using a **Monotonic Decreasing Stack** and stores results in a **Hash Map** in $\mathcal{O}(|nums1| + |nums2|)$ time and $\mathcal{O}(|nums2|)$ space.

In technical interviews, this problem tests monotonic lookup tables and generalized range queries.

---

## 1. Monotonic Stack + Hash Map Architecture

```cpp
vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
    unordered_map<int, int> next_greater;
    vector<int> stk;
    
    for (int x : nums2) {
        while (!stk.empty() && x > stk.back()) {
            next_greater[stk.back()] = x;
            stk.pop_back();
        }
        stk.push_back(x);
    }
    
    vector<int> ans;
    for (int x : nums1) {
        ans.push_back(next_greater.count(x) ? next_greater[x] : -1);
    }
    return ans;
}
```

---

## Summary Matrix: Trade-offs at a Glance

| Phase | Strategy | Time | Space |
| :--- | :--- | :--- | :--- |
| **Preprocessing `nums2`** | Monotonic Decreasing Stack | $\mathcal{O}(|nums2|)$ | $\mathcal{O}(|nums2|)$ |
| **Querying `nums1`** | Hash Map Lookup | $\mathcal{O}(|nums1|)$ | $\mathcal{O}(1)$ auxiliary |
""",

    "089 Next Greater Element II": """# 04 Interview Follow-ups & System Variations: Next Greater Element II

The problem finds the next greater element in a **Circular Array**. The optimal approach iterates through the array twice ($2N$ steps) using modulo indexing `i % n` with a Monotonic Decreasing Stack in $\mathcal{O}(N)$ time and $\mathcal{O}(N)$ space.

In technical interviews, this problem tests virtual array unrolling and circular boundary invariants.

---

## 1. The $2N$ Virtual Unrolling Pattern

### 💡 Why $2N - 1$ Steps Suffice
- In a circular array of size $N$, every element can look ahead at most $N - 1$ positions.
- Looping $i$ from $0$ to $2N - 1$ simulates traversing the array concatenated with itself `nums + nums`.
- Only push to stack during the first pass ($i < N$); the second pass serves only to resolve unresolved elements remaining in the stack.

---

## Summary Matrix: Trade-offs at a Glance

| Variation | Traversal Range | Time | Space |
| :--- | :--- | :--- | :--- |
| **Linear Array (I)** | $0 \dots N-1$ | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| **Circular Array (II)**| $0 \dots 2N-1$ via `i % n` | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
""",

    "090 Largest Rectangle in Histogram": """# 04 Interview Follow-ups & System Variations: Largest Rectangle in Histogram

The problem finds the area of the largest rectangle in a histogram (Hard). The optimal solution uses a **Monotonic Increasing Stack** in $\mathcal{O}(N)$ time and $\mathcal{O}(N)$ space.

In top-tier technical interviews, this is considered a premier algorithmic challenge. Interviewers probe boundary sentinels, width calculation derivations, and Divide & Conquer Segment Tree alternatives.

---

## 1. Derivation of Width: Why `i - stack.top() - 1`?

### 💡 The Geometric Invariant
- When a bar at `stack.top()` is popped because `heights[i] < heights[popped]`:
  - `heights[i]` is the **Right Smaller Boundary** (first bar to the right shorter than `heights[popped]`).
  - The new `stack.top()` (after popping) is the **Left Smaller Boundary** (first bar to the left shorter than `heights[popped]`).
- The rectangle bounded by `heights[popped]` extends between `left_boundary` and `right_boundary`:
  $$\text{Width} = (\text{right} - 1) - (\text{left}) = i - \text{stack.top()} - 1$$
- If stack is empty after popping: The popped bar is the smallest bar seen so far $\implies \text{Width} = i$.

---

## 2. Clean Sentinel Flush Optimization

### 💡 Adding a Trailing `0` Height
- By appending a sentinel height `0` to the histogram, all remaining bars in the stack are automatically popped and evaluated without needing post-loop cleanup code.

---

## 3. Alternative: Divide & Conquer with Segment Tree (RMQ)

### 💡 Range Minimum Query Approach
- The largest rectangle in range $[L, R]$ is:
  $$\max\Big(\text{height}[min\_idx] \times (R - L + 1),\; \text{Solve}(L, min\_idx - 1),\; \text{Solve}(min\_idx + 1, R)\Big)$$
- Precomputing Range Minimum Query via Segment Tree: $\mathcal{O}(N \log N)$ average time, $\mathcal{O}(N^2)$ worst case on skewed histograms.
- Monotonic stack is strictly superior ($\mathcal{O}(N)$ worst case).

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Worst-Case Time | Space | Complexity |
| :--- | :--- | :--- | :--- |
| **Monotonic Stack (Optimal)**| $\mathcal{O}(N)$ strictly | $\mathcal{O}(N)$ | 1 linear pass |
| **Segment Tree RMQ** | $\mathcal{O}(N^2)$ worst / $\mathcal{O}(N \log N)$ avg | $\mathcal{O}(N)$ | Tree construction |
""",

    "091 Maximal Rectangle": """# 04 Interview Follow-ups & System Variations: Maximal Rectangle

The problem finds the largest rectangle containing only `1`s in a 2D binary matrix (Hard). The optimal approach transforms the matrix row-by-row into a dynamic Histogram and runs the **Largest Rectangle in Histogram** algorithm on each row in $\mathcal{O}(R \times C)$ time and $\mathcal{O}(C)$ space.

In technical interviews, this problem is compared with Maximal Square and 2D Dynamic Programming.

---

## 1. 2D-to-1D Histogram Row Reduction

### 💡 Row-by-Row Height Accumulation
- Maintain a 1D array `heights[C]`.
- For each row $r \in [0, R - 1]$:
  - For each column $c$: `heights[c] = (matrix[r][c] == '1') ? heights[c] + 1 : 0;`
  - Compute largest rectangle for `heights` in $\mathcal{O}(C)$ using Monotonic Stack.
- **Total Time Complexity**: $R \times \mathcal{O}(C) = \mathcal{O}(R \times C)$.
- **Total Space Complexity**: $\mathcal{O}(C)$.

---

## 2. Maximal Rectangle vs. Maximal Square (LeetCode #221)

| Problem | Shape Constraint | Optimal Technique | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Maximal Rectangle (#85)**| Arbitrary width/height | Row Histogram + Monotonic Stack | $\mathcal{O}(R \times C)$ | $\mathcal{O}(C)$ |
| **Maximal Square (#221)** | Width == Height | 2D DP: $DP[i][j] = 1 + \min(top, left, diag)$ | $\mathcal{O}(R \times C)$ | $\mathcal{O}(C)$ |

---

## Summary Matrix: Trade-offs at a Glance

| Dimension | Strategy | Time | Space |
| :--- | :--- | :--- | :--- |
| **Maximal Rectangle** | Row-wise Histogram + Monotonic Stack | $\mathcal{O}(R \times C)$ | $\mathcal{O}(C)$ |
| **Dynamic Programming**| Track `left`, `right`, `height` per cell | $\mathcal{O}(R \times C)$ | $\mathcal{O}(C)$ |
""",

    "092 Online Stock Span": """# 04 Interview Follow-ups & System Variations: Online Stock Span

The problem calculates the span of a stock's price today (maximum consecutive days price was $\le$ today's price). The optimal solution uses a **Monotonic Decreasing Stack of Pairs** `(price, span)` in $\mathcal{O}(1)$ amortized time per call and $\mathcal{O}(N)$ space.

In technical interviews, this problem tests formal amortized complexity proofs and memory-bounded streaming.

---

## 1. Mathematical Proof of $\mathcal{O}(1)$ Amortized Complexity

### 💡 The Accounting Aggregate Method
- Each price is pushed onto the stack **at most once**.
- Each price is popped from the stack **at most once** across the entire lifetime of the data stream.
- For $N$ total calls to `next(price)`:
  $$\text{Total Pushes} \le N, \quad \text{Total Pops} \le N$$
  $$\text{Total Operations} \le 2N$$
- **Amortized Time per Call**: $\frac{2N}{N} = \mathcal{O}(1)$ constant time.

---

## 2. Span Compression in Stack Nodes

```cpp
class StockSpanner {
    stack<pair<int, int>> stk; // {price, span}
public:
    int next(int price) {
        int span = 1;
        while (!stk.empty() && stk.top().first <= price) {
            span += stk.top().second;
            stk.pop(); // Compress past spans
        }
        stk.push({price, span});
        return span;
    }
};
```

---

## Summary Matrix: Trade-offs at a Glance

| Operation | Amortized Time | Worst-Case Single Call | Space |
| :--- | :--- | :--- | :--- |
| `next(price)` | $\mathcal{O}(1)$ | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
""",

    "093 Trapping Rain Water": """# 04 Interview Follow-ups & System Variations: Trapping Rain Water

The problem computes how much water elevation map can trap after raining (Hard). Optimal solutions include **Two Pointers** ($\mathcal{O}(N)$ time, $\mathcal{O}(1)$ space), **Monotonic Decreasing Stack** ($\mathcal{O}(N)$ space), and **Dynamic Programming** ($\mathcal{O}(N)$ space).

In technical interviews, this is one of the most famous problems in computer science. Interviewers test 3D generalizations (Trapping Rain Water II) and real-time streaming elevation.

---

## 1. 3 Optimal Approaches Compared

| Approach | Trapping Perspective | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| **Two Pointers (Optimal)**| **Vertical Columns**: $\min(\text{LMax}, \text{RMax}) - H[i]$ | $\mathcal{O}(N)$ | **$\mathcal{O}(1)$** |
| **Dynamic Programming** | **Vertical Columns**: Precompute `left_max` & `right_max` | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| **Monotonic Stack** | **Horizontal Layers**: Bounded by popped bottom and walls | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |

---

## 2. Two-Pointer Invariant Proof ($\mathcal{O}(1)$ Space)

### 💡 Why `left_max < right_max` Guarantees Correctness
- If `left_max < right_max`, the water trapped at `left` is **strictly bottlenecked by `left_max`**, regardless of what unknown heights lie between `left` and `right`.
- Water trapped at `left` is simply $\text{left\_max} - \text{height}[\text{left}]$. Advance `left++`.

---

## 3. Generalization: Trapping Rain Water II (3D Terrain / LeetCode #407)

### 💡 Min-Heap Priority Queue BFS
- In a 3D terrain $R \times C$, water spills outwards towards the boundary.
- **Algorithm**:
  1. Push all boundary cells into a **Min-Heap** `(height, r, c)` and mark as visited.
  2. Maintain `current_water_level = 0`.
  3. Pop lowest cell $(h, r, c)$ from heap. Update `current_water_level = max(current_water_level, h)`.
  4. For each unvisited neighbor:
     - Water trapped = $\max(0, \text{current\_water\_level} - \text{neighbor\_height})$.
     - Push neighbor to heap with its height.
- **Time Complexity**: $\mathcal{O}(R \cdot C \log(R \cdot C))$, **Space Complexity**: $\mathcal{O}(R \cdot C)$.

---

## Summary Matrix: Trade-offs at a Glance

| Dimension | Terrain Model | Algorithm | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **1D Array (#42)** | 2D Profile | Two Pointers | $\mathcal{O}(N)$ | strictly $\mathcal{O}(1)$ |
| **3D Grid (#407)** | 3D Elevation | Min-Heap Priority Queue BFS | $\mathcal{O}(RC \log(RC))$ | $\mathcal{O}(RC)$ |
""",

    "094 Asteroid Collision": """# 04 Interview Follow-ups & System Variations: Asteroid Collision

The problem finds the state of asteroids after all collisions (positive = moving right, negative = moving left). The optimal solution uses a **Stack** in $\mathcal{O}(N)$ time and $\mathcal{O}(N)$ space.

In technical interviews, this problem tests collision logic isolation, annihilation edge cases, and variable speed physical simulations.

---

## 1. Collision Decision Matrix

- Collision happens **IF AND ONLY IF**: `stack.top() > 0` (moving right) AND `current < 0` (moving left).
- **All other combinations never collide**:
  - Positive followed by Positive ($+ \to +$): Moving same direction.
  - Negative followed by Negative ($-\to -$): Moving same direction.
  - Negative followed by Positive ($-\to +$): Moving away from each other.

---

## Summary Matrix: Trade-offs at a Glance

| Collision Case | Condition | Outcome |
| :--- | :--- | :--- |
| **Top Wins** | `abs(top) > abs(curr)` | `curr` destroyed; top survives |
| **Current Wins** | `abs(top) < abs(curr)` | `top` destroyed; re-check new top |
| **Mutual Annihilation**| `abs(top) == abs(curr)`| Both destroyed |
""",

    "095 Basic Calculator II": """# 04 Interview Follow-ups & System Variations: Basic Calculator II

The problem evaluates an arithmetic expression containing non-negative integers, `+`, `-`, `*`, `/` and spaces without parentheses. While a Stack achieves $\mathcal{O}(N)$ space, the optimal approach uses **Two Running Scalars** (`last_num` and `running_sum`) in $\mathcal{O}(N)$ time and strictly $\mathcal{O}(1)$ space.

In technical interviews, this problem is extended to nested parentheses and full Recursive Descent Parsers (Basic Calculator III).

---

## 1. Low-Memory Optimization: Eliminating the Stack ($\mathcal{O}(1)$ Space)

### 💡 Running Precedence Accumulator
```cpp
int calculate(string s) {
    long long running_sum = 0, last_num = 0, current_num = 0;
    char op = '+';
    
    for (int i = 0; i < s.size(); i++) {
        if (isdigit(s[i])) {
            current_num = current_num * 10 + (s[i] - '0');
        }
        if ((!isdigit(s[i]) && s[i] != ' ') || i == s.size() - 1) {
            if (op == '+') {
                running_sum += last_num;
                last_num = current_num;
            } else if (op == '-') {
                running_sum += last_num;
                last_num = -current_num;
            } else if (op == '*') {
                last_num = last_num * current_num;
            } else if (op == '/') {
                last_num = last_num / current_num;
            }
            op = s[i];
            current_num = 0;
        }
    }
    return running_sum + last_num;
}
```

---

## 2. Generalization: Basic Calculator III (With Parentheses `()`)

### 💡 Recursive Descent Parser
- Whenever encountering `'('`, recursively call `calculate(s)` starting from the inner expression.
- Return the sub-result when encountering `')'`.
- **Time Complexity**: $\mathcal{O}(N)$, **Space Complexity**: $\mathcal{O}(D)$ recursion depth.

---

## Summary Matrix: Trade-offs at a Glance

| Calculator Level | Features | Optimal Approach | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Basic Calculator II (#227)** | `+`, `-`, `*`, `/` | 2 Running Scalars (`last_num`) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Basic Calculator I (#224)** | `+`, `-`, `()` | Sign Stack | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| **Basic Calculator III (#772)**| `+`, `-`, `*`, `/`, `()`| Recursive Descent Parser | $\mathcal{O}(N)$ | $\mathcal{O}(D)$ |
""",

    "096 Implement Queue using Stacks": """# 04 Interview Follow-ups & System Variations: Implement Queue using Stacks

The problem implements a FIFO Queue using two LIFO Stacks (`in_stack` and `out_stack`). Pushes take $\mathcal{O}(1)$ and pops take $\mathcal{O}(1)$ amortized time with $\mathcal{O}(N)$ space.

In technical interviews, this problem tests amortized complexity proofs and multi-threaded lock decoupling.

---

## 1. Amortized $\mathcal{O}(1)$ Time Complexity Proof

### 💡 Lazy Transfer Invariant
- Elements are pushed directly to `in_stack` in $\mathcal{O}(1)$.
- When `pop()` or `peek()` is called:
  - If `out_stack` is not empty: Pop directly from `out_stack` in $\mathcal{O}(1)$.
  - If `out_stack` is empty: Transfer **all** elements from `in_stack` to `out_stack`.
- **Amortized Analysis**: Each element is pushed to `in_stack` once, transferred to `out_stack` once, and popped from `out_stack` once $\implies$ exactly 3 operations per element over its entire lifetime.
- Average cost per operation is $\mathcal{O}(1)$.

---

## 2. Thread-Safe Concurrency Optimization

### 💡 Lock Decoupling (Two Mutexes)
- Since `push()` only interacts with `in_stack` and `pop()` primarily interacts with `out_stack`, a producer thread and consumer thread can operate concurrently using separate locks on each stack without blocking each other (except during empty-transfer phase).

---

## Summary Matrix: Trade-offs at a Glance

| Operation | Amortized Time | Worst-Case Single Call | Space |
| :--- | :--- | :--- | :--- |
| `push(x)` | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | $\mathcal{O}(N)$ |
| `pop()` | $\mathcal{O}(1)$ | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ auxiliary |
| `peek()` | $\mathcal{O}(1)$ | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ auxiliary |
""",

    "097 Implement Stack using Queues": """# 04 Interview Follow-ups & System Variations: Implement Stack using Queues

The problem implements a LIFO Stack using FIFO Queues. Optimal approaches use 1 Queue (rotating elements on push) in $\mathcal{O}(N)$ push and $\mathcal{O}(1)$ pop, or 2 Queues.

In technical interviews, this problem is contrasted with Queue using Stacks to demonstrate why no amortized $\mathcal{O}(1)$ pop exists for Queues.

---

## 1. Single Queue Implementation (Push Rotation)

```cpp
class MyStack {
    queue<int> q;
public:
    void push(int x) {
        q.push(x);
        int sz = q.size();
        for (int i = 0; i < sz - 1; i++) {
            q.push(q.front());
            q.pop(); // Rotate old elements behind the new top
        }
    }
    int pop() { int v = q.front(); q.pop(); return v; }
    int top() { return q.front(); }
    bool empty() { return q.empty(); }
};
```

---

## Summary Matrix: Trade-offs at a Glance

| Design | Push Time | Pop Time | Top Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Push-Costly (1 Queue)**| $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | $\mathcal{O}(N)$ |
| **Pop-Costly (2 Queues)** | $\mathcal{O}(1)$ | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
""",

    "098 Sliding Window Maximum": """# 04 Interview Follow-ups & System Variations: Sliding Window Maximum

The problem finds the maximum element in each sliding window of size $k$ (Hard). The optimal solution uses a **Monotonic Decreasing Deque** in $\mathcal{O}(N)$ time and $\mathcal{O}(k)$ space.

In technical interviews, this problem is compared with Block Decomposition (Two-Pass Prefix/Suffix Max with $\mathcal{O}(1)$ space) and Sliding Window Median (Two Heaps).

---

## 1. Monotonic Deque Invariant ($\mathcal{O}(N)$ Strict)

### 💡 Deque Maintenance Rules
1. **Evict Out-of-Window Elements**: If `deque.front() <= i - k`, pop front.
2. **Maintain Monotonic Decreasing Order**: While `!deque.empty() && nums[deque.back()] <= nums[i]`, pop back.
3. Push current index `i` to back.
4. If $i \ge k - 1$, record maximum `nums[deque.front()]`.
- **Amortized Proof**: Each index is pushed and popped at most once $\implies \mathcal{O}(N)$ total operations.

---

## 2. Block Decomposition: Prefix/Suffix Max ($\mathcal{O}(1)$ Auxiliary Space)

### 💡 Two-Pass Array Method
1. Divide array into blocks of size $k$.
2. Precompute `left_max[i]` (max from start of block to $i$) and `right_max[i]` (max from end of block to $i$).
3. Sliding window max for range $[i, i + k - 1]$ is simply:
   $$\max\Big(\text{right\_max}[i],\; \text{left\_max}[i + k - 1]\Big)$$
- **Query Time**: strictly $\mathcal{O}(1)$ with zero deques!

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Data Structure | Time | Space |
| :--- | :--- | :--- | :--- |
| **Monotonic Deque (Optimal)**| `std::deque<int>` | $\mathcal{O}(N)$ | $\mathcal{O}(k)$ |
| **Block Prefix/Suffix Max** | Flat arrays | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ or $\mathcal{O}(1)$ in-place |
| **Max-Heap (Priority Queue)**| `priority_queue<pair<int, int>>` | $\mathcal{O}(N \log N)$ | $\mathcal{O}(N)$ |
""",

    "099 Task Scheduler": """# 04 Interview Follow-ups & System Variations: Task Scheduler

The problem finds the minimum CPU intervals to execute all tasks with a cooldown period $n$ between identical tasks. The optimal greedy mathematical formula calculates the answer in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ auxiliary space.

In technical interviews, this problem tests idle slot math derivations, Max-Heap simulation, and Earliest Deadline First (EDF) scheduling.

---

## 1. Mathematical Derivation of the $\mathcal{O}(N)$ Greedy Formula

### 💡 The Idle Frame Invariant
- Let `max_freq` be the maximum frequency of any task.
- Let `count_max_freq` be the number of distinct tasks that share this `max_freq`.
- These most frequent tasks form `max_freq - 1` empty frames of width $n + 1$, plus the final trailing task chunk:
  $$\text{Minimum Time} = (\text{max\_freq} - 1) \times (n + 1) + \text{count\_max\_freq}$$
- If the total number of tasks exceeds this frame capacity, no idle slots are required:
  $$\text{Answer} = \max(\text{tasks.size()},\; (\text{max\_freq} - 1) \times (n + 1) + \text{count\_max\_freq})$$
- **Time Complexity**: $\mathcal{O}(N)$ single pass, **Space Complexity**: $\mathcal{O}(26) = \mathcal{O}(1)$.

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Strategy | Time | Space |
| :--- | :--- | :--- | :--- |
| **Greedy Math Formula** | Frame Calculation | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Max-Heap + Cooldown Queue**| Discrete Event Simulation | $\mathcal{O}(N \log 26)$ | $\mathcal{O}(26) = \mathcal{O}(1)$ |
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
