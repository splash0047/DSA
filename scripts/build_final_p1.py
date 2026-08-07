import os

BASE_DIR = r"c:\Users\Pinak chimurkar\DSA"
phase1_dir = os.path.join(BASE_DIR, "Phase 01 Two Pointers & Sliding Window")
os.makedirs(phase1_dir, exist_ok=True)

p1_final = [
    # 021
    {
        "id": "021", "name": "Remove Nth Node From End of List", "lc_num": 19, "difficulty": "Medium",
        "url": "https://leetcode.com/problems/remove-nth-node-from-end-of-list/",
        "q_statement": "Given the `head` of a linked list, remove the `n`-th node from the end of the list and return its head.",
        "examples": "Input: head = [1,2,3,4,5], n = 2\nOutput: [1,2,3,5]",
        "constraints": "- 1 <= sz <= 30\n- 0 <= Node.val <= 100\n- 1 <= n <= sz",
        "bf_pattern": "Two-Pass Length Calculation",
        "bf_intuition": "First pass calculates total length L. Second pass traverses to position L - n and updates next pointer.",
        "bf_algo": "1. Calculate length L of linked list.\n2. If n == L, return head->next.\n3. Traverse to (L - n - 1)-th node and delete target node.",
        "bf_code": "struct ListNode { int val; ListNode *next; ListNode(int x) : val(x), next(nullptr) {} };\nclass Solution {\npublic:\n    ListNode* removeNthFromEnd(ListNode* head, int n) {\n        int length = 0;\n        ListNode* curr = head;\n        while (curr) { length++; curr = curr->next; }\n        if (n == length) return head->next;\n        curr = head;\n        for (int i = 0; i < length - n - 1; ++i) curr = curr->next;\n        curr->next = curr->next->next;\n        return head;\n    }\n};",
        "bf_tc": "O(N) (Two Passes)", "bf_sc": "O(1)",
        "bf_why_not_opt": "Requires two passes over linked list. Fast and Slow pointers allow one-pass deletion.",
        "opt_pattern": "Two Pointers (Fast & Slow Gap of N)",
        "opt_concept": "Advance fast pointer n steps ahead. Then move both fast and slow pointers together until fast reaches end.",
        "opt_obs": "When fast pointer reaches end, slow pointer will be positioned right before the N-th node from end.",
        "opt_intuition": "Use a dummy node pointing to head to cleanly handle deleting the head node itself.",
        "opt_algo": "1. Dummy node pointing to head.\n2. Advance fast pointer n+1 steps from dummy.\n3. Move fast and slow together until fast is null.\n4. slow->next = slow->next->next.\n5. Return dummy->next.",
        "opt_code": "struct ListNode { int val; ListNode *next; ListNode(int x) : val(x), next(nullptr) {} };\nclass Solution {\npublic:\n    ListNode* removeNthFromEnd(ListNode* head, int n) {\n        ListNode dummy(0);\n        dummy.next = head;\n        ListNode* fast = &dummy;\n        ListNode* slow = &dummy;\n        for (int i = 0; i <= n; ++i) fast = fast->next;\n        while (fast != nullptr) {\n            fast = fast->next;\n            slow = slow->next;\n        }\n        slow->next = slow->next->next;\n        return dummy.next;\n    }\n};",
        "opt_dry_run": "dummy->1->2->3->4->5, n=2 -> fast moved 3 steps to 3 -> move together -> slow at 3 -> delete 4 -> return 1->2->3->5",
        "opt_tc": "O(N) (Single Pass)", "opt_sc": "O(1)",
        "opt_why_opt": "Single pass linked list traversal in O(N) time and O(1) space.",
        "opt_mistakes": "Forgetting dummy node causing segmentation fault when deleting head node (n = length).",
        "summary": "Delete N-th node from end of linked list in single pass using Fast and Slow pointers separated by N steps.",
        "pattern_rec": "N-th element from end of linked list -> Fast/Slow pointer gap of N.",
        "clues": "One-pass follow up, 1-indexed from end, singly linked list.",
        "diagram": "dummy -> 1 -> 2 -> 3 -> 4 -> 5\n                   S         F (gap of n+1)",
        "alt_sol": "Two pass length calculation.",
        "edge_cases": "Delete head node (n=sz), single node list (head=[1], n=1).",
        "tips": "Always use a dummy node for linked list deletion problems.",
        "similar": "LeetCode #61: Rotate List, LeetCode #2095: Delete Middle Node",
        "rev_notes": "Dummy node. Fast advances n+1 steps. Move fast & slow together until fast==null. slow->next = slow->next->next. O(N) single pass, O(1) space."
    },
    # 022
    {
        "id": "022", "name": "Squares of a Sorted Array", "lc_num": 977, "difficulty": "Easy",
        "url": "https://leetcode.com/problems/squares-of-a-sorted-array/",
        "q_statement": "Given an integer array `nums` sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.",
        "examples": "Input: nums = [-4,-1,0,3,10]\nOutput: [0,9,16,100]",
        "constraints": "- 1 <= nums.length <= 10^4\n- -10^4 <= nums[i] <= 10^4\n- `nums` is sorted in non-decreasing order.",
        "bf_pattern": "Square and Sort",
        "bf_intuition": "Square every number and call std::sort on the array.",
        "bf_algo": "1. For each x in nums: x = x * x.\n2. std::sort(nums.begin(), nums.end()).\n3. Return nums.",
        "bf_code": "#include <vector>\n#include <algorithm>\nclass Solution {\npublic:\n    std::vector<int> sortedSquares(std::vector<int>& nums) {\n        for (int& x : nums) x = x * x;\n        std::sort(nums.begin(), nums.end());\n        return nums;\n    }\n};",
        "bf_tc": "O(N log N)", "bf_sc": "O(1) extra space",
        "bf_why_not_opt": "Sorting takes O(N log N). Since array is pre-sorted, two pointers achieves O(N) linear time.",
        "opt_pattern": "Two Pointers (Outside-In Fill)",
        "opt_concept": "Largest squares occur at either extreme (far-left negative or far-right positive).",
        "opt_obs": "Comparing abs(nums[left]) and abs(nums[right]) identifies largest remaining squared value.",
        "opt_intuition": "Place left pointer at 0, right pointer at n-1. Place larger squared value at back of result array (pos = n-1) and shrink window inward.",
        "opt_algo": "1. left = 0, right = n-1, pos = n-1.\n2. Create result vector of size n.\n3. While left <= right:\n   if abs(nums[left]) > abs(nums[right]): res[pos--] = nums[left]*nums[left], left++\n   else: res[pos--] = nums[right]*nums[right], right--.\n4. Return res.",
        "opt_code": "#include <vector>\n#include <cmath>\nclass Solution {\npublic:\n    std::vector<int> sortedSquares(const std::vector<int>& nums) {\n        int n = nums.size();\n        std::vector<int> result(n);\n        int left = 0, right = n - 1;\n        for (int pos = n - 1; pos >= 0; --pos) {\n            if (std::abs(nums[left]) > std::abs(nums[right])) {\n                result[pos] = nums[left] * nums[left];\n                left++;\n            } else {\n                result[pos] = nums[right] * nums[right];\n                right--;\n            }\n        }\n        return result;\n    }\n};",
        "opt_dry_run": "[-4,-1,0,3,10] -> compare |-4| vs |10| -> res[4]=100 -> compare |-4| vs |3| -> res[3]=16...",
        "opt_tc": "O(N)", "opt_sc": "O(N) for output array",
        "opt_why_opt": "Linear O(N) single pass filling output array from back.",
        "opt_mistakes": "Filling result array from front instead of back.",
        "summary": "Sort squares of sorted array in O(N) time using two pointers comparing absolute values at left and right boundaries.",
        "pattern_rec": "Sorted array with negative values squared -> Two Pointers Outside-In.",
        "clues": "Pre-sorted input, non-decreasing output, linear O(N) follow-up.",
        "diagram": "L -> [-4, -1, 0, 3, 10] <- R (Max square is at boundaries!)",
        "alt_sol": "Square then sort O(N log N).",
        "edge_cases": "All non-negative ([0,1,2]), all negative ([-5,-3,-1]).",
        "tips": "Fill output array from right to left (largest to smallest).",
        "similar": "LeetCode #88: Merge Sorted Array, LeetCode #360: Sort Transformed Array",
        "rev_notes": "left=0, right=n-1. Loop pos=n-1 down to 0: if abs(nums[left])>abs(nums[right]) pick left++ else right--. O(N) time, O(N) space."
    },
    # 023
    {
        "id": "023", "name": "Backspace String Compare", "lc_num": 844, "difficulty": "Easy",
        "url": "https://leetcode.com/problems/backspace-string-compare/",
        "q_statement": "Given two strings `s` and `t`, return `true` if they are equal when both are typed into empty text editors. `'#'` means a backspace character.",
        "examples": "Input: s = \"ab#c\", t = \"ad#c\"\nOutput: true\nExplanation: Both s and t become \"ac\".",
        "constraints": "- 1 <= s.length, t.length <= 200\n- O(1) space constraint follow-up.",
        "bf_pattern": "Stack Simulation",
        "bf_intuition": "Build final string using std::string or stack for both s and t, then compare.",
        "bf_algo": "1. Build processString(s) using stack/string.\n2. Build processString(t).\n3. Return processString(s) == processString(t).",
        "bf_code": "#include <string>\nclass Solution {\nprivate:\n    std::string build(const std::string& str) {\n        std::string res = \"\";\n        for (char c : str) {\n            if (c != '#') res.push_back(c);\n            else if (!res.empty()) res.pop_back();\n        }\n        return res;\n    }\npublic:\n    bool backspaceCompare(const std::string& s, const std::string& t) {\n        return build(s) == build(t);\n    }\n};",
        "bf_tc": "O(N + M)", "bf_sc": "O(N + M)",
        "bf_why_not_opt": "Uses auxiliary memory for stack strings. Two Pointers scanning backwards achieves O(1) space.",
        "opt_pattern": "Two Pointers (Backward Scan with Skip Count)",
        "opt_concept": "Traverse strings backwards from end. Maintain skip count when encountering '#'.",
        "opt_obs": "Backspaces only affect characters to their left, so scanning backwards allows immediately skipping deleted characters.",
        "opt_intuition": "Set i = s.len-1, j = t.len-1. Count backspaces when moving backward. Find next valid character in both strings and compare.",
        "opt_algo": "1. i = s.size()-1, j = t.size()-1.\n2. While i >= 0 or j >= 0:\n   a. Find next valid char in s by skipping backspaced chars.\n   b. Find next valid char in t by skipping backspaced chars.\n   c. Compare valid chars; if mismatch return false.\n3. Return true.",
        "opt_code": "#include <string>\nclass Solution {\npublic:\n    bool backspaceCompare(const std::string& s, const std::string& t) {\n        int i = s.length() - 1, j = t.length() - 1;\n        int skip_s = 0, skip_t = 0;\n        \n        while (i >= 0 || j >= 0) {\n            while (i >= 0) {\n                if (s[i] == '#') { skip_s++; i--; }\n                else if (skip_s > 0) { skip_s--; i--; }\n                else break;\n            }\n            while (j >= 0) {\n                if (t[j] == '#') { skip_t++; j--; }\n                else if (skip_t > 0) { skip_t--; j--; }\n                else break;\n            }\n            if (i >= 0 != j >= 0) return false;\n            if (i >= 0 && j >= 0 && s[i] != t[j]) return false;\n            i--; j--;\n        }\n        return true;\n    }\n};",
        "opt_dry_run": "s=\"ab#c\", t=\"ad#c\" -> scan back: 'c'=='c', skip 'b' & 'd', 'a'=='a' -> true",
        "opt_tc": "O(N + M)", "opt_sc": "O(1)",
        "opt_why_opt": "Linear time with strictly O(1) extra space.",
        "opt_mistakes": "Not handling consecutive backspaces (`\"a##c\"`).",
        "summary": "Compare backspace strings in O(1) space by scanning backwards with skip counters.",
        "pattern_rec": "Backspace character processing with O(1) space -> Backward Two Pointers.",
        "clues": "'#' is backspace, O(1) space target.",
        "diagram": "s: \"a b # c\" <- i (reads c, skips b due to #, reads a)\nt: \"a d # c\" <- j",
        "alt_sol": "Stack approach O(N) space.",
        "edge_cases": "Strings reduce to empty (\"a#b#\" vs \"c#d#\"), unequal valid lengths.",
        "tips": "Inner while loops skip all deleted characters before character comparison.",
        "similar": "LeetCode #1047: Remove All Adjacent Duplicates",
        "rev_notes": "i=s.len-1, j=t.len-1. Skip chars using skip count while reading backwards. Compare next valid chars. O(N+M) time, O(1) space."
    },
    # 024
    {
        "id": "024", "name": "Maximum Average Subarray I", "lc_num": 643, "difficulty": "Easy",
        "url": "https://leetcode.com/problems/maximum-average-subarray-i/",
        "q_statement": "You are given an integer array `nums` consisting of `n` elements, and an integer `k`. Find a contiguous subarray whose length is equal to `k` that has the maximum average value and return this value.",
        "examples": "Input: nums = [1,12,-5,-6,50,3], k = 4\nOutput: 12.75\nExplanation: Subarray [12, -5, -6, 50] has max sum = 51, average = 51 / 4 = 12.75.",
        "constraints": "- n == nums.length\n- 1 <= k <= n <= 10^5\n- -10^4 <= nums[i] <= 10^4",
        "bf_pattern": "Nested Loops Subarray Sum",
        "bf_intuition": "Calculate sum of every contiguous subarray of size k.",
        "bf_algo": "1. max_sum = -INF.\n2. Loop i from 0 to n-k: sum = sum(nums[i...i+k-1]), max_sum = max(max_sum, sum).\n3. Return max_sum / k.",
        "bf_code": "#include <vector>\n#include <algorithm>\nclass Solution {\npublic:\n    double findMaxAverage(const std::vector<int>& nums, int k) {\n        double max_sum = -1e18;\n        for (int i = 0; i <= (int)nums.size() - k; ++i) {\n            double sum = 0;\n            for (int j = i; j < i + k; ++j) sum += nums[j];\n            max_sum = std::max(max_sum, sum);\n        }\n        return max_sum / k;\n    }\n};",
        "bf_tc": "O(N * K)", "bf_sc": "O(1)",
        "bf_why_not_opt": "Re-calculates sum of overlapping windows. Sliding Window achieves linear O(N) time.",
        "opt_pattern": "Fixed-Size Sliding Window",
        "opt_concept": "Maintain running sum of window of size k. When window slides right, add new element and subtract outgoing element.",
        "opt_obs": "Sum of window [i+1 ... i+k] = Sum of window [i ... i+k-1] + nums[i+k] - nums[i].",
        "opt_intuition": "Compute sum of first k elements. Then slide window across array updating running sum in O(1) per step.",
        "opt_algo": "1. Compute initial sum of first k elements.\n2. max_sum = sum.\n3. Loop i from k to n-1:\n   sum += nums[i] - nums[i - k]\n   max_sum = max(max_sum, sum).\n4. Return (double)max_sum / k.",
        "opt_code": "#include <vector>\n#include <algorithm>\nclass Solution {\npublic:\n    double findMaxAverage(const std::vector<int>& nums, int k) {\n        double current_sum = 0;\n        for (int i = 0; i < k; ++i) current_sum += nums[i];\n        \n        double max_sum = current_sum;\n        for (size_t i = k; i < nums.size(); ++i) {\n            current_sum += nums[i] - nums[i - k];\n            max_sum = std::max(max_sum, current_sum);\n        }\n        return max_sum / k;\n    }\n};",
        "opt_dry_run": "[1,12,-5,-6,50,3], k=4 -> initial sum(1,12,-5,-6)=2 -> slide 50: 2+50-1=51 -> slide 3: 51+3-12=42 -> max=51 -> 51/4 = 12.75",
        "opt_tc": "O(N)", "opt_sc": "O(1)",
        "opt_why_opt": "Single pass O(N) linear time with O(1) space.",
        "opt_mistakes": "Integer division (forgetting to cast sum or return type to double).",
        "summary": "Find maximum average subarray of fixed size k using fixed-size sliding window in O(N) time.",
        "pattern_rec": "Fixed length k subarray property -> Fixed-Size Sliding Window.",
        "clues": "Contiguous subarray of length k, maximum average.",
        "diagram": "Window [1, 12, -5, -6] -> Slide right -> [12, -5, -6, 50] (+50, -1)",
        "alt_sol": "Prefix sum array O(N) space.",
        "edge_cases": "k == n, k == 1, negative numbers only.",
        "tips": "Cast to double before dividing by k.",
        "similar": "LeetCode #209: Minimum Size Subarray Sum, LeetCode #1343",
        "rev_notes": "Sum first k elements. Loop i=k..n-1: sum += nums[i] - nums[i-k], max_sum = max(max_sum, sum). Return max_sum/k. O(N) time, O(1) space."
    },
    # 025
    {
        "id": "025", "name": "Longest Substring Without Repeating Characters", "lc_num": 3, "difficulty": "Medium",
        "url": "https://leetcode.com/problems/longest-substring-without-repeating-characters/",
        "q_statement": "Given a string `s`, find the length of the **longest substring** without repeating characters.",
        "examples": "Input: s = \"abcabcbb\"\nOutput: 3\nExplanation: The answer is \"abc\", with the length of 3.",
        "constraints": "- 0 <= s.length <= 5 * 10^4\n- s consists of English letters, digits, symbols and spaces.",
        "bf_pattern": "All Substrings Check",
        "bf_intuition": "Generate all possible substrings, check if each contains all unique characters using a set, and track max length.",
        "bf_algo": "1. max_len = 0.\n2. Loop i from 0 to n-1, loop j from i to n-1.\n3. If substring s[i..j] has all unique chars: max_len = max(max_len, j - i + 1).",
        "bf_code": "#include <string>\n#include <unordered_set>\n#include <algorithm>\nclass Solution {\npublic:\n    int lengthOfLongestSubstring(const std::string& s) {\n        int max_len = 0, n = s.length();\n        for (int i = 0; i < n; ++i) {\n            std::unordered_set<char> seen;\n            for (int j = i; j < n; ++j) {\n                if (seen.count(s[j])) break;\n                seen.insert(s[j]);\n                max_len = std::max(max_len, j - i + 1);\n            }\n        }\n        return max_len;\n    }\n};",
        "bf_tc": "O(N^2)", "bf_sc": "O(min(N, M))",
        "bf_why_not_opt": "Re-checks substrings redundantly taking O(N^2). Dynamic Variable Sliding Window achieves O(N).",
        "opt_pattern": "Variable-Size Sliding Window (Hash Map Index Tracking)",
        "opt_concept": "Maintain sliding window [left...right]. Use hash map to store last seen index of each character.",
        "opt_obs": "If s[right] was seen at index `last_idx >= left`, jump `left = last_idx + 1` directly.",
        "opt_intuition": "As `right` expands the window, if character s[right] is duplicated inside current window [left...right], jump `left` past the duplicate.",
        "opt_algo": "1. unordered_map<char, int> last_seen or char_index array of size 256 initialized to -1.\n2. left = 0, max_len = 0.\n3. Loop right from 0 to n-1:\n   if s[right] was seen and idx >= left: left = idx + 1\n   update last_seen[s[right]] = right\n   max_len = max(max_len, right - left + 1).\n4. Return max_len.",
        "opt_code": "#include <string>\n#include <vector>\n#include <algorithm>\nclass Solution {\npublic:\n    int lengthOfLongestSubstring(const std::string& s) {\n        std::vector<int> last_seen(256, -1);\n        int max_len = 0;\n        int left = 0;\n        \n        for (int right = 0; right < (int)s.length(); ++right) {\n            if (last_seen[s[right]] >= left) {\n                left = last_seen[s[right]] + 1;\n            }\n            last_seen[s[right]] = right;\n            max_len = std::max(max_len, right - left + 1);\n        }\n        return max_len;\n    }\n};",
        "opt_dry_run": "\"abcabcbb\" -> r=0('a') len=1 -> r=1('b') len=2 -> r=2('c') len=3 -> r=3('a') left jumps to 1 ('a' duplicate at 0), len=3...",
        "opt_tc": "O(N)", "opt_sc": "O(1) (Fixed char set size 256)",
        "opt_why_opt": "Single pass O(N) time with constant O(1) space (256 element lookup table).",
        "opt_mistakes": "Forgetting condition `last_seen[c] >= left` when jumping left pointer (jumping to stale index outside current window).",
        "summary": "Find length of longest substring without repeating characters using variable sliding window with last-seen character index tracking.",
        "pattern_rec": "Longest substring without repeating characters -> Variable Sliding Window.",
        "clues": "Substring (contiguous), unique characters, maximum length.",
        "diagram": "Window [a b c] -> next is 'a' -> jump left past previous 'a' -> Window [b c a]",
        "alt_sol": "Sliding window with std::unordered_set and inner while loop to shrink left.",
        "edge_cases": "Empty string (0), single char (1), all identical characters (\"bbbb\" -> 1).",
        "tips": "Using `std::vector<int>(256, -1)` is much faster than `std::unordered_map`.",
        "similar": "LeetCode #159, #340, #992",
        "rev_notes": "last_seen vector size 256 init -1. left=0. For right=0..n-1: if last_seen[s[r]]>=left left=last_seen[s[r]]+1. Update last_seen, max_len. O(N) time, O(1) space."
    }
]

# Write final Phase 1 problems
for p_data in p1_final:
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

print("Generated problems 021 to 025!")
