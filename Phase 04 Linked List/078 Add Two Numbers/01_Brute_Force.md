# Add Two Numbers

- **Problem Number**: 2
- **Platform**: LeetCode #2
- **Difficulty**: Medium
- **Pattern**: String / BigInt Conversion

---

## Brute Force Intuition

Convert linked lists `l1` and `l2` into integers or string representations, sum the two numbers, and convert the resulting sum back into a reversed linked list.

---

## Algorithm

1. Extract digits from `l1` and build integer `num1`.
2. Extract digits from `l2` and build integer `num2`.
3. Compute `sum = num1 + num2`.
4. Build new linked list by extracting digits of `sum` from right to left using modulo 10.

---

## Code

```cpp
#include <string>
#include <algorithm>

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        // String-based BigInt implementation due to 100-digit constraint
        std::string s1 = "", s2 = "";
        while (l1 != nullptr) { s1 += std::to_string(l1->val); l1 = l1->next; }
        while (l2 != nullptr) { s2 += std::to_string(l2->val); l2 = l2->next; }
        
        std::reverse(s1.begin(), s1.end());
        std::reverse(s2.begin(), s2.end());
        
        std::string sum_str = "";
        int i = s1.length() - 1, j = s2.length() - 1, carry = 0;
        while (i >= 0 || j >= 0 || carry > 0) {
            int digit1 = (i >= 0) ? (s1[i--] - '0') : 0;
            int digit2 = (j >= 0) ? (s2[j--] - '0') : 0;
            int sum = digit1 + digit2 + carry;
            carry = sum / 10;
            sum_str += std::to_string(sum % 10);
        }
        
        ListNode dummy(0);
        ListNode* curr = &dummy;
        for (char c : sum_str) {
            curr->next = new ListNode(c - '0');
            curr = curr->next;
        }
        
        return dummy.next;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(\max(N, M))$
  - String extraction, string reversal, digit addition, and list creation.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(\max(N, M))$
  - Auxiliary string storage.

---

## Why This Approach Is Not Optimal

Converting linked lists into strings requires unnecessary intermediate string allocations and conversions. By using **Single-Pass Digit Addition with Carry**, we can add digits node-by-node directly in $\mathcal{O}(\max(N, M))$ time.
