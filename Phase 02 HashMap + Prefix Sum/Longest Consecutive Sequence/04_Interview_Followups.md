# 04 Interview Follow-ups: Longest Consecutive Sequence

## 1. What if the Array is Distributed Across Multiple Machines?
- Use Disjoint Set Union (DSU) or Hash Partitioning:
  - Partition elements by range buckets $[K \cdot B, (K+1) \cdot B - 1]$.
  - Stitch boundary elements across adjacent partition machines via remote DSU queries.
