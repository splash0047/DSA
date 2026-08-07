# Basic Calculator II

- **Problem Number**: 227
- **Platform**: LeetCode #227
- **Difficulty**: Medium
- **Pattern**: Two-Pass Vector Precedence Evaluation

---

## Brute Force Intuition

Parse string `s` into two vectors: `vector<long long> nums` for numbers and `vector<char> ops` for operators.
- **Pass 1**: Evaluate high-precedence operators (`*` and `/`) from left to right. When an operator at `ops[i]` is `*` or `/`, compute `nums[i] (op) nums[i+1]`, update `nums[i]`, and erase `ops[i]` and `nums[i+1]`.
- **Pass 2**: Evaluate low-precedence operators (`+` and `-`) from left to right over the remaining elements.

---

## Algorithm

1. Parse numbers and operators into `nums` and `ops` (skipping whitespace).
2. Pass 1 (`*` and `/`):
   - For `i = 0` to `ops.size() - 1`:
     - If `ops[i] == '*'` or `ops[i] == '/'`:
       - `val = (ops[i] == '*') ? (nums[i] * nums[i+1]) : (nums[i] / nums[i+1])`.
       - `nums[i] = val`.
       - Erase `nums[i+1]` and `ops[i]`.
       - `i--`.
3. Pass 2 (`+` and `-`):
   - `res = nums[0]`.
   - For `i = 0` to `ops.size() - 1`:
     - `res = (ops[i] == '+') ? (res + nums[i+1]) : (res - nums[i+1])`.
4. Return `res`.

---

## Code

```cpp
#include <string>
#include <vector>
#include <cctype>

class Solution {
public:
    int calculate(std::string s) {
        std::vector<long long> nums;
        std::vector<char> ops;
        
        long long current_num = 0;
        bool in_num = false;
        
        for (char ch : s) {
            if (std::isdigit(ch)) {
                current_num = current_num * 10 + (ch - '0');
                in_num = true;
            } else if (ch == '+' || ch == '-' || ch == '*' || ch == '/') {
                nums.push_back(current_num);
                ops.push_back(ch);
                current_num = 0;
                in_num = false;
            }
        }
        if (in_num || nums.empty()) {
            nums.push_back(current_num);
        }
        
        // Pass 1: Process '*' and '/'
        for (size_t i = 0; i < ops.size(); ) {
            if (ops[i] == '*' || ops[i] == '/') {
                long long a = nums[i];
                long long b = nums[i + 1];
                long long res = (ops[i] == '*') ? (a * b) : (a / b);
                
                nums[i] = res;
                nums.erase(nums.begin() + i + 1);
                ops.erase(ops.begin() + i);
            } else {
                i++;
            }
        }
        
        // Pass 2: Process '+' and '-'
        long long final_res = nums[0];
        for (size_t i = 0; i < ops.size(); ++i) {
            if (ops[i] == '+') final_res += nums[i + 1];
            else if (ops[i] == '-') final_res -= nums[i + 1];
        }
        
        return static_cast<int>(final_res);
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N^2)$
  - Vector element deletion via `erase` shifts remaining elements in $\mathcal{O}(N)$ time per operator.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Vector storage for numbers and operators.

---

## Why This Approach Is Not Optimal

Vector `erase` operations take quadratic $\mathcal{O}(N^2)$ time. Using a **Single-Pass Operand Stack**, high precedence operations (`*`, `/`) can be evaluated immediately while low precedence operations (`+`, `-`) are deferred on the stack, computing the answer in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space!
