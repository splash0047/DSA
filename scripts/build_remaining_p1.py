import os

BASE_DIR = r"c:\Users\Pinak chimurkar\DSA"
phase1_dir = os.path.join(BASE_DIR, "Phase 01 Two Pointers & Sliding Window")
os.makedirs(phase1_dir, exist_ok=True)

p1_problems = [
    # 017
    {
        "id": "017", "name": "Container With Most Water", "lc_num": 11, "difficulty": "Medium",
        "url": "https://leetcode.com/problems/container-with-most-water/",
        "q_statement": "You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i`-th line are `(i, 0)` and `(i, height[i])`. Find two lines that together with the x-axis form a container such that the container contains the most water. Return the maximum amount of water a container can store.",
        "examples": "Input: height = [1,8,6,2,5,4,8,3,7]\nOutput: 49\nExplanation: The max area is between index 1 (height 8) and index 8 (height 7), area = min(8, 7) * (8 - 1) = 7 * 7 = 49.",
        "constraints": "- n == height.length\n- 2 <= n <= 10^5\n- 0 <= height[i] <= 10^4",
        "bf_pattern": "Nested Loops / All Pairs",
        "bf_intuition": "Calculate area for every possible pair of lines (i, j) and track maximum area.",
        "bf_algo": "1. max_area = 0.\n2. Loop i from 0 to n-2, loop j from i+1 to n-1.\n3. area = min(height[i], height[j]) * (j - i).\n4. max_area = max(max_area, area).\n5. Return max_area.",
        "bf_code": "#include <vector>\n#include <algorithm>\nclass Solution {\npublic:\n    int maxArea(const std::vector<int>& height) {\n        int max_a = 0, n = height.size();\n        for (int i = 0; i < n - 1; ++i) {\n            for (int j = i + 1; j < n; ++j) {\n                int area = std::min(height[i], height[j]) * (j - i);\n                max_a = std::max(max_a, area);\n            }\n        }\n        return max_a;\n    }\n};",
        "bf_tc": "O(N^2)", "bf_sc": "O(1)",
        "bf_why_not_opt": "Quadratic time O(N^2). Two pointers from boundaries achieves linear O(N) time.",
        "opt_pattern": "Two Pointers (Shrinking Window)",
        "opt_concept": "Start at widest window (left=0, right=n-1). To potentially find larger area, move the pointer pointing to shorter line inward.",
        "opt_obs": "Area is constrained by shorter line height: min(h[left], h[right]) * width. Moving longer line inward can only decrease width without increasing height.",
        "opt_intuition": "Always advance pointer with smaller height because keeping smaller height while decreasing width can never yield a larger area.",
        "opt_algo": "1. left = 0, right = n - 1, max_area = 0.\n2. While left < right:\n   area = min(height[left], height[right]) * (right - left)\n   max_area = max(max_area, area)\n   if height[left] < height[right]: left++ else right--.\n3. Return max_area.",
        "opt_code": "#include <vector>\n#include <algorithm>\nclass Solution {\npublic:\n    int maxArea(const std::vector<int>& height) {\n        int left = 0, right = height.size() - 1;\n        int max_water = 0;\n        while (left < right) {\n            int width = right - left;\n            int current_height = std::min(height[left], height[right]);\n            max_water = std::max(max_water, current_height * width);\n            if (height[left] < height[right]) {\n                left++;\n            } else {\n                right--;\n            }\n        }\n        return max_water;\n    }\n};",
        "opt_dry_run": "[1,8,6,2,5,4,8,3,7] -> left=0(1), right=8(7) area=8*1=8 -> move left -> left=1(8), right=8(7) area=7*7=49 ...",
        "opt_tc": "O(N)", "opt_sc": "O(1)",
        "opt_why_opt": "Single pass O(N) time inspection of heights with constant O(1) space.",
        "opt_mistakes": "Moving the pointer with larger height or moving both pointers simultaneously.",
        "summary": "Find maximum water container area using two pointers shrinking from boundaries by always moving pointer with shorter line inward.",
        "pattern_rec": "Maximize area between array boundaries -> Two Pointers (Boundary Shrinking).",
        "clues": "Find 2 lines, width * min_height area formula, O(N) target.",
        "diagram": "L -> [1, 8, 6, 2, 5, 4, 8, 3, 7] <- R  (area = min(1,7)*8 = 8, move L)",
        "alt_sol": "Monotonic Stack / Segment Tree (unnecessary complexity).",
        "edge_cases": "Two elements ([1,1]), strictly increasing ([1,2,3,4]), strictly decreasing.",
        "tips": "Be ready to prove why skipping shorter line retains correctness.",
        "similar": "LeetCode #42: Trapping Rain Water, LeetCode #407: Trapping Rain Water II",
        "rev_notes": "left=0, right=n-1. While left<right: area = min(h[left], h[right])*(right-left). If h[left]<h[right] left++ else right--. O(N) time, O(1) space."
    },
    # 018
    {
        "id": "018", "name": "3Sum", "lc_num": 15, "difficulty": "Medium",
        "url": "https://leetcode.com/problems/3sum/",
        "q_statement": "Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`. The solution set must not contain duplicate triplets.",
        "examples": "Input: nums = [-1,0,1,2,-1,-4]\nOutput: [[-1,-1,2],[-1,0,1]]",
        "constraints": "- 3 <= nums.length <= 3000\n- -10^5 <= nums[i] <= 10^5",
        "bf_pattern": "Triple Nested Loops + Hash Set Deduplication",
        "bf_intuition": "Iterate all triplets (i, j, k), check if sum == 0, sort triplet and add to set to avoid duplicates.",
        "bf_algo": "1. Triple loop i, j, k.\n2. If nums[i]+nums[j]+nums[k] == 0: sort triplet and insert into std::set.\n3. Convert set to vector.",
        "bf_code": "#include <vector>\n#include <set>\n#include <algorithm>\nclass Solution {\npublic:\n    std::vector<std::vector<int>> threeSum(std::vector<int>& nums) {\n        std::set<std::vector<int>> res;\n        int n = nums.size();\n        for (int i = 0; i < n - 2; ++i) {\n            for (int j = i + 1; j < n - 1; ++j) {\n                for (int k = j + 1; k < n; ++k) {\n                    if (nums[i] + nums[j] + nums[k] == 0) {\n                        std::vector<int> triplet = {nums[i], nums[j], nums[k]};\n                        std::sort(triplet.begin(), triplet.end());\n                        res.insert(triplet);\n                    }\n                }\n            }
        }\n        return std::vector<std::vector<int>>(res.begin(), res.end());\n    }\n};",
        "bf_tc": "O(N^3 log K)", "bf_sc": "O(K) where K is number of triplets",
        "bf_why_not_opt": "Cubic time O(N^3). Sorting first allows reducing to O(N^2) time via two pointers.",
        "opt_pattern": "Sort + Two Pointers (Fixed Outer Loop)",
        "opt_concept": "Sort array. Fix first element `nums[i]`, then use Two Pointers (`left = i+1`, `right = n-1`) to find target `-nums[i]`.",
        "opt_obs": "After sorting, duplicate values are adjacent. Skipping duplicates at i, left, and right pointers prevents duplicate triplets without needing a set.",
        "opt_intuition": "Sort nums. For each i, if `nums[i] > 0` break (sum cannot be 0). Skip duplicate `nums[i] == nums[i-1]`. Run Two Sum II logic on remaining suffix.",
        "opt_algo": "1. Sort nums.\n2. Loop i from 0 to n-3:\n   a. If i > 0 and nums[i] == nums[i-1] continue.\n   b. left = i + 1, right = n - 1.\n   c. While left < right:\n      sum = nums[i] + nums[left] + nums[right]\n      if sum == 0: add triplet, left++, right++, skip duplicate left & right elements.\n      else if sum < 0: left++ else right--.\n3. Return triplets.",
        "opt_code": "#include <vector>\n#include <algorithm>\nclass Solution {\npublic:\n    std::vector<std::vector<int>> threeSum(std::vector<int>& nums) {\n        std::vector<std::vector<int>> result;\n        int n = nums.size();\n        std::sort(nums.begin(), nums.end());\n        \n        for (int i = 0; i < n - 2; ++i) {\n            if (nums[i] > 0) break;\n            if (i > 0 && nums[i] == nums[i - 1]) continue;\n            \n            int left = i + 1;\n            int right = n - 1;\n            while (left < right) {\n                int sum = nums[i] + nums[left] + nums[right];\n                if (sum == 0) {\n                    result.push_back({nums[i], nums[left], nums[right]});\n                    while (left < right && nums[left] == nums[left + 1]) left++;\n                    while (left < right && nums[right] == nums[right - 1]) right--;\n                    left++;\n                    right--;\n                } else if (sum < 0) {\n                    left++;\n                } else {\n                    right--;\n                }\n            }\n        }\n        return result;\n    }\n};",
        "opt_dry_run": "nums=[-4,-1,-1,0,1,2] -> i=0(-4) no match -> i=1(-1) L=2(-1), R=5(2) sum=0 -> add [-1,-1,2]...",
        "opt_tc": "O(N^2)", "opt_sc": "O(1) extra space excluding result array",
        "opt_why_opt": "Optimal O(N^2) time for 3Sum problem (3Sum hard lower bound under 3SUM conjecture is O(N^2)).",
        "opt_mistakes": "Not skipping duplicate elements causing duplicate triplets, missing `nums[i] > 0` early exit.",
        "summary": "Find all unique triplets summing to 0 by sorting the array and running Two Pointers for each fixed element in O(N^2) time.",
        "pattern_rec": "Triplet sum -> Sort + Fixed Element + Two Pointers.",
        "clues": "3 elements sum to 0, no duplicate triplets, sorted array processing.",
        "diagram": "Sort: [-4, -1, -1, 0, 1, 2]\ni=-1 -> L=-1, R=2 -> sum = -1 + -1 + 2 = 0 (Found!)",
        "alt_sol": "Hash Map for target - (nums[i] + nums[j]).",
        "edge_cases": "All zeroes ([0,0,0,0]), no triplets, less than 3 elements.", "tips": "Be thorough when explaining duplicate skip conditions (`while (left < right && nums[left] == nums[left+1]) left++`).",
        "similar": "LeetCode #1, #16, #18, #611",
        "rev_notes": "Sort. Loop i=0..n-3. Skip duplicate nums[i]. left=i+1, right=n-1. Sum==0 -> push triplet & skip duplicate left/right. O(N^2) time, O(1) space."
    },
    # 019
    {
        "id": "019", "name": "4Sum", "lc_num": 18, "difficulty": "Medium",
        "url": "https://leetcode.com/problems/4sum/",
        "q_statement": "Given an array `nums` of `n` integers, return an array of all the **unique** quadruplets `[nums[a], nums[b], nums[c], nums[d]]` such that `nums[a] + nums[b] + nums[c] + nums[d] == target`.",
        "examples": "Input: nums = [1,0,-1,0,-2,2], target = 0\nOutput: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]",
        "constraints": "- 1 <= nums.length <= 200\n- -10^9 <= nums[i], target <= 10^9",
        "bf_pattern": "Quadruple Loops + Set Deduplication",
        "bf_intuition": "Four nested loops checking all combinations.",
        "bf_algo": "1. Four nested loops i, j, k, l.\n2. If sum == target, insert sorted quadruplet into set.",
        "bf_code": "#include <vector>\n#include <set>\n#include <algorithm>\nclass Solution {\npublic:\n    std::vector<std::vector<int>> fourSum(std::vector<int>& nums, int target) {\n        std::set<std::vector<int>> res;\n        int n = nums.size();\n        for (int i = 0; i < n - 3; ++i)\n            for (int j = i + 1; j < n - 2; ++j)\n                for (int k = j + 1; k < n - 1; ++k)\n                    for (int l = k + 1; l < n; ++l)\n                        if ((long long)nums[i] + nums[j] + nums[k] + nums[l] == target) {\n                            std::vector<int> quad = {nums[i], nums[j], nums[k], nums[l]};\n                            std::sort(quad.begin(), quad.end());\n                            res.insert(quad);\n                        }\n        return std::vector<std::vector<int>>(res.begin(), res.end());\n    }\n};",
        "bf_tc": "O(N^4)", "bf_sc": "O(K)", "bf_why_not_opt": "O(N^4) is too slow. Sorting + Two Nested Loops + Two Pointers achieves O(N^3).",
        "opt_pattern": "Sort + Two Fixed Loops + Two Pointers (K-Sum Generalization)",
        "opt_concept": "Sort array. Fix first two elements i and j, use Two Pointers for remaining two elements.",
        "opt_obs": "Same duplicate skipping principle as 3Sum extended to two outer loops.",
        "opt_intuition": "Sort nums. Loop i, skip duplicate nums[i]. Loop j, skip duplicate nums[j]. Run Two Pointers for remaining sum.",
        "opt_algo": "1. Sort nums.\n2. Loop i from 0 to n-4 (skip duplicates).\n3. Loop j from i+1 to n-3 (skip duplicates).\n4. left = j+1, right = n-1. Use long long for sum to prevent integer overflow.\n5. Move pointers based on comparison with target.",
        "opt_code": "#include <vector>\n#include <algorithm>\nclass Solution {\npublic:\n    std::vector<std::vector<int>> fourSum(std::vector<int>& nums, int target) {\n        std::vector<std::vector<int>> result;\n        int n = nums.size();
        if (n < 4) return result;\n        std::sort(nums.begin(), nums.end());\n        \n        for (int i = 0; i < n - 3; ++i) {\n            if (i > 0 && nums[i] == nums[i - 1]) continue;\n            for (int j = i + 1; j < n - 2; ++j) {\n                if (j > i + 1 && nums[j] == nums[j - 1]) continue;\n                int left = j + 1, right = n - 1;\n                while (left < right) {\n                    long long sum = (long long)nums[i] + nums[j] + nums[left] + nums[right];\n                    if (sum == target) {\n                        result.push_back({nums[i], nums[j], nums[left], nums[right]});\n                        while (left < right && nums[left] == nums[left + 1]) left++;\n                        while (left < right && nums[right] == nums[right - 1]) right--;\n                        left++; right--;\n                    } else if (sum < target) left++;\n                    else right--;\n                }\n            }\n        }\n        return result;\n    }\n};",
        "opt_dry_run": "nums=[-2,-1,0,0,1,2], target=0 -> i=0(-2), j=1(-1) -> L=2(0), R=5(2) sum=0 -> [-2,-1,0,2]",
        "opt_tc": "O(N^3)", "opt_sc": "O(1) extra space", "opt_why_opt": "Optimal O(N^3) complexity for 4Sum using two pointers.",
        "opt_mistakes": "Integer overflow during sum calculation (must cast to long long).",
        "summary": "Find all unique quadruplets summing to target by sorting array, fixing 2 elements, and using Two Pointers in O(N^3) time.",
        "pattern_rec": "Quadruplet sum -> Sort + 2 Outer Loops + Two Pointers.",
        "clues": "4 elements, target sum, integer overflow potential.",
        "diagram": "i fixed -> j fixed -> Two Pointers L & R scan remaining array",
        "alt_sol": "Recursive K-Sum solver.",
        "edge_cases": "Less than 4 elements, integer overflow with large values.", "tips": "Cast sum calculation to long long.",
        "similar": "LeetCode #15: 3Sum, LeetCode #454: 4Sum II",
        "rev_notes": "Sort. Loop i, loop j (skip duplicates). Two pointers left=j+1, right=n-1. Use long long sum. O(N^3) time, O(1) space."
    },
    # 020
    {
        "id": "020", "name": "Sort Colors", "lc_num": 75, "difficulty": "Medium",
        "url": "https://leetcode.com/problems/sort-colors/",
        "q_statement": "Given an array `nums` with `n` objects colored red, white, or blue, sort them **in-place** so that objects of the same color are adjacent, with the colors in the order red (0), white (1), and blue (2). You must solve this problem without using the library's sort function.",
        "examples": "Input: nums = [2,0,2,1,1,0]\nOutput: [0,0,1,1,2,2]",
        "constraints": "- n == nums.length\n- 1 <= n <= 300\n- nums[i] is either 0, 1, or 2.",
        "bf_pattern": "Counting Sort (Two-Pass)",
        "bf_intuition": "Count frequencies of 0s, 1s, and 2s in first pass, then overwrite array in second pass.",
        "bf_algo": "1. c0=0, c1=0, c2=0.\n2. Count occurrences of 0, 1, 2.\n3. Overwrite nums with c0 zeroes, c1 ones, c2 twos.",
        "bf_code": "#include <vector>\nclass Solution {\npublic:\n    void sortColors(std::vector<int>& nums) {\n        int c0 = 0, c1 = 0, c2 = 0;\n        for (int x : nums) {\n            if (x == 0) c0++;\n            else if (x == 1) c1++;\n            else c2++;\n        }\n        int idx = 0;\n        while (c0--) nums[idx++] = 0;\n        while (c1--) nums[idx++] = 1;\n        while (c2--) nums[idx++] = 2;\n    }\n};",
        "bf_tc": "O(N) (Two Passes)", "bf_sc": "O(1)", "bf_why_not_opt": "Takes two passes. Dutch National Flag algorithm solves in one pass.",
        "opt_pattern": "Dutch National Flag Algorithm (Three Pointers)",
        "opt_concept": "Maintain 3 pointers: `low` (boundary for 0s), `mid` (current element), `high` (boundary for 2s).",
        "opt_obs": "Array is partitioned into 4 zones: [0...low-1] are 0s, [low...mid-1] are 1s, [mid...high] are unclassified, [high+1...n-1] are 2s.",
        "opt_intuition": "Process nums[mid]: If 0, swap(nums[low], nums[mid]), low++, mid++. If 1, mid++. If 2, swap(nums[mid], nums[high]), high--.",
        "opt_algo": "1. low = 0, mid = 0, high = n - 1.\n2. While mid <= high:\n   if nums[mid] == 0: swap(nums[low++], nums[mid++])\n   else if nums[mid] == 1: mid++\n   else: swap(nums[mid], nums[high--]).",
        "opt_code": "#include <vector>\n#include <algorithm>\nclass Solution {\npublic:\n    void sortColors(std::vector<int>& nums) {\n        int low = 0, mid = 0, high = nums.size() - 1;\n        while (mid <= high) {\n            if (nums[mid] == 0) {\n                std::swap(nums[low++], nums[mid++]);\n            } else if (nums[mid] == 1) {\n                mid++;\n            } else {\n                std::swap(nums[mid], nums[high--]);\n            }\n        }\n    }\n};",
        "opt_dry_run": "[2,0,2,1,1,0] -> swap(0,5)->[0,0,2,1,1,2] high=4 ... -> [0,0,1,1,2,2]",
        "opt_tc": "O(N) (Single Pass)", "opt_sc": "O(1)", "opt_why_opt": "Single pass partition in O(N) time with O(1) space.",
        "opt_mistakes": "Incrementing `mid` when swapping with `high` (swapped element from `high` is unexamined and must be checked at current `mid`).",
        "summary": "Sort array of 0s, 1s, 2s in single pass using Dutch National Flag 3-pointer algorithm in O(N) time.",
        "pattern_rec": "3-way partitioning of array -> Dutch National Flag Algorithm.",
        "clues": "3 distinct values (0, 1, 2), in-place single pass requirement.",
        "diagram": "[0..low-1: 0s] | [low..mid-1: 1s] | [mid..high: Unknown] | [high+1..n-1: 2s]",
        "alt_sol": "Counting Sort (2 passes).",
        "edge_cases": "All elements identical ([0,0,0]), already sorted ([0,1,2]), single element.",
        "tips": "Emphasize why mid is NOT incremented when swapping with high.",
        "similar": "LeetCode #280, #324",
        "rev_notes": "low=0, mid=0, high=n-1. While mid<=high: 0->swap(low++, mid++); 1->mid++; 2->swap(mid, high--). O(N) single pass, O(1) space."
    }
]

# Write Phase 1 problems
for p_data in p1_problems:
    p_folder = os.path.join(phase1_dir, f"{p_data['id']} {p_data['name']}")
    os.makedirs(p_folder, exist_ok=True)
    
    with open(os.path.join(p_folder, "00_Question.md"), "w", encoding="utf-8") as f:
        f.write(f"# {p_data['id']}. {p_data['name']}\n\n- **Platform**: LeetCode\n- **Problem Number**: #{p_data['lc_num']}\n- **Difficulty**: {p_data['difficulty']}\n- **URL**: [{p_data['name']}]({p_data['url']})\n\n---\n\n## Problem Statement\n\n{p_data['q_statement']}\n\n---\n\n## Examples\n\n{p_data['examples']}\n\n---\n\n## Constraints\n\n{p_data['constraints']}\n")
        
    with open(os.path.join(p_folder, "01_Brute_Force.md"), "w", encoding="utf-8") as f:
        f.write(f"# {p_data['name']}\n\n- **Problem Number**: {p_data['lc_num']}\n- **Platform**: LeetCode #{p_data['lc_num']}\n- **Difficulty**: {p_data['difficulty']}\n- **Pattern**: {p_data['bf_pattern']}\n\n---\n\n## Brute Force Intuition\n\n{p_data['bf_intuition']}\n\n---\n\n## Algorithm\n\n{p_data['bf_algo']}\n\n---\n\n## Code\n\n```cpp\n{p_data['bf_code']}\n```\n\n---\n\n## Time Complexity\n\n- **Time Complexity**: {p_data['bf_tc']}\n\n---\n\n## Space Complexity\n\n- **Space Complexity**: {p_data['bf_sc']}\n\n---\n\n## Why This Approach Is Not Optimal\n\n{p_data['bf_why_not_opt']}\n")

    with open(os.path.join(p_folder, "02_Optimal_Approach.md"), "w", encoding="utf-8") as f:
        f.write(f"# {p_data['name']}\n\n## Pattern Used\n\n- **Pattern**: **{p_data['opt_pattern']}**\n- **Concept**: {p_data['opt_concept']}\n\n---\n\n## Observation\n\n{p_data['opt_obs']}\n\n---\n\n## Intuition\n\n{p_data['opt_intuition']}\n\n---\n\n## Algorithm\n\n{p_data['opt_algo']}\n\n---\n\n## Clean C++17 Solution\n\n```cpp\n{p_data['opt_code']}\n```\n\n---\n\n## Dry Run\n\n{p_data['opt_dry_run']}\n\n---\n\n## Time Complexity\n\n- **Time Complexity**: {p_data['opt_tc']}\n\n---\n\n## Space Complexity\n\n- **Space Complexity**: {p_data['opt_sc']}\n\n---\n\n## Why This is Optimal\n\n{p_data['opt_why_opt']}\n\n---\n\n## Common Mistakes\n\n{p_data['opt_mistakes']}\n")

    with open(os.path.join(p_folder, "03_Explanation.md"), "w", encoding="utf-8") as f:
        f.write(f"# Problem Summary\n\n{p_data['summary']}\n\n---\n\n## Pattern Recognition\n\n{p_data['pattern_rec']}\n\n---\n\n## Important Clues\n\n{p_data['clues']}\n\n---\n\n## Example\n\n```text\n{p_data['diagram']}\n```\n\n---\n\n## Alternative Solutions\n\n{p_data['alt_sol']}\n\n---\n\n## Edge Cases\n\n{p_data['edge_cases']}\n\n---\n\n## Interview Tips\n\n{p_data['tips']}\n\n---\n\n## Similar Problems\n\n{p_data['similar']}\n\n---\n\n## Revision Notes\n\n{p_data['rev_notes']}\n")

print("Generated problems 017 to 020!")
