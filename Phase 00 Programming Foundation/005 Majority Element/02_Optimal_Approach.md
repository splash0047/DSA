# Majority Element

## Pattern Used

- **Pattern**: **Boyer-Moore Voting Algorithm**
- **Concept**: Element cancellation pairing. If we pair up different elements and discard them, the majority element (which accounts for strictly more than half of the total elements) is guaranteed to survive.

---

## Observation

Since the majority element occurs more than $\lfloor n / 2 \rfloor$ times:
1. The sum of counts of all *other* non-majority elements is strictly less than the count of the majority element.
2. If we increment a counter when seeing a candidate element and decrement it when seeing any other element, the net count for the true majority element will always end up strictly greater than `0`.

---

## Intuition

Imagine an election where candidates vote. Every vote for candidate $X$ adds +1. Every vote for a different candidate cancels out one vote (-1). 
- If a candidate's vote count drops to `0`, we discard that candidate and pick the current element as the new candidate.
- Because the majority candidate has more votes than all rival candidates combined, the majority candidate will always emerge as the final survivor.

---

## Algorithm

1. Initialize `candidate = 0` and `count = 0`.
2. Iterate through each `num` in `nums`:
   a. If `count == 0`, assign `candidate = num`.
   b. If `num == candidate`, increment `count++`.
   c. Else, decrement `count--`.
3. Return `candidate`.

---

## Clean C++17 Solution

```cpp
#include <vector>

class Solution {
public:
    int majorityElement(const std::vector<int>& nums) {
        int candidate = 0;
        int count = 0;
        
        for (int num : nums) {
            if (count == 0) {
                candidate = num;
            }
            count += (num == candidate) ? 1 : -1; or
       //     if (num == candidate)
        //          count++;
      //       else
                   count--;
//
        }
        
        return candidate;
    }
};
```

---

## Dry Run

### Input
- `nums = [2, 2, 1, 1, 1, 2, 2]`

### Execution Trace

| Step | `num` | Candidate State Before | Count State Before | Action | `candidate` After | `count` After |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `2` | - | `0` | Set candidate = 2 | `2` | `1` |
| 2 | `2` | `2` | `1` | Match (2 == 2) -> count++ | `2` | `2` |
| 3 | `1` | `2` | `2` | Mismatch (1 != 2) -> count-- | `2` | `1` |
| 4 | `1` | `2` | `1` | Mismatch (1 != 2) -> count-- | `2` | `0` |
| 5 | `1` | `2` | `0` | Set candidate = 1 | `1` | `1` |
| 6 | `2` | `1` | `1` | Mismatch (2 != 1) -> count-- | `1` | `0` |
| 7 | `2` | `1` | `0` | Set candidate = 2 | `2` | `1` |

### Result
- Output: `2`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Single pass through array of $N$ elements.
  - Constant time operations inside loop.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(1)$
  - Uses only two integer variables (`candidate`, `count`), achieving $\mathcal{O}(1)$ auxiliary memory.

---

## Why This is Optimal

- Reading all elements at least once requires $\Omega(N)$ time.
- Performing the selection using $\mathcal{O}(1)$ additional memory achieves the absolute theoretical minimum for space complexity.

---

## Common Mistakes

1. **Resetting Candidate Incorrectly**: Resetting candidate on `count < 0` instead of `count == 0`.
2. **Assuming Majority Always Exists When Not Guaranteed**: If the problem statement did not guarantee a majority element's existence, a second verification pass would be necessary. Here, the guarantee allows returning `candidate` directly.
