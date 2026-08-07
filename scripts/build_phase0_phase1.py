import os
import sys

BASE_DIR = r"c:\Users\Pinak chimurkar\DSA"

phase0_dir = os.path.join(BASE_DIR, "Phase 00 Programming Foundation")
phase1_dir = os.path.join(BASE_DIR, "Phase 01 Two Pointers & Sliding Window")

os.makedirs(phase0_dir, exist_ok=True)
os.makedirs(phase1_dir, exist_ok=True)

problems_phase0 = [
    {
        "id": "003",
        "name": "Best Time to Buy and Sell Stock",
        "lc_num": 121,
        "difficulty": "Easy",
        "url": "https://leetcode.com/problems/best-time-to-buy-and-sell-stock/",
        "q_statement": "You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`-th day. You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.",
        "examples": "Example 1:\nInput: prices = [7,1,5,3,6,4]\nOutput: 5\nExplanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.\n\nExample 2:\nInput: prices = [7,6,4,3,1]\nOutput: 0\nExplanation: In this case, no transactions are done and max profit = 0.",
        "constraints": "- 1 <= prices.length <= 10^5\n- 0 <= prices[i] <= 10^4",
        "bf_pattern": "Nested Loops / Brute Force Pair Comparison",
        "bf_intuition": "To find the maximum profit, we can compare every possible pair of buy day `i` and sell day `j` (where `j > i`) and calculate `prices[j] - prices[i]`. We keep track of the maximum profit found.",
        "bf_algo": "1. Initialize `max_profit = 0`.\n2. Outer loop `i` from `0` to `n-2` (buy day).\n3. Inner loop `j` from `i+1` to `n-1` (sell day).\n4. Update `max_profit = max(max_profit, prices[j] - prices[i])`.\n5. Return `max_profit`.",
        "bf_code": """#include <vector>
#include <algorithm>

class Solution {
public:
    int maxProfit(const std::vector<int>& prices) {
        int max_profit = 0;
        int n = prices.size();
        for (int i = 0; i < n - 1; ++i) {
            for (int j = i + 1; j < n; ++j) {
                int profit = prices[j] - prices[i];
                if (profit > max_profit) {
                    max_profit = profit;
                }
            }
        }
        return max_profit;
    }
};""",
        "bf_tc": "O(N^2)",
        "bf_sc": "O(1)",
        "bf_why_not_opt": "We perform O(N^2) comparisons by re-checking every pair. Instead of scanning all future sell days for a buy day, we can keep track of the minimum buy price seen so far in a single pass.",
        "opt_pattern": "Single Pass Tracking / Greedy Min-Element",
        "opt_concept": "Maintaining a running minimum purchase price `min_price` as we traverse the stock prices. The maximum profit on day `i` is `prices[i] - min_price`.",
        "opt_obs": "Selling on day `i` is optimal if we bought at the minimum price among all days `0` to `i-1`.",
        "opt_intuition": "As you walk through the price array, track the lowest price seen so far. At each price, check how much profit you would make if you sold today. Update your global max profit accordingly.",
        "opt_algo": "1. Initialize `min_price = INT_MAX` and `max_profit = 0`.\n2. Traverse each `price` in `prices`:\n   a. `min_price = min(min_price, price)`\n   b. `max_profit = max(max_profit, price - min_price)`\n3. Return `max_profit`.",
        "opt_code": """#include <vector>
#include <algorithm>
#include <climits>

class Solution {
public:
    int maxProfit(const std::vector<int>& prices) {
        int min_price = INT_MAX;
        int max_profit = 0;
        
        for (int price : prices) {
            if (price < min_price) {
                min_price = price;
            } else if (price - min_price > max_profit) {
                max_profit = price - min_price;
            }
        }
        
        return max_profit;
    }
};""",
        "opt_dry_run": "| Step | price | min_price | current profit | max_profit |\n|---|---|---|---|---|\n| 1 | 7 | 7 | 0 | 0 |\n| 2 | 1 | 1 | 0 | 0 |\n| 3 | 5 | 1 | 4 | 4 |\n| 4 | 3 | 1 | 2 | 4 |\n| 5 | 6 | 1 | 5 | 5 |\n| 6 | 4 | 1 | 3 | 5 |",
        "opt_tc": "O(N)",
        "opt_sc": "O(1)",
        "opt_why_opt": "We must inspect each price at least once (O(N) lower bound). Single pass with O(1) auxiliary variables achieves optimal time and space.",
        "opt_mistakes": "1. Allowing sell day to precede buy day.\n2. Initializing `min_price` to `0` instead of `INT_MAX` or `prices[0]`.\n3. Resetting `min_price` incorrectly.",
        "summary": "Find maximum difference `prices[j] - prices[i]` with `j > i`. Track running minimum price seen so far and update max profit at each step in O(N) time and O(1) space.",
        "pattern_rec": "Single transaction maximum profit in a sequence -> Running minimum prefix tracking.",
        "clues": "Must buy before selling, single transaction allowed, array unsorted over time.",
        "diagram": "prices: [7,  1,  5,  3,  6,  4]\nmin_p:   7   1   1   1   1   1\nprofit:  0   0   4   2   5   3 -> Max = 5",
        "alt_sol": "Kadane's Algorithm on daily differences `diff[i] = prices[i] - prices[i-1]`.",
        "edge_cases": "Strictly decreasing prices ([5,4,3,2,1] -> 0), single element array ([5] -> 0), identical prices ([3,3,3] -> 0).",
        "tips": "Discuss Kadane's algorithm connection and why tracking min element is simpler.",
        "similar": "1. LeetCode #122: Best Time to Buy and Sell Stock II\n2. LeetCode #123: Best Time to Buy and Sell Stock III\n3. LeetCode #188: Best Time to Buy and Sell Stock IV\n4. LeetCode #309: Best Time to Buy and Sell Stock with Cooldown\n5. LeetCode #53: Maximum Subarray",
        "rev_notes": "Track min_price and max_profit in single loop. O(N) time, O(1) space. Update min_price if current < min_price, else update max_profit."
    },
    {
        "id": "004",
        "name": "Contains Duplicate",
        "lc_num": 217,
        "difficulty": "Easy",
        "url": "https://leetcode.com/problems/contains-duplicate/",
        "q_statement": "Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.",
        "examples": "Example 1:\nInput: nums = [1,2,3,1]\nOutput: true\n\nExample 2:\nInput: nums = [1,2,3,4]\nOutput: false\n\nExample 3:\nInput: nums = [1,1,1,3,3,4,3,2,4,2]\nOutput: true",
        "constraints": "- 1 <= nums.length <= 10^5\n- -10^9 <= nums[i] <= 10^9",
        "bf_pattern": "Nested Loops / All-Pairs Comparison",
        "bf_intuition": "Compare every element with every other element to see if any pair is equal.",
        "bf_algo": "1. Loop `i` from `0` to `n-2`.\n2. Loop `j` from `i+1` to `n-1`.\n3. If `nums[i] == nums[j]`, return `true`.\n4. Return `false`.",
        "bf_code": """#include <vector>

class Solution {
public:
    bool containsDuplicate(const std::vector<int>& nums) {
        int n = nums.size();
        for (int i = 0; i < n - 1; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (nums[i] == nums[j]) {
                    return true;
                }
            }
        }
        return false;
    }
};""",
        "bf_tc": "O(N^2)",
        "bf_sc": "O(1)",
        "bf_why_not_opt": "Checking every pair takes quadratic time. We can trade space for time using a Hash Set to check duplicates in O(1) average time per element.",
        "opt_pattern": "Hash Set Lookup",
        "opt_concept": "Inserting elements into `std::unordered_set` and checking for existing presence.",
        "opt_obs": "If an element is already present in the set during insertion, a duplicate exists.",
        "opt_intuition": "Maintain a set of seen numbers. For each number in the array, if it's in the set, we found a duplicate. Otherwise, add it to the set.",
        "opt_algo": "1. Initialize empty `std::unordered_set<int> seen`.\n2. For each `num` in `nums`:\n   a. If `seen.count(num)` > 0, return `true`.\n   b. Insert `num` into `seen`.\n3. Return `false`.",
        "opt_code": """#include <vector>
#include <unordered_set>

class Solution {
public:
    bool containsDuplicate(const std::vector<int>& nums) {
        std::unordered_set<int> seen;
        for (int num : nums) {
            if (seen.find(num) != seen.end()) {
                return true;
            }
            seen.insert(num);
        }
        return false;
    }
};""",
        "opt_dry_run": "| Step | num | seen map | Found? | Action |\n|---|---|---|---|---|\n| 1 | 1 | {} | No | Insert 1 |\n| 2 | 2 | {1} | No | Insert 2 |\n| 3 | 3 | {1,2} | No | Insert 3 |\n| 4 | 1 | {1,2,3} | **Yes** | Return true |",
        "opt_tc": "O(N)",
        "opt_sc": "O(N)",
        "opt_why_opt": "We visit each element once. Hash set operations are O(1) on average. Overall O(N) time and O(N) space.",
        "opt_mistakes": "1. Forgetting average vs worst-case hash set performance.\n2. Not knowing sorting alternative O(N log N) time with O(1) extra space.",
        "summary": "Determine if any element appears at least twice. Use an unordered hash set to detect duplicate values in O(N) time and O(N) space.",
        "pattern_rec": "Uniqueness / frequency check -> Hash Set or Sorting.",
        "clues": "Check if distinct, unsorted input, return boolean.",
        "diagram": "nums = [1, 2, 3, 1]\nseen = {1, 2, 3} -> 1 already seen -> return true",
        "alt_sol": "Sorting first: `std::sort` array in O(N log N) time and check adjacent elements in O(1) space.",
        "edge_cases": "Single element array ([1] -> false), all identical elements ([2,2,2] -> true), negative numbers ([-1,-1] -> true).",
        "tips": "Mention trade-off between Hash Set (O(N) time, O(N) space) and Sorting (O(N log N) time, O(1) space).",
        "similar": "1. LeetCode #219: Contains Duplicate II\n2. LeetCode #220: Contains Duplicate III\n3. LeetCode #136: Single Number\n4. LeetCode #448: Find All Numbers Disappeared in an Array\n5. LeetCode #287: Find the Duplicate Number",
        "rev_notes": "Hash set approach: insert while scanning. If found in set -> return true. O(N) time, O(N) space. Sorting alternative: O(N log N) time, O(1) space."
    },
    {
        "id": "005",
        "name": "Majority Element",
        "lc_num": 169,
        "difficulty": "Easy",
        "url": "https://leetcode.com/problems/majority-element/",
        "q_statement": "Given an array `nums` of size `n`, return the majority element. The majority element is the element that appears **more than `⌊n / 2⌋` times**. You may assume that the majority element always exists in the array.",
        "examples": "Example 1:\nInput: nums = [3,2,3]\nOutput: 3\n\nExample 2:\nInput: nums = [2,2,1,1,1,2,2]\nOutput: 2",
        "constraints": "- n == nums.length\n- 1 <= n <= 5 * 10^4\n- -10^9 <= nums[i] <= 10^9",
        "bf_pattern": "Frequency Counting via Nested Loops / HashMap",
        "bf_intuition": "Count the frequency of each element using a hash map or nested loops and return the one with count > n/2.",
        "bf_algo": "1. Create hash map `counts`.\n2. Count frequency of each number in `nums`.\n3. Return the number with count > n/2.",
        "bf_code": """#include <vector>
#include <unordered_map>

class Solution {
public:
    int majorityElement(const std::vector<int>& nums) {
        std::unordered_map<int, int> counts;
        int n = nums.size();
        for (int num : nums) {
            counts[num]++;
            if (counts[num] > n / 2) {
                return num;
            }
        }
        return -1;
    }
};""",
        "bf_tc": "O(N)",
        "bf_sc": "O(N)",
        "bf_why_not_opt": "Using a hash map takes O(N) auxiliary space. Boyer-Moore Voting Algorithm allows finding the majority element in O(1) space.",
        "opt_pattern": "Boyer-Moore Voting Algorithm",
        "opt_concept": "Canceling out distinct element pairs. Since majority element occurs > n/2 times, it will remain after canceling out all other pairs.",
        "opt_obs": "If we pair up different elements and remove them, the majority element will always be the last candidate standing.",
        "opt_intuition": "Maintain a `candidate` and a `count`. When `count == 0`, set candidate to current element. If current element equals candidate, increment count; otherwise decrement count.",
        "opt_algo": "1. Initialize `candidate = 0`, `count = 0`.\n2. For each `num` in `nums`:\n   a. If `count == 0`, `candidate = num`.\n   b. If `num == candidate`, `count++`, else `count--`.\n3. Return `candidate`.",
        "opt_code": """#include <vector>

class Solution {
public:
    int majorityElement(const std::vector<int>& nums) {
        int candidate = 0;
        int count = 0;
        
        for (int num : nums) {
            if (count == 0) {
                candidate = num;
            }
            count += (num == candidate) ? 1 : -1;
        }
        
        return candidate;
    }
};""",
        "opt_dry_run": "| Step | num | candidate | count |\n|---|---|---|---|\n| 1 | 2 | 2 | 1 |\n| 2 | 2 | 2 | 2 |\n| 3 | 1 | 2 | 1 |\n| 4 | 1 | 2 | 0 |\n| 5 | 1 | 1 | 1 |\n| 6 | 2 | 1 | 0 |\n| 7 | 2 | 2 | 1 |",
        "opt_tc": "O(N)",
        "opt_sc": "O(1)",
        "opt_why_opt": "O(N) time to scan array once, O(1) space without extra data structures. Optimal bound.",
        "opt_mistakes": "1. Resetting candidate at wrong condition.\n2. Not verifying candidate when majority element presence is not guaranteed (here it is guaranteed).",
        "summary": "Find element appearing > n/2 times. Boyer-Moore Voting Algorithm tracks candidate and count, canceling opposing pairs to find result in O(N) time and O(1) space.",
        "pattern_rec": "Element count > n/2 -> Boyer-Moore Voting Algorithm.",
        "clues": "Majority element > n/2 guaranteed to exist, O(1) space follow-up.",
        "diagram": "nums = [2,2,1,1,1,2,2]\n[2,2] (cnt=2) -> [2,2,1] (cnt=1) -> [2,2,1,1] (cnt=0) -> [1] (cnt=1) ... -> candidate 2",
        "alt_sol": "Sorting: Sort `nums` and return `nums[n/2]`. Time O(N log N), Space O(1) or O(N).",
        "edge_cases": "Single element array ([1] -> 1), all identical ([5,5,5] -> 5).",
        "tips": "Be ready to explain why candidate cancels out minority elements mathematically.",
        "similar": "1. LeetCode #229: Majority Element II\n2. LeetCode #1150: Check If a Number Is Majority Element in a Sorted Array\n3. LeetCode #274: H-Index\n4. LeetCode #136: Single Number\n5. LeetCode #692: Top K Frequent Words",
        "rev_notes": "Boyer-Moore Voting: candidate & count. count==0 -> candidate=num. num==candidate ? count++ : count--. O(N) time, O(1) space."
    }
]

def make_problem_files(p_data, target_dir):
    p_folder = os.path.join(target_dir, f"{p_data['id']} {p_data['name']}")
    os.makedirs(p_folder, exist_ok=True)
    
    # 00_Question.md
    q_content = f"""# {p_data['id']}. {p_data['name']}

- **Platform**: LeetCode
- **Problem Number**: #{p_data['lc_num']}
- **Difficulty**: {p_data['difficulty']}
- **URL**: [{p_data['name']}]({p_data['url']})

---

## Problem Statement

{p_data['q_statement']}

---

## Examples

{p_data['examples']}

---

## Constraints

{p_data['constraints']}
"""
    with open(os.path.join(p_folder, "00_Question.md"), "w", encoding="utf-8") as f:
        f.write(q_content)
        
    # 01_Brute_Force.md
    bf_content = f"""# {p_data['name']}

- **Problem Number**: {p_data['lc_num']}
- **Platform**: LeetCode #{p_data['lc_num']}
- **Difficulty**: {p_data['difficulty']}
- **Pattern**: {p_data['bf_pattern']}

---

## Brute Force Intuition

{p_data['bf_intuition']}

---

## Algorithm

{p_data['bf_algo']}

---

## Code

```cpp
{p_data['bf_code']}
```

---

## Time Complexity

- **Time Complexity**: {p_data['bf_tc']}

---

## Space Complexity

- **Space Complexity**: {p_data['bf_sc']}

---

## Why This Approach Is Not Optimal

{p_data['bf_why_not_opt']}
"""
    with open(os.path.join(p_folder, "01_Brute_Force.md"), "w", encoding="utf-8") as f:
        f.write(bf_content)

    # 02_Optimal_Approach.md
    opt_content = f"""# {p_data['name']}

## Pattern Used

- **Pattern**: **{p_data['opt_pattern']}**
- **Concept**: {p_data['opt_concept']}

---

## Observation

{p_data['opt_obs']}

---

## Intuition

{p_data['opt_intuition']}

---

## Algorithm

{p_data['opt_algo']}

---

## Clean C++17 Solution

```cpp
{p_data['opt_code']}
```

---

## Dry Run

{p_data['opt_dry_run']}

---

## Time Complexity

- **Time Complexity**: {p_data['opt_tc']}

---

## Space Complexity

- **Space Complexity**: {p_data['opt_sc']}

---

## Why This is Optimal

{p_data['opt_why_opt']}

---

## Common Mistakes

{p_data['opt_mistakes']}
"""
    with open(os.path.join(p_folder, "02_Optimal_Approach.md"), "w", encoding="utf-8") as f:
        f.write(opt_content)

    # 03_Explanation.md
    exp_content = f"""# Problem Summary

{p_data['summary']}

---

## Pattern Recognition

{p_data['pattern_rec']}

---

## Important Clues

{p_data['clues']}

---

## Example

```text
{p_data['diagram']}
```

---

## Alternative Solutions

{p_data['alt_sol']}

---

## Edge Cases

{p_data['edge_cases']}

---

## Interview Tips

{p_data['tips']}

---

## Similar Problems

{p_data['similar']}

---

## Revision Notes

{p_data['rev_notes']}
"""
    with open(os.path.join(p_folder, "03_Explanation.md"), "w", encoding="utf-8") as f:
        f.write(exp_content)
    print(f"Generated {p_data['id']} {p_data['name']}")

for p in problems_phase0:
    make_problem_files(p, phase0_dir)

print("Phase 0 initial batch generated!")
