# 04 Interview Follow-ups & System Variations: Palindrome Linked List

The problem determines if a singly linked list is a palindrome. The optimal in-place solution finds the middle, reverses the second half, compares in lockstep, and restores the list in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem is used to test safe in-place restoration and rolling hashes for read-only streams.

---

## 1. Clean 4-Step In-Place Implementation with List Restoration

```cpp
bool isPalindrome(ListNode* head) {
    if (!head || !head->next) return true;
    
    // 1. Find first middle
    ListNode *slow = head, *fast = head;
    while (fast->next && fast->next->next) {
        slow = slow->next;
        fast = fast->next->next;
    }
    
    // 2. Reverse second half
    ListNode *prev = nullptr, *curr = slow->next;
    while (curr) {
        ListNode* next_node = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next_node;
    }
    
    // 3. Compare first and second half
    ListNode *p1 = head, *p2 = prev;
    bool is_pal = true;
    while (p2) {
        if (p1->val != p2->val) { is_pal = false; break; }
        p1 = p1->next;
        p2 = p2->next;
    }
    
    // 4. Restore list back to original shape (Good Engineering!)
    curr = prev; prev = nullptr;
    while (curr) {
        ListNode* next_node = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next_node;
    }
    slow->next = prev;
    
    return is_pal;
}
```

---

## Summary Matrix: Trade-offs at a Glance

| Approach | List Mutation | Time | Space |
| :--- | :--- | :--- | :--- |
| **In-Place Reverse + Restore** | Modifies & Restores | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Array Copy** | Immutable | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ memory |
| **Forward/Backward Rolling Hash**| Immutable | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ (probabilistic) |
