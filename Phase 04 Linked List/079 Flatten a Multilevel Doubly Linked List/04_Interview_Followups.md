# 04 Interview Follow-ups & System Variations: Flatten a Multilevel Doubly Linked List

The problem flattens a multilevel doubly linked list containing `child` pointers into a single-level doubly linked list in preorder traversal order. The optimal iterative approach splices child sublists in-place in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem tests bidirectional pointer consistency (`prev` and `next`), stack-based DFS vs. in-place splicing, and tree preorder flattening.

---

## 1. In-Place Child Splicing Template ($\mathcal{O}(1)$ Extra Space)

```cpp
Node* flatten(Node* head) {
    Node* curr = head;
    while (curr != nullptr) {
        if (curr->child != nullptr) {
            Node* next_node = curr->next;
            Node* child = curr->child;
            
            // Find tail of child list
            while (child->next != nullptr) child = child->next;
            
            // Splice child list between curr and next_node
            curr->next = curr->child;
            curr->child->prev = curr;
            curr->child = nullptr;
            
            if (next_node != nullptr) {
                child->next = next_node;
                next_node->prev = child;
            }
        }
        curr = curr->next;
    }
    return head;
}
```

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Space Model | Time | Space |
| :--- | :--- | :--- | :--- |
| **In-Place Splicing** | Rewire child tails | $\mathcal{O}(N)$ | strictly $\mathcal{O}(1)$ |
| **Stack-Based DFS** | Recursive / Stack | $\mathcal{O}(N)$ | $\mathcal{O}(D)$ depth |
