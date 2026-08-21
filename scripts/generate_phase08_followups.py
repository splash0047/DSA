import os

BASE_DIR = r"c:\Users\Pinak chimurkar\DSA\Phase 08 Graphs"

data = {
    "123 Number of Islands": """# 04 Interview Follow-ups & System Variations: Number of Islands

The problem counts the number of disconnected islands in a 2D binary grid. Optimal solutions include **DFS Flood Fill** / **BFS** in $\mathcal{O}(M \times N)$ time and $\mathcal{O}(M \times N)$ space (or in-place cell mutation for $\mathcal{O}(1)$ auxiliary space), or **Disjoint Set Union (DSU)**.

In top-tier technical interviews, this is the archetypal grid connectivity problem. Interviewers probe massive grid streaming (1B cells), dynamic land additions (Number of Islands II), and distributed MapReduce graph partitioning.

---

## 1. What if the Grid Has 1 Billion Cells ($10^5 \times 10^5$) and Cannot Fit in RAM?

### 🛑 Memory Bottleneck
A $10^5 \times 10^5$ grid takes 10 GB of raw memory; in-memory DFS or BFS will trigger Out-Of-Memory (OOM).

### 💡 Row-by-Row Disjoint Set Streaming
- You only need to keep **2 rows** in memory at any given time (the `previous_row` and `current_row`).
- Maintain a **Disjoint Set Union (Union-Find)** structure for the active active land boundaries.
- As `current_row` streams in:
  - Union adjacent horizontal land cells in `current_row`.
  - Union vertical connections with `previous_row`.
  - When moving to the next row, discard nodes from the row above that have no downward connections.
- **RAM Overhead**: Strictly $\mathcal{O}(\text{Column Width})$ instead of $\mathcal{O}(R \times C)$.

---

## 2. Dynamic Land Additions: Number of Islands II (LeetCode #305)

### 🛑 The Scenario
Start with an empty $M \times N$ ocean grid. Land positions are added one by one dynamically; return the island count after each addition.

### 💡 Disjoint Set with Path Compression & Union by Rank
- Each cell $(r, c)$ has a 1D ID: $\text{id} = r \times N + c$.
- When a new land cell $(r, c)$ is added:
  - Increment `count++`.
  - Check 4 cardinal neighbors. If a neighbor is land:
    - Perform `Union(current_id, neighbor_id)`.
    - If they were in different sets, decrement `count--`.
- **Time Complexity**: $\mathcal{O}(K \times \alpha(M \times N))$ where $K$ is number of additions and $\alpha$ is the Inverse Ackermann function ($\approx \mathcal{O}(1)$).

---

## Summary Matrix: Trade-offs at a Glance

| Variation | Grid Model | Optimal Algorithm | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Static Grid** | In-Memory | DFS / BFS Flood Fill | $\mathcal{O}(MN)$ | $\mathcal{O}(MN)$ stack / queue |
| **Massive Grid** | 2-Row Stream | 2-Row Disjoint Set (DSU) | $\mathcal{O}(MN \alpha(N))$ | $\mathcal{O}(N)$ RAM |
| **Dynamic Land (#305)**| Point Additions | Disjoint Set with Path Compression | $\mathcal{O}(K \alpha(MN))$ | $\mathcal{O}(MN)$ DSU |
""",

    "124 Max Area of Island": """# 04 Interview Follow-ups & System Variations: Max Area of Island

The problem finds the maximum area of a connected island in a 2D binary matrix. Optimal solutions include **Recursive DFS** or **Iterative BFS** tracking component sizes in $\mathcal{O}(M \times N)$ time and $\mathcal{O}(M \times N)$ space.

In technical interviews, this problem tests call-stack safety in large connected components and component size tracking in Disjoint Set Union.

---

## 1. Preventing Stack Overflow on Massive Connected Continents

### 🛑 The Recursion Hazard
If the entire $1000 \times 1000$ grid is a single giant island of $10^6$ land cells, recursive DFS will create $10^6$ call stack frames, causing a crash.

### 💡 Iterative BFS with Queue
```cpp
int bfsArea(vector<vector<int>>& grid, int r, int c) {
    int area = 0;
    queue<pair<int, int>> q;
    q.push({r, c});
    grid[r][c] = 0; // Mark visited immediately upon enqueue!
    
    int dirs[4][2] = {{-1,0}, {1,0}, {0,-1}, {0,1}};
    while (!q.empty()) {
        auto [cr, cc] = q.front(); q.pop();
        area++;
        
        for (auto& d : dirs) {
            int nr = cr + d[0], nc = cc + d[1];
            if (nr >= 0 && nr < grid.size() && nc >= 0 && nc < grid[0].size() && grid[nr][nc] == 1) {
                grid[nr][nc] = 0; // Prevent duplicate enqueues
                q.push({nr, nc});
            }
        }
    }
    return area;
}
```

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Call Stack Safety | Time | Space |
| :--- | :--- | :--- | :--- |
| **Recursive DFS** | Unsafe on large islands | $\mathcal{O}(MN)$ | $\mathcal{O}(MN)$ stack |
| **Iterative BFS** | **Safe (Heap Queue)** | $\mathcal{O}(MN)$ | $\mathcal{O}(\min(M, N))$ queue |
| **Disjoint Set Union** | **Safe** | $\mathcal{O}(MN \alpha(MN))$ | $\mathcal{O}(MN)$ array |
""",

    "125 Clone Graph": """# 04 Interview Follow-ups & System Variations: Clone Graph

The problem creates a deep copy of a connected undirected graph where each node contains an integer value and a list of neighbor pointers. Optimal approaches include **DFS** or **BFS** with a `visited` Hash Map mapping `Node* -> Node*` in $\mathcal{O}(V + E)$ time and $\mathcal{O}(V)$ space.

In technical interviews, this problem is extended to distributed graph processing (Apache Giraph / GraphX Pregel model) and massive graph serialization.

---

## 1. Graph Cloning Template with Visited Map

```cpp
unordered_map<Node*, Node*> visited;

Node* cloneGraph(Node* node) {
    if (!node) return nullptr;
    if (visited.count(node)) return visited[node];
    
    Node* clone = new Node(node->val);
    visited[node] = clone;
    
    for (Node* neighbor : node->neighbors) {
        clone->neighbors.push_back(cloneGraph(neighbor));
    }
    return clone;
}
```

---

## 2. Distributed Scale: Cloning Graphs with 1 Billion Vertices (Pregel / Bulk Synchronous Parallel)

### 🛑 Memory & Pointer Limitations
A graph with $10^9$ vertices and $10^{11}$ edges cannot fit in a single server's RAM; pointer-based object graphs cannot cross machine boundaries.

### 💡 Vertex-Centric Message Passing (Bulk Synchronous Parallel)
1. Vertices are partitioned across cluster nodes by `hash(vertex_id) % NUM_MACHINES`.
2. **Superstep 1**: Each machine clones local vertices and broadcasts adjacency requests to remote neighbor hosts.
3. **Superstep 2**: Remote machines reply with newly minted cloned node IDs.
4. **Superstep 3**: Stitch remote edge IDs into adjacency lists without pointers.

---

## Summary Matrix: Trade-offs at a Glance

| Scenario | Strategy | Time | Space |
| :--- | :--- | :--- | :--- |
| **In-Memory Graph** | DFS / BFS with Hash Map | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ |
| **Distributed Graph** | Pregel Vertex-Centric Message Passing | $\mathcal{O}(\frac{V+E}{M})$ | $\mathcal{O}(\frac{V+E}{M})$ / node |
""",

    "126 Pacific Atlantic Water Flow": """# 04 Interview Follow-ups & System Variations: Pacific Atlantic Water Flow

The problem finds all grid coordinates where water can flow both to the Pacific Ocean (top/left) and Atlantic Ocean (bottom/right). The optimal solution runs **Reverse Graph Traversal** (flowing uphill from ocean boundaries) using 2 BFS/DFS passes in $\mathcal{O}(M \times N)$ time and $\mathcal{O}(M \times N)$ space.

In technical interviews, this problem is the prime demonstration of **Multi-Source Reverse Search** vs. naive forward simulation.

---

## 1. Why Forward Simulation is $\mathcal{O}(M^2 N^2)$ vs. Reverse Search $\mathcal{O}(MN)$

### 🛑 The Forward Simulation Pitfall
Testing water flow starting from every individual cell $(r, c)$ triggers $M \times N$ separate flood fills, taking $\mathcal{O}(M^2 N^2)$ worst-case time.

### 💡 Reverse Multi-Source Search (Uphill Flow)
- Water can only flow from $(r_1, c_1) \to (r_2, c_2)$ if $\text{height}_1 \ge \text{height}_2$.
- In reverse, water flows **uphill**: $(r_2, c_2) \to (r_1, c_1)$ if $\text{height}_1 \ge \text{height}_2$.
1. **Pacific Pass**: Start Multi-Source BFS from all Top and Left border cells. Mark reachable cells in `pacific_visited`.
2. **Atlantic Pass**: Start Multi-Source BFS from all Bottom and Right border cells. Mark reachable cells in `atlantic_visited`.
3. Cells where `pacific_visited[r][c] && atlantic_visited[r][c]` are the exact answer!
- **Time Complexity**: $2 \times \mathcal{O}(MN) = \mathcal{O}(MN)$ strictly.

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Traversal Direction | Number of Traversals | Time Complexity |
| :--- | :--- | :--- | :--- |
| **Forward Simulation** | Downhill from each cell | $M \times N$ individual searches | $\mathcal{O}(M^2 N^2)$ (Slow) |
| **Reverse Search (Optimal)**| Uphill from Oceans | Exactly 2 Multi-Source BFS | $\mathcal{O}(MN)$ (Optimal) |
""",

    "127 Surrounded Regions": """# 04 Interview Follow-ups & System Variations: Surrounded Regions

The problem captures all regions on an $M \times N$ board surrounded by `'X'` by flipping all enclosed `'O'`s to `'X'`. The optimal approach uses **Boundary-Connected Flood Fill** in $\mathcal{O}(M \times N)$ time and $\mathcal{O}(M \times N)$ space (or in-place marking with $\mathcal{O}(1)$ auxiliary space).

In technical interviews, this problem is compared with Union-Find with a Dummy Ocean Node and game board flood fills (Go game).

---

## 1. 3-Phase Boundary-Connected In-Place Marking

### 💡 Step-by-Step Algorithm
1. **Phase 1 (Mark Safe Boundary Cells)**:
   - Run DFS / BFS starting only from `'O'` cells located on the **4 outer boundaries** (Row $0$, Row $M-1$, Col $0$, Col $N-1$).
   - Temporarily mark these boundary-connected `'O'` cells as `'S'` (Safe).
2. **Phase 2 (Flip Enclosed Cells)**:
   - Iterate through entire grid: Any remaining `'O'` is completely surrounded $\implies$ flip to `'X'`.
3. **Phase 3 (Restore Safe Cells)**:
   - Flip all `'S'` cells back to `'O'`.
- **Space Complexity**: $\mathcal{O}(1)$ auxiliary memory (modifies board in-place).

---

## 2. Alternative: Disjoint Set Union with Dummy Ocean Node

### 💡 Graph Union Pattern
- Create a virtual `DUMMY_OCEAN` node (index $M \times N$).
- Connect all boundary `'O'` cells to `DUMMY_OCEAN`.
- Connect all adjacent `'O'` cells together.
- Any `'O'` whose root is NOT connected to `DUMMY_OCEAN` is surrounded $\implies$ flip to `'X'`.

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Memory Strategy | Time | Auxiliary Space |
| :--- | :--- | :--- | :--- |
| **Boundary Flood Fill** | In-Place `'S'` marking | $\mathcal{O}(MN)$ | $\mathcal{O}(1)$ auxiliary |
| **Disjoint Set Union** | `DUMMY_OCEAN` root set | $\mathcal{O}(MN \alpha(MN))$ | $\mathcal{O}(MN)$ DSU array |
""",

    "128 Rotting Oranges": """# 04 Interview Follow-ups & System Variations: Rotting Oranges

The problem finds the minimum number of minutes until no fresh orange remains in a grid. The optimal solution uses **Multi-Source BFS with Level Barriers** in $\mathcal{O}(M \times N)$ time and $\mathcal{O}(M \times N)$ space.

In technical interviews, this problem is the gold standard for Multi-Source BFS. Interviewers test why DFS fails here, unreachable island detection, and 3D warehouse extensions.

---

## 1. Why DFS Cannot Solve Rotting Oranges Directly

### 🛑 The Simulation Asymmetry
- All rotten oranges rot their adjacent fresh oranges **simultaneously in parallel** on each minute tick.
- DFS explores one single path deeply first, requiring expensive repeated minimum timestamp updates across all overlapping paths ($\mathcal{O}(MN)$ per branch).
- **Multi-Source BFS** naturally expands all rotting fronts uniformly outward in concentric 1-minute layers, guaranteeing the earliest rotting time for every orange in a single pass.

---

## 2. Multi-Source BFS Implementation Pattern

```cpp
int orangesRotting(vector<vector<int>>& grid) {
    int m = grid.size(), n = grid[0].size();
    queue<pair<int, int>> q;
    int fresh_count = 0;
    
    for (int r = 0; r < m; r++) {
        for (int c = 0; c < n; c++) {
            if (grid[r][c] == 2) q.push({r, c}); // Seed all initial rotten oranges
            else if (grid[r][c] == 1) fresh_count++;
        }
    }
    
    if (fresh_count == 0) return 0;
    
    int minutes = -1;
    int dirs[4][2] = {{-1,0}, {1,0}, {0,-1}, {0,1}};
    
    while (!q.empty()) {
        int sz = q.size();
        minutes++;
        for (int i = 0; i < sz; i++) {
            auto [cr, cc] = q.front(); q.pop();
            for (auto& d : dirs) {
                int nr = cr + d[0], nc = cc + d[1];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 1) {
                    grid[nr][nc] = 2; // Rot the fresh orange
                    fresh_count--;
                    q.push({nr, nc});
                }
            }
        }
    }
    return (fresh_count == 0) ? minutes : -1;
}
```

---

## Summary Matrix: Trade-offs at a Glance

| Scenario | Algorithm | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| **2D Grid** | Multi-Source BFS | $\mathcal{O}(MN)$ | $\mathcal{O}(MN)$ |
| **3D Grid ($R \times C \times H$)**| 6-Neighbor 3D BFS | $\mathcal{O}(R \cdot C \cdot H)$ | $\mathcal{O}(R \cdot C \cdot H)$ |
""",

    "129 Course Schedule": """# 04 Interview Follow-ups & System Variations: Course Schedule

The problem determines if all courses can be finished given prerequisite pairs. This is equivalent to **Cycle Detection in a Directed Graph**. Optimal solutions include **Kahn's Algorithm (BFS with In-degrees)** or **DFS 3-Coloring** in $\mathcal{O}(V + E)$ time and $\mathcal{O}(V + E)$ space.

In technical interviews, this problem is the foundation of DAG topological sorting, package dependency managers (npm, pip), and build systems.

---

## 1. Kahn's Algorithm (BFS In-Degree) vs. DFS 3-Coloring

| Feature | Kahn's Algorithm (BFS) | DFS 3-Coloring |
| :--- | :--- | :--- |
| **Core Mechanism** | Track `in_degree[u]` for each node | Track node states (`UNVISITED`, `VISITING`, `VISITED`) |
| **Cycle Detection** | `processed_count < num_courses` | Finding an edge to a `VISITING` (Gray) node |
| **Queue / Stack** | Enqueue nodes with `in_degree == 0` | Standard recursion call stack |
| **Topological Order**| Natural forward order | Reverse of post-order finishing times |

---

## 2. DFS 3-Coloring Cycle Detection Template

```cpp
bool hasCycle(int u, vector<vector<int>>& adj, vector<int>& state) {
    state[u] = 1; // 1 = VISITING (Gray node on current recursion path)
    for (int v : adj[u]) {
        if (state[v] == 1) return true; // Back-edge detected -> CYCLE!
        if (state[v] == 0 && hasCycle(v, adj, state)) return true;
    }
    state[u] = 2; // 2 = VISITED (Black node completely evaluated)
    return false;
}
```

---

## Summary Matrix: Trade-offs at a Glance

| Approach | In-Degree Array Needed? | Time | Space |
| :--- | :--- | :--- | :--- |
| **Kahn's BFS (Optimal)** | Yes (`in_degree[V]`) | $\mathcal{O}(V + E)$ | $\mathcal{O}(V + E)$ |
| **DFS 3-Coloring** | No (State array `0, 1, 2`) | $\mathcal{O}(V + E)$ | $\mathcal{O}(V + E)$ |
""",

    "130 Course Schedule II": """# 04 Interview Follow-ups & System Variations: Course Schedule II

The problem returns a valid ordering of courses you should take to finish all courses (Topological Sort). Optimal approaches include **Kahn's BFS Algorithm** appending nodes to an `order` list in $\mathcal{O}(V + E)$ time and $\mathcal{O}(V + E)$ space.

In technical interviews, this problem is compared with parallel compilation job graphs (Make, Ninja, Bazel) and detecting all valid orderings.

---

## 1. Build Systems & Multi-Core Parallel Job Compilation (Ninja / Bazel)

### 💡 Parallel Topological Execution
- When building large software codebases (like Linux or Chrome):
  - Every source file is a vertex; dependencies are directed edges.
  - All nodes with `in_degree == 0` can be compiled **simultaneously in parallel across multiple CPU cores**!
  - As a file finishes compiling, decrement in-degrees of dependent files; when any hits 0, push to the thread pool work queue.

---

## Summary Matrix: Trade-offs at a Glance

| Output Goal | Algorithm | Time | Space |
| :--- | :--- | :--- | :--- |
| **Boolean Check (I)** | Kahn's count check | $\mathcal{O}(V + E)$ | $\mathcal{O}(V + E)$ |
| **1 Valid Order (II)** | Kahn's `order` vector append | $\mathcal{O}(V + E)$ | $\mathcal{O}(V + E)$ |
| **All Valid Orders** | Backtracking DFS with In-degrees | $\mathcal{O}(V!)$ | $\mathcal{O}(V)$ |
""",

    "131 Graph Valid Tree": """# 04 Interview Follow-ups & System Variations: Graph Valid Tree

The problem checks if an undirected graph of $N$ nodes and a list of edges forms a valid tree. Optimal solutions verify the **2 Fundamental Tree Invariants** in $\mathcal{O}(V + E)$ time and $\mathcal{O}(V)$ space.

In technical interviews, this problem tests minimal graph invariants and Disjoint Set Union cycle detection.

---

## 1. The 2 Fundamental Tree Theorems

An undirected graph with $N$ vertices is a valid tree **IF AND ONLY IF**:
1. **Edge Count Invariant**: Exactly $N - 1$ edges ($E = N - 1$).
2. **Connectivity Invariant**: The graph is fully connected (has exactly 1 connected component).

### 💡 The Fast-Exit Optimization
```cpp
bool validTree(int n, vector<vector<int>>& edges) {
    if (edges.size() != n - 1) return false; // Immediate fast exit!
    
    // Run DSU or BFS to verify full connectivity in 1 pass
}
```

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Edge Check | Connectivity Check | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **DSU (Union-Find)** | `edges.size() == n - 1` | Detect cycle on union | $\mathcal{O}(N \alpha(N))$ | $\mathcal{O}(N)$ |
| **BFS / DFS** | `edges.size() == n - 1` | Visited count $== N$ | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
""",

    "132 Number of Connected Components in an Undirected Graph": """# 04 Interview Follow-ups & System Variations: Number of Connected Components

The problem finds the number of connected components in an undirected graph. Optimal solutions include **Disjoint Set Union (Union-Find with Path Compression and Union by Rank)** in $\mathcal{O}((V + E) \alpha(V))$ time and $\mathcal{O}(V)$ space, or **BFS/DFS**.

In technical interviews, this problem is the prime template for dynamic connectivity and social network friend circles.

---

## 1. Disjoint Set Union (DSU) Optimal Implementation

```cpp
class DSU {
    vector<int> parent, rank;
    int count;
public:
    DSU(int n) : parent(n), rank(n, 0), count(n) {
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]); // Path compression
    }
    bool unite(int i, int j) {
        int root_i = find(i), root_j = find(j);
        if (root_i == root_j) return false;
        if (rank[root_i] < rank[root_j]) swap(root_i, root_j);
        parent[root_j] = root_i;
        if (rank[root_i] == rank[root_j]) rank[root_i]++;
        count--;
        return true;
    }
    int getCount() const { return count; }
};
```

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Nature | Time Complexity | Auxiliary Space |
| :--- | :--- | :--- | :--- |
| **Disjoint Set (DSU)** | Dynamic edges online | $\mathcal{O}((V + E) \alpha(V))$ | $\mathcal{O}(V)$ |
| **BFS / DFS** | Static graph traversal | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ |
""",

    "133 Word Ladder": """# 04 Interview Follow-ups & System Variations: Word Ladder

The problem finds the shortest transformation sequence from `beginWord` to `endWord` changing 1 letter at a time (Hard). Optimal approaches include **Bidirectional BFS** in $\mathcal{O}(N \times L^2)$ time and $\mathcal{O}(N \times L)$ space.

In technical interviews, this is the premier problem for demonstrating **Bidirectional Search** and intermediate pattern hashing.

---

## 1. Bidirectional BFS: Exponential Search Space Reduction

### 💡 Why Bidirectional BFS is $100\times$ Faster
- Let the branching factor be $B = 26 \times L$, and the shortest transformation depth be $D$.
- **Standard 1-Way BFS**: Explores $\mathcal{O}(B^D)$ nodes.
- **Bidirectional BFS (Meeting in the Middle)**:
  - Expands from `beginSet` and `endSet` simultaneously.
  - Always expand the smaller of the two sets:
    $$\mathcal{O}(B^{D/2} + B^{D/2}) = 2 \times \mathcal{O}(B^{D/2})$$
  - For $B = 20, D = 6$: 1-Way BFS searches $20^6 = 64,000,000$ states; Bidirectional BFS searches only $2 \times 20^3 = 16,000$ states!

---

## 2. Generalization: Word Ladder II (Return ALL Shortest Transformation Sequences)

### 💡 2-Phase Architecture (BFS DAG + DFS Backtracking)
1. **Phase 1 (BFS)**: Construct a directed acyclic graph of parent pointers during level order traversal until `endWord` is reached.
2. **Phase 2 (DFS Backtracking)**: Backtrack from `endWord` to `beginWord` along the shortest DAG to collect all valid word sequence paths.

---

## Summary Matrix: Trade-offs at a Glance

| Variation | Algorithm | Time Complexity | Search States ($B=20, D=6$) |
| :--- | :--- | :--- | :--- |
| **Shortest Length (#127)** | Bidirectional BFS | $\mathcal{O}(N \cdot L^2)$ | $\approx 1.6 \times 10^4$ |
| **All Paths (#126)** | BFS Parent DAG + DFS Backtrack | $\mathcal{O}(N \cdot L^2 + \text{Paths})$ | $\mathcal{O}(\text{Paths} \cdot L)$ |
""",

    "134 Network Delay Time": """# 04 Interview Follow-ups & System Variations: Network Delay Time

The problem finds the time taken for all nodes to receive a signal from node $K$ on a directed weighted graph. The optimal solution uses **Dijkstra's Algorithm with a Min-Heap Priority Queue** in $\mathcal{O}((V + E) \log V)$ time and $\mathcal{O}(V + E)$ space.

In technical interviews, this problem is the launchpad for shortest path comparisons (Dijkstra, Bellman-Ford, Floyd-Warshall, A*).

---

## 1. Comprehensive Shortest Path Algorithm Comparison

| Algorithm | Edge Weights | Time Complexity | Space Complexity | Best Use Case |
| :--- | :--- | :--- | :--- | :--- |
| **Dijkstra (Min-Heap)** | Non-Negative ($\ge 0$) | $\mathcal{O}((V + E) \log V)$ | $\mathcal{O}(V + E)$ | Single-Source Non-Negative |
| **0-1 BFS (Deque)** | Weights $\in \{0, 1\}$ | $\mathcal{O}(V + E)$ strictly | $\mathcal{O}(V)$ | Grid moves / Binary weights |
| **Bellman-Ford** | Negative allowed | $\mathcal{O}(V \cdot E)$ | $\mathcal{O}(V)$ | Detects Negative Weight Cycles |
| **SPFA (Queue Optimized)**| Negative allowed | $\mathcal{O}(E)$ avg / $\mathcal{O}(VE)$ worst | $\mathcal{O}(V)$ | Sparse graphs with negative edges |
| **Floyd-Warshall** | Negative allowed | $\mathcal{O}(V^3)$ | $\mathcal{O}(V^2)$ | All-Pairs Shortest Paths |
| **A* Search** | Non-Negative + Heuristic | $\mathcal{O}(E)$ directed | $\mathcal{O}(V)$ | Spatial Map Navigation (GPS) |

---

## 2. Dijkstra's Algorithm Implementation Template

```cpp
int networkDelayTime(vector<vector<int>>& times, int n, int k) {
    vector<vector<pair<int, int>>> adj(n + 1);
    for (auto& t : times) {
        adj[t[0]].push_back({t[1], t[2]}); // u -> {v, weight}
    }
    
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    vector<int> dist(n + 1, INT_MAX);
    
    dist[k] = 0;
    pq.push({0, k}); // {distance, node}
    
    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (d > dist[u]) continue; // Stale heap entry optimization
        
        for (auto& [v, w] : adj[u]) {
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            }
        }
    }
    
    int max_time = 0;
    for (int i = 1; i <= n; i++) {
        if (dist[i] == INT_MAX) return -1;
        max_time = max(max_time, dist[i]);
    }
    return max_time;
}
```

---

## Summary Matrix: Trade-offs at a Glance

| Scenario | Recommended Algorithm | Time | Space |
| :--- | :--- | :--- | :--- |
| **Non-Negative Weights** | Dijkstra (Min-Heap) | $\mathcal{O}((V + E) \log V)$ | $\mathcal{O}(V + E)$ |
| **Negative Weights Present** | Bellman-Ford / SPFA | $\mathcal{O}(V \cdot E)$ | $\mathcal{O}(V)$ |
| **All-Pairs Distances ($N \le 500$)**| Floyd-Warshall | $\mathcal{O}(V^3)$ | $\mathcal{O}(V^2)$ |
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
