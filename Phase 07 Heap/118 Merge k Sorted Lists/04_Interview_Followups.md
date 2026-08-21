# 04 Interview Follow-ups & System Variations: Merge k Sorted Lists (Heap)

The problem merges $K$ sorted linked lists of total $N$ nodes. The optimal Min-Heap approach stores the active head node of each of the $K$ lists, running in $\mathcal{O}(N \log K)$ time and $\mathcal{O}(K)$ space.

In technical interviews, this problem is compared with multi-way external streaming and priority queue comparator overhead.

---

## 1. Min-Heap Implementation with Node Pointers

```cpp
struct CompareNode {
    bool operator()(ListNode* a, ListNode* b) {
        return a->val > b->val; // Min-Heap
    }
};

ListNode* mergeKLists(vector<ListNode*>& lists) {
    priority_queue<ListNode*, vector<ListNode*>, CompareNode> pq;
    for (auto list : lists) {
        if (list) pq.push(list);
    }
    
    ListNode dummy(0);
    ListNode* tail = &dummy;
    while (!pq.empty()) {
        ListNode* top = pq.top(); pq.pop();
        tail->next = top;
        tail = tail->next;
        if (top->next) pq.push(top->next);
    }
    return dummy.next;
}
```

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Space Model | Time | Space |
| :--- | :--- | :--- | :--- |
| **Min-Heap (Optimal)** | Heap of $K$ pointers | $\mathcal{O}(N \log K)$ | $\mathcal{O}(K)$ |
| **Divide & Conquer** | Pairwise merge lists | $\mathcal{O}(N \log K)$ | $\mathcal{O}(1)$ auxiliary |
