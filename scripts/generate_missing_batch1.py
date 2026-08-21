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

# Let's write Phase 02, 03, 04, 05, 06, 07, 08 problems first!

# 3. Isomorphic Strings (LC #205)
write_problem(
    "Phase 02 HashMap + Prefix Sum", "Isomorphic Strings",
    r"""# Isomorphic Strings

- **Platform**: LeetCode
- **Problem Number**: #205
- **Difficulty**: Easy
- **URL**: [LeetCode #205 - Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/)

---

## Problem Statement

Given two strings `s` and `t`, determine if they are isomorphic.

Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

---

## Examples

### Example 1
```text
Input: s = "egg", t = "add"
Output: true
```

### Example 2
```text
Input: s = "foo", t = "bar"
Output: false
```

### Example 3
```text
Input: s = "paper", t = "title"
Output: true
```

---

## Constraints

- $1 \le \text{s.length} \le 5 \times 10^4$
- $\text{t.length} == \text{s.length}$
- `s` and `t` consist of any valid ascii character.
""",
    r"""# Isomorphic Strings - Brute Force

- **Problem Number**: 205
- **Platform**: LeetCode #205
- **Difficulty**: Easy
- **Pattern**: String Reconstruction / Linear Search

---

## Algorithm

1. For each character `s[i]`, find its first occurrence index in `s`.
2. Find the first occurrence index of `t[i]` in `t`.
3. If their first occurrence indices differ at any position $i$, the character mapping pattern is inconsistent $\implies$ return `false`.
4. Return `true`.

---

## Code

```cpp
#include <string>

class Solution {
public:
    bool isIsomorphic(std::string s, std::string t) {
        if (s.size() != t.size()) return false;
        for (int i = 0; i < s.size(); i++) {
            if (s.find(s[i]) != t.find(t[i])) {
                return false;
            }
        }
        return true;
    }
};
```

---

## Time & Space Complexity

- **Time Complexity**: $\mathcal{O}(N^2)$ due to `std::string::find` linear scanning.
- **Space Complexity**: $\mathcal{O}(1)$.
""",
    r"""# Isomorphic Strings - Optimal Approach

- **Problem Number**: 205
- **Platform**: LeetCode #205
- **Difficulty**: Easy
- **Pattern**: Last Seen Index Array / Bijection Tracking

---

## Optimal Intuition

Maintain two arrays mapping each character to its most recent 1-indexed position seen so far. If at any index `s[i]` and `t[i]` recorded different last-seen timestamps, they cannot be isomorphic.

---

## Code

```cpp
#include <string>

class Solution {
public:
    bool isIsomorphic(std::string s, std::string t) {
        if (s.size() != t.size()) return false;
        int map_s[256] = {0};
        int map_t[256] = {0};

        for (int i = 0; i < s.size(); i++) {
            unsigned char c1 = s[i];
            unsigned char c2 = t[i];

            if (map_s[c1] != map_t[c2]) return false;

            map_s[c1] = i + 1;
            map_t[c2] = i + 1;
        }
        return true;
    }
};
```

---

## Time & Space Complexity

- **Time Complexity**: $\mathcal{O}(N)$ single pass.
- **Space Complexity**: $\mathcal{O}(1)$ (fixed 256-element arrays).
""",
    r"""# Isomorphic Strings - Deep Explanation

## Core Concept: Bijection (1-to-1 and Onto)
A valid isomorphism requires:
1. Every character in $S$ maps to exactly one character in $T$.
2. No two distinct characters in $S$ map to the same character in $T$.
Using the last-seen index array automatically verifies both directions of the bijection in $\mathcal{O}(1)$ space!
""",
    r"""# 04 Interview Follow-ups: Isomorphic Strings

## 1. What if Character Set is Unicode (UTF-32)?
- Fixed 256 array cannot hold $2^{20}$ code points.
- Use two `std::unordered_map<char32_t, int>` structures. Time remains $\mathcal{O}(N)$ average, space is $\mathcal{O}(U)$ where $U$ is distinct characters.
"""
)

# 4. Word Pattern (LC #290)
write_problem(
    "Phase 02 HashMap + Prefix Sum", "Word Pattern",
    r"""# Word Pattern

- **Platform**: LeetCode
- **Problem Number**: #290
- **Difficulty**: Easy
- **URL**: [LeetCode #290 - Word Pattern](https://leetcode.com/problems/word-pattern/)

---

## Problem Statement

Given a `pattern` and a string `s`, find if `s` follows the same pattern.

Here **follow** means a full match, such that there is a bijection between a letter in `pattern` and a **non-empty** word in `s`.

---

## Examples

### Example 1
```text
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
```

### Example 2
```text
Input: pattern = "abba", s = "dog cat cat fish"
Output: false
```

### Example 3
```text
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
```

---

## Constraints

- $1 \le \text{pattern.length} \le 300$
- `pattern` contains only lower-case English letters.
- $1 \le \text{s.length} \le 3000$
- `s` contains only lowercase English letters and spaces `' '`.
- `s` does not contain any leading or trailing spaces.
- All the words in `s` are separated by a single space.
""",
    r"""# Word Pattern - Brute Force

- **Problem Number**: 290
- **Platform**: LeetCode #290
- **Difficulty**: Easy
- **Pattern**: String Tokenization + Pairwise Consistency Check

---

## Algorithm

1. Split `s` into a list of word tokens.
2. If `pattern.length != words.length`, return `false`.
3. For each pair $(i, j)$:
   - Check if `(pattern[i] == pattern[j]) != (words[i] == words[j])`. If so, return `false`.
4. Return `true`.

---

## Code

```cpp
#include <string>
#include <vector>
#include <sstream>

class Solution {
public:
    bool wordPattern(std::string pattern, std::string s) {
        std::stringstream ss(s);
        std::string word;
        std::vector<std::string> words;
        while (ss >> word) words.push_back(word);

        if (pattern.size() != words.size()) return false;

        for (int i = 0; i < pattern.size(); i++) {
            for (int j = i + 1; j < pattern.size(); j++) {
                if ((pattern[i] == pattern[j]) != (words[i] == words[j])) {
                    return false;
                }
            }
        }
        return true;
    }
};
```

---

## Time & Space Complexity

- **Time Complexity**: $\mathcal{O}(N^2 \cdot L)$ where $L$ is word length.
- **Space Complexity**: $\mathcal{O}(N \cdot L)$ for words list.
""",
    r"""# Word Pattern - Optimal Approach

- **Problem Number**: 290
- **Platform**: LeetCode #290
- **Difficulty**: Easy
- **Pattern**: Two-Way Hash Map / Last Seen Index Tracking

---

## Optimal Intuition

Map `char -> index` and `word -> index`. When examining the $i$-th element, check that `char_to_idx[pattern[i]] == word_to_idx[word]`. Update both to $i + 1$.

---

## Code

```cpp
#include <string>
#include <vector>
#include <sstream>
#include <unordered_map>

class Solution {
public:
    bool wordPattern(std::string pattern, std::string s) {
        std::stringstream ss(s);
        std::string word;
        std::vector<std::string> words;
        while (ss >> word) words.push_back(word);

        if (pattern.size() != words.size()) return false;

        std::unordered_map<char, int> char_map;
        std::unordered_map<std::string, int> word_map;

        for (int i = 0; i < pattern.size(); i++) {
            char c = pattern[i];
            const std::string& w = words[i];

            if (char_map[c] != word_map[w]) return false;

            char_map[c] = i + 1;
            word_map[w] = i + 1;
        }
        return true;
    }
};
```

---

## Time & Space Complexity

- **Time Complexity**: $\mathcal{O}(N \cdot L)$
- **Space Complexity**: $\mathcal{O}(N \cdot L)$
""",
    r"""# Word Pattern - Deep Explanation

## Walkthrough
Pattern: `"abba"`, Words: `["dog", "cat", "cat", "dog"]`
- `i=0`: `c='a'`, `w="dog"` $\to$ both not seen $\to$ set both to index $1$.
- `i=1`: `c='b'`, `w="cat"` $\to$ both not seen $\to$ set both to index $2$.
- `i=2`: `c='b'`, `w="cat"` $\to$ both had index $2$ $\to$ match! set both to index $3$.
- `i=3`: `c='a'`, `w="dog"` $\to$ both had index $1$ $\to$ match! set both to index $4$.
Result: `true`.
""",
    r"""# 04 Interview Follow-ups: Word Pattern

## 1. What if `s` is an infinite stream of words?
- Stream words one-by-one from a socket/file reader rather than pre-tokenizing the entire string into memory.
- If stream terminates before pattern or pattern exhausts first, return `false`.
"""
)

# 5. Longest Consecutive Sequence (LC #128)
write_problem(
    "Phase 02 HashMap + Prefix Sum", "Longest Consecutive Sequence",
    r"""# Longest Consecutive Sequence

- **Platform**: LeetCode
- **Problem Number**: #128
- **Difficulty**: Medium
- **URL**: [LeetCode #128 - Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)

---

## Problem Statement

Given an unsorted array of integers `nums`, return *the length of the longest consecutive elements sequence.*

You must write an algorithm that runs in **$\mathcal{O}(N)$** time.

---

## Examples

### Example 1
```text
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
```

### Example 2
```text
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
```

---

## Constraints

- $0 \le \text{nums.length} \le 10^5$
- $-10^9 \le \text{nums}[i] \le 10^9$
""",
    r"""# Longest Consecutive Sequence - Brute Force (Sorting)

- **Problem Number**: 128
- **Platform**: LeetCode #128
- **Difficulty**: Medium
- **Pattern**: Sorting + Linear Scan

---

## Algorithm

1. If array is empty, return 0.
2. Sort `nums` in ascending order.
3. Traverse sorted array, tracking `current_streak`:
   - If `nums[i] == nums[i-1]`, skip duplicate.
   - If `nums[i] == nums[i-1] + 1`, `current_streak++`.
   - Else, reset `current_streak = 1`.
4. Return `max_streak`.

---

## Code

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    int longestConsecutive(std::vector<int>& nums) {
        if (nums.empty()) return 0;
        std::sort(nums.begin(), nums.end());

        int longest = 1, current = 1;
        for (size_t i = 1; i < nums.size(); i++) {
            if (nums[i] == nums[i - 1]) continue;
            if (nums[i] == nums[i - 1] + 1) {
                current++;
            } else {
                longest = std::max(longest, current);
                current = 1;
            }
        }
        return std::max(longest, current);
    }
};
```

---

## Time & Space Complexity

- **Time Complexity**: $\mathcal{O}(N \log N)$
- **Space Complexity**: $\mathcal{O}(1)$ or $\mathcal{O}(N)$ depending on sorting algorithm.
""",
    r"""# Longest Consecutive Sequence - Optimal Approach (Hash Set Streak Start)

- **Problem Number**: 128
- **Platform**: LeetCode #128
- **Difficulty**: Medium
- **Pattern**: Hash Set with Sequence Start Detection ($\mathcal{O}(N)$)

---

## Optimal Intuition

Insert all numbers into an `unordered_set`. A number `x` is the **start of a sequence** if and only if `x - 1` is NOT in the set. For each sequence start, count how many consecutive numbers exist (`x + 1, x + 2, ...`).

Every element is visited at most twice $\implies$ strictly $\mathcal{O}(N)$ time!

---

## Code

```cpp
#include <vector>
#include <unordered_set>
#include <algorithm>

class Solution {
public:
    int longestConsecutive(const std::vector<int>& nums) {
        std::unordered_set<int> num_set(nums.begin(), nums.end());
        int longest = 0;

        for (int num : num_set) {
            // Check if 'num' is the start of a sequence
            if (!num_set.count(num - 1)) {
                int current_num = num;
                int current_streak = 1;

                while (num_set.count(current_num + 1)) {
                    current_num++;
                    current_streak++;
                }
                longest = std::max(longest, current_streak);
            }
        }
        return longest;
    }
};
```

---

## Time & Space Complexity

- **Time Complexity**: $\mathcal{O}(N)$ average time (each number is evaluated at most twice).
- **Space Complexity**: $\mathcal{O}(N)$ auxiliary space for the Hash Set.
""",
    r"""# Longest Consecutive Sequence - Deep Explanation

## Why is the Inner Loop $\mathcal{O}(N)$ Overall?
At first glance, nested while loops look like $\mathcal{O}(N^2)$.
However, the `if (!num_set.count(num - 1))` guard ensures the inner loop ONLY runs for the very first element of each contiguous cluster.
Each number in the array is traversed at most twice (once in the outer loop, once in the inner loop).
Hence, amortized total operations is $2N = \mathcal{O}(N)$.
""",
    r"""# 04 Interview Follow-ups: Longest Consecutive Sequence

## 1. What if the Array is Distributed Across Multiple Machines?
- Use Disjoint Set Union (DSU) or Hash Partitioning:
  - Partition elements by range buckets $[K \cdot B, (K+1) \cdot B - 1]$.
  - Stitch boundary elements across adjacent partition machines via remote DSU queries.
"""
)

# 6. First Bad Version (LC #278)
write_problem(
    "Phase 03 Binary Search", "First Bad Version",
    r"""# First Bad Version

- **Platform**: LeetCode
- **Problem Number**: #278
- **Difficulty**: Easy
- **URL**: [LeetCode #278 - First Bad Version](https://leetcode.com/problems/first-bad-version/)

---

## Problem Statement

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have `n` versions `[1, 2, ..., n]` and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API `bool isBadVersion(version)` which returns whether `version` is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

---

## Examples

### Example 1
```text
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
```

---

## Constraints

- $1 \le \text{bad} \le n \le 2^{31} - 1$
""",
    r"""# First Bad Version - Brute Force

- **Problem Number**: 278
- **Platform**: LeetCode #278
- **Difficulty**: Easy
- **Pattern**: Linear Scan

---

## Algorithm

Iterate linearly from version $1$ to $n$. The first version where `isBadVersion(i) == true` is the answer.

---

## Code

```cpp
// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        for (int i = 1; i <= n; i++) {
            if (isBadVersion(i)) return i;
        }
        return n;
    }
};
```

---

## Time & Space Complexity

- **Time Complexity**: $\mathcal{O}(N)$ API calls.
- **Space Complexity**: $\mathcal{O}(1)$.
""",
    r"""# First Bad Version - Optimal Approach (Binary Search)

- **Problem Number**: 278
- **Platform**: LeetCode #278
- **Difficulty**: Easy
- **Pattern**: Lower Bound Binary Search

---

## Optimal Intuition

The versions represent a monotonic boolean predicate array `[F, F, ..., F, T, T, ..., T]`. We can find the transition boundary using Binary Search in $\mathcal{O}(\log N)$ API calls.

---

## Code

```cpp
class Solution {
public:
    int firstBadVersion(int n) {
        int left = 1, right = n;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (isBadVersion(mid)) {
                right = mid; // First bad could be mid or to the left
            } else {
                left = mid + 1; // Must be to the right
            }
        }
        return left;
    }
};
```

---

## Time & Space Complexity

- **Time Complexity**: $\mathcal{O}(\log N)$
- **Space Complexity**: $\mathcal{O}(1)$
""",
    r"""# First Bad Version - Deep Explanation

## Monotonicity & `left + (right - left) / 2`
Using `mid = left + (right - left) / 2` prevents 32-bit integer overflow when $n = 2^{31} - 1$.
The predicate `isBadVersion` is monotonically non-decreasing, ensuring binary search correctness.
""",
    r"""# 04 Interview Follow-ups: First Bad Version

## 1. Git Bisect Real-World Analogy
- `git bisect` uses this exact binary search algorithm over commit histories to find the regression commit introducing a bug in $\mathcal{O}(\log N)$ builds.
"""
)

print("Batch 1 completed!")
