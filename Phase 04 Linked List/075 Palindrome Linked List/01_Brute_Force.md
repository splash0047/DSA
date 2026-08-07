# Palindrome Linked List

- **Problem Number**: 234
- **Platform**: LeetCode #234
- **Difficulty**: Easy
- **Pattern**: Vector Copy & Two-Pointer Check

---

## Brute Force Intuition

Traverse the linked list and copy all node values into an array `vals`. Then use two pointers `left = 0` and `right = vals.size() - 1` to check if `vals` is a palindrome.

---

## Algorithm

1. Extract all node values into `vector<int> vals`.
2. `left = 0`, `right = vals.size() - 1`.
3. While `left < right`:
   a. If `vals[left] != vals[right]`, return `false`.
   b. `left++`, `right--`.
4. Return `true`.

---

## Code

```cpp
#include <vector>

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    bool isPalindrome(ListNode* head) {
        std::vector<int> vals;
        ListNode* curr = head;
        while (curr != nullptr) {
            vals.push_back(curr->val);
            curr = curr->next;
        }
        
        int left = 0;
        int right = vals.size() - 1;
        while (left < right) {
            if (vals[left] != vals[right]) {
                return false;
            }
            left++;
            right--;
        }
        
        return true;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Single pass to extract values and $N/2$ comparisons.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Stores $N$ node values in vector memory.

---

## Why This Approach Is Not Optimal

Using a vector requires $\mathcal{O}(N)$ auxiliary space. By combining **Fast/Slow Mid Finding** and **In-Place Reversal of Second Half**, we can verify if a linked list is a palindrome in $\mathcal{O}(N)$ time with $\mathcal{O}(1)$ space.
