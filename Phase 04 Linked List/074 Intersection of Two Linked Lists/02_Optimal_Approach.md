# Intersection of Two Linked Lists

## Pattern Used

- **Pattern**: **Two Pointers Path Equivalence Switching**
- **Concept**: Initialize two pointers `pA = headA` and `pB = headB`. Advance both 1 step at a time.
  - When `pA` reaches `nullptr`, redirect `pA = headB`.
  - When `pB` reaches `nullptr`, redirect `pB = headA`.
  - Both pointers will travel a total length of $(LenA + LenB)$. If the lists intersect, `pA` and `pB` will meet exactly at the intersection node! If they do not intersect, both pointers will hit `nullptr` at the exact same time.

---

## Observation / Mathematical Proof

Let:
- $a$ = length of non-shared segment in List A.
- $b$ = length of non-shared segment in List B.
- $c$ = length of shared common intersecting segment.

Path traveled by `pA`: $a + c + b$.
Path traveled by `pB`: $b + c + a$.

Since $(a + c + b) = (b + c + a)$, both pointers travel the **exact same total distance**! After switching lists once, `pA` and `pB` become synchronized and reach the intersection node simultaneously.

If there is no intersection ($c = 0$), both pointers travel $a + b$ steps and hit `nullptr` simultaneously (`pA == pB == nullptr`).

---

## Intuition

Redirecting `pA` to `headB` and `pB` to `headA` naturally neutralizes any length difference between the two lists without needing to count list lengths explicitly.

---

## Algorithm

1. If `headA == nullptr || headB == nullptr`, return `nullptr`.
2. `pA = headA`, `pB = headB`.
3. While `pA != pB`:
   a. `pA = (pA == nullptr) ? headB : pA->next`.
   b. `pB = (pB == nullptr) ? headA : pB->next`.
4. Return `pA`.

---

## Clean C++17 Solution

```cpp
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if (headA == nullptr || headB == nullptr) return nullptr;
        
        ListNode* pA = headA;
        ListNode* pB = headB;
        
        while (pA != pB) {
            pA = (pA == nullptr) ? headB : pA->next;
            pB = (pB == nullptr) ? headA : pB->next;
        }
        
        return pA; // Either points to intersection node or nullptr (no intersection)
    }
};
```

---

## Dry Run

### Input
- `listA = [4 -> 1 -> 8 -> 4 -> 5]` ($a=2, c=3$)
- `listB = [5 -> 6 -> 1 -> 8 -> 4 -> 5]` ($b=3, c=3$)

### Execution Trace

- Pass 1:
  - `pA` advances 5 nodes, hits `nullptr`, switches to `headB`.
  - `pB` advances 6 nodes, hits `nullptr`, switches to `headA`.
- Pass 2:
  - `pA` traverses $b=3$ nodes of List B.
  - `pB` traverses $a=2$ nodes of List A.
  - Both `pA` and `pB` land on Node `8` simultaneously!

### Result
- Output Node: `8`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(M + N)$
  - Both pointers travel at most $M + N$ steps.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Constant auxiliary space (only two pointer variables used).

---

## Why This is Optimal

- Finds intersection in linear $\mathcal{O}(M + N)$ time.
- Uses zero extra memory ($\mathcal{O}(1)$ space), satisfying the follow-up.

---

## Common Mistakes

1. **Switching Pointer on `pA->next == nullptr` vs `pA == nullptr`**: Switching on `pA->next == nullptr` creates an infinite loop when lists do NOT intersect because pointers never hit `nullptr` together. Always switch on `pA == nullptr`.
2. **Modifying List Nodes**: Overwriting node pointers or values, violating the constraint that lists must retain their original structure.
