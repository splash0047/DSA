import os

DSA_ROOT = r"c:\Users\Pinak chimurkar\DSA"

def write_problem(phase_dir, folder_name, q_content, bf_content, opt_content, exp_content, fol_content):
    target_dir = os.path.join(DSA_ROOT, phase_dir, folder_name)
    os.makedirs(target_dir, exist_ok=True)
    
    files = {
        "00_Question.md": q_content,
        "01_Brute_Force.md": bf_content,
        "02_Optimal_Approach.md": opt_content,
        "03_Explanation.md": exp_content,
        "04_Interview_Followups.md": fol_content,
    }
    
    for filename, content in files.items():
        filepath = os.path.join(target_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
    print(f"Created: {phase_dir}/{folder_name}")

# Group Anagrams (LC #49)
write_problem(
    "Phase 02 HashMap + Prefix Sum", "Group Anagrams",
    r"""# Group Anagrams

- **Platform**: LeetCode
- **Problem Number**: #49
- **Difficulty**: Medium
- **URL**: [LeetCode #49 - Group Anagrams](https://leetcode.com/problems/group-anagrams/)

---

## Problem Statement

Given an array of strings `strs`, group the **anagrams** together. You can return the answer in **any order**.
""",
    r"""# Group Anagrams - Brute Force

- **Pattern**: Pairwise Anagram Checking with Frequency Array
""",
    r"""# Group Anagrams - Optimal Approach

```cpp
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>

class Solution {
public:
    std::vector<std::vector<std::string>> groupAnagrams(std::vector<std::string>& strs) {
        std::unordered_map<std::string, std::vector<std::string>> map;
        for (const std::string& s : strs) {
            std::string key = s;
            std::sort(key.begin(), key.end());
            map[key].push_back(s);
        }

        std::vector<std::vector<std::string>> result;
        result.reserve(map.size());
        for (auto& [key, group] : map) {
            result.push_back(std::move(group));
        }
        return result;
    }
};
```
""",
    r"""# Group Anagrams - Deep Explanation

Uses sorted string as the hash map key grouping all anagrams into the same bucket in $\mathcal{O}(N \cdot K \log K)$ time.
""",
    r"""# 04 Interview Follow-ups: Group Anagrams

## 1. Character Count Tuple Key
- Avoid $\mathcal{O}(K \log K)$ sort by building a 26-character count string key in $\mathcal{O}(K)$ time.
"""
)

# Happy Number (LC #202)
write_problem(
    "Phase 02 HashMap + Prefix Sum", "Happy Number",
    r"""# Happy Number

- **Platform**: LeetCode
- **Problem Number**: #202
- **Difficulty**: Easy
- **URL**: [LeetCode #202 - Happy Number](https://leetcode.com/problems/happy-number/)

---

## Problem Statement

Write an algorithm to determine if a number `n` is happy.
""",
    r"""# Happy Number - Brute Force (Hash Set)

```cpp
#include <unordered_set>

class Solution {
    int getNext(int n) {
        int total = 0;
        while (n > 0) {
            int d = n % 10;
            total += d * d;
            n /= 10;
        }
        return total;
    }
public:
    bool isHappy(int n) {
        std::unordered_set<int> seen;
        while (n != 1 && !seen.count(n)) {
            seen.insert(n);
            n = getNext(n);
        }
        return n == 1;
    }
};
```
""",
    r"""# Happy Number - Optimal Approach (Floyd's Cycle Finding)

```cpp
class Solution {
    int getNext(int n) {
        int total = 0;
        while (n > 0) {
            int d = n % 10;
            total += d * d;
            n /= 10;
        }
        return total;
    }
public:
    bool isHappy(int n) {
        int slow = n;
        int fast = getNext(n);

        while (fast != 1 && slow != fast) {
            slow = getNext(slow);
            fast = getNext(getNext(fast));
        }
        return fast == 1;
    }
};
```
""",
    r"""# Happy Number - Deep Explanation

Uses Tortoise and Hare algorithm to detect cycles in $\mathcal{O}(1)$ auxiliary space.
""",
    r"""# 04 Interview Follow-ups: Happy Number

## 1. Space Optimization
- Floyd's cycle detection eliminates heap hash set memory.
"""
)

print("Created Group Anagrams & Happy Number successfully!")
