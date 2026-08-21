# 04 Interview Follow-ups & System Variations: Number of Connected Components

The problem finds the number of connected components in an undirected graph. Optimal solutions include **Disjoint Set Union (Union-Find with Path Compression and Union by Rank)** in $\mathcal{O}((V + E) lpha(V))$ time and $\mathcal{O}(V)$ space, or **BFS/DFS**.

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
| **Disjoint Set (DSU)** | Dynamic edges online | $\mathcal{O}((V + E) lpha(V))$ | $\mathcal{O}(V)$ |
| **BFS / DFS** | Static graph traversal | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ |
