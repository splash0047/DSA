# 04 Interview Follow-ups & System Variations: Partition List

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
