import os

BASE_DIR = r"c:\Users\Pinak chimurkar\DSA"
phase0_dir = os.path.join(BASE_DIR, "Phase 00 Programming Foundation")
phase1_dir = os.path.join(BASE_DIR, "Phase 01 Two Pointers & Sliding Window")

os.makedirs(phase0_dir, exist_ok=True)
os.makedirs(phase1_dir, exist_ok=True)

problems = [
    # 011
    {
        "dir": phase0_dir, "id": "011", "name": "Reverse String", "lc_num": 344, "difficulty": "Easy",
        "url": "https://leetcode.com/problems/reverse-string/",
        "q_statement": "Write a function that reverses a string. The input string is given as an array of characters `s`. You must do this by modifying the input array in-place with O(1) extra memory.",
        "examples": "Input: s = [\"h\",\"e\",\"l\",\"l\",\"o\"]\nOutput: [\"o\",\"l\",\"l\",\"e\",\"h\"]",
        "constraints": "- 1 <= s.length <= 10^5",
        "bf_pattern": "Auxiliary Vector Copy",
        "bf_intuition": "Copy elements into a new vector in reverse order.",
        "bf_algo": "1. Create temp vector.\n2. Fill temp backwards.\n3. Copy back to s.",
        "bf_code": "#include <vector>\nclass Solution {\npublic:\n    void reverseString(std::vector<char>& s) {\n        std::vector<char> temp(s.rbegin(), s.rend());\n        s = temp;\n    }\n};",
        "bf_tc": "O(N)", "bf_sc": "O(N)", "bf_why_not_opt": "Uses O(N) auxiliary space violating O(1) in-place constraint.",
        "opt_pattern": "Two Pointers (In-Place Swap)",
        "opt_concept": "Swap characters at left and right pointers while left < right.",
        "opt_obs": "Swapping s[i] and s[n-1-i] reverses the array in-place.",
        "opt_intuition": "Place left pointer at start, right pointer at end. Swap s[left] and s[right], increment left, decrement right.",
        "opt_algo": "1. left = 0, right = s.size() - 1.\n2. While left < right: swap(s[left++], s[right--]).",
        "opt_code": "#include <vector>\n#include <algorithm>\nclass Solution {\npublic:\n    void reverseString(std::vector<char>& s) {\n        int left = 0, right = s.size() - 1;\n        while (left < right) {\n            std::swap(s[left++], s[right--]);\n        }\n    }\n};",
        "opt_dry_run": "['h','e','l','l','o'] -> swap(h,o) -> swap(e,l) -> ['o','l','l','e','h']",
        "opt_tc": "O(N)", "opt_sc": "O(1)", "opt_why_opt": "Performs N/2 swaps in-place taking O(N) time and O(1) space.",
        "opt_mistakes": "Off-by-one errors with right index initialization.",
        "summary": "Reverse string in-place using two pointers swapping from edges towards center.",
        "pattern_rec": "In-place sequence reversal -> Two Pointers Swap.",
        "clues": "In-place, O(1) extra memory.", "diagram": "L -> ['h','e','l','l','o'] <- R",
        "alt_sol": "std::reverse(s.begin(), s.end()).",
        "edge_cases": "Single character, even vs odd lengths.", "tips": "Mention std::swap mechanics.",
        "similar": "LeetCode #541, #345, #151",
        "rev_notes": "left=0, right=n-1. While left<right: swap(s[left++], s[right--]). O(N) time, O(1) space."
    },
    # 012
    {
        "dir": phase0_dir, "id": "012", "name": "Reverse Words in a String", "lc_num": 151, "difficulty": "Medium",
        "url": "https://leetcode.com/problems/reverse-words-in-a-string/",
        "q_statement": "Given an input string `s`, reverse the order of the **words**. Return a string of the words concatenated by a single space with no leading or trailing spaces.",
        "examples": "Input: s = \"the sky is blue\"\nOutput: \"blue is sky the\"",
        "constraints": "- 1 <= s.length <= 10^4",
        "bf_pattern": "String Stream Split and Reverse",
        "bf_intuition": "Split words into a list using std::stringstream, reverse the list, and join with spaces.",
        "bf_algo": "1. Parse words into vector using stringstream.\n2. Reverse vector.\n3. Join words with single space.",
        "bf_code": "#include <string>\n#include <sstream>\n#include <vector>\n#include <algorithm>\nclass Solution {\npublic:\n    std::string reverseWords(std::string s) {\n        std::stringstream ss(s);\n        std::string word;\n        std::vector<std::string> words;\n        while (ss >> word) words.push_back(word);\n        std::reverse(words.begin(), words.end());\n        std::string result = \"\";\n        for (int i = 0; i < words.size(); ++i) {\n            result += words[i] + (i == words.size() - 1 ? \"\" : \" \");\n        }\n        return result;\n    }\n};",
        "bf_tc": "O(N)", "bf_sc": "O(N)", "bf_why_not_opt": "Allocates extra memory for word list string vector.",
        "opt_pattern": "Two-Pass In-Place Reversal",
        "opt_concept": "1. Reverse whole string. 2. Reverse each individual word. 3. Clean extra spaces.",
        "opt_obs": "Reversing whole string reverses both word order and word characters. Reversing each word restores character order.",
        "opt_intuition": "Reverse entire string, then scan and reverse each word back to original character order while removing extra spaces.",
        "opt_algo": "1. Reverse string s.\n2. Use two pointers to reverse each word back.\n3. Clean leading/trailing/multiple spaces in-place.",
        "opt_code": "#include <string>\n#include <algorithm>\nclass Solution {\npublic:\n    std::string reverseWords(std::string s) {\n        std::reverse(s.begin(), s.end());\n        int n = s.length(), idx = 0;\n        for (int i = 0; i < n; ++i) {\n            if (s[i] != ' ') {\n                if (idx != 0) s[idx++] = ' ';\n                int start = idx;\n                while (i < n && s[i] != ' ') s[idx++] = s[i++];\n                std::reverse(s.begin() + start, s.begin() + idx);\n            }\n        }\n        s.erase(s.begin() + idx, s.end());\n        return s;\n    }\n};",
        "opt_dry_run": "\"the sky\" -> \"yks eht\" -> reverse words -> \"sky the\"",
        "opt_tc": "O(N)", "opt_sc": "O(1) extra space", "opt_why_opt": "In-place string modification without extra heap allocations.",
        "opt_mistakes": "Leaving multiple spaces between words or leading/trailing spaces.",
        "summary": "Reverse word order by reversing whole string and then reversing individual words in-place.",
        "pattern_rec": "Reverse word sequence -> Reverse whole string then reverse each word.",
        "clues": "Trim extra spaces, reverse order of words.", "diagram": "\"the sky\" -> Rev All -> \"yks eht\" -> Rev Words -> \"sky the\"",
        "alt_sol": "std::stringstream approach.",
        "edge_cases": "Multiple spaces between words, leading/trailing spaces.", "tips": "Handle space cleaning carefully.",
        "similar": "LeetCode #186, #557",
        "rev_notes": "Reverse whole string. Scan words, reverse each word back, shift to remove spaces. O(N) time, O(1) space."
    },
    # 013
    {
        "dir": phase0_dir, "id": "013", "name": "Longest Common Prefix", "lc_num": 14, "difficulty": "Easy",
        "url": "https://leetcode.com/problems/longest-common-prefix/",
        "q_statement": "Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string `\"\"`.",
        "examples": "Input: strs = [\"flower\",\"flow\",\"flight\"]\nOutput: \"fl\"",
        "constraints": "- 1 <= strs.length <= 200\n- 0 <= strs[i].length <= 200",
        "bf_pattern": "Vertical Scanning",
        "bf_intuition": "Compare characters column by column across all strings.",
        "bf_algo": "1. For col index i from 0 to strs[0].length()-1:\n2. For each str in strs: if i >= str.length() or str[i] != strs[0][i], return prefix so far.\n3. Return strs[0].",
        "bf_code": "#include <vector>\n#include <string>\nclass Solution {\npublic:\n    std::string longestCommonPrefix(const std::vector<std::string>& strs) {\n        if (strs.empty()) return \"\";\n        for (int i = 0; i < strs[0].length(); ++i) {\n            char c = strs[0][i];\n            for (int j = 1; j < strs.size(); ++j) {\n                if (i >= strs[j].length() || strs[j][i] != c) {\n                    return strs[0].substr(0, i);\n                }\n            }\n        }\n        return strs[0];\n    }\n};",
        "bf_tc": "O(S) where S is sum of all characters", "bf_sc": "O(1)", "bf_why_not_opt": "Vertical scanning is optimal O(S) time as it stops early at first mismatch.",
        "opt_pattern": "Vertical Scanning / Horizontal Scanning",
        "opt_concept": "Compare character by character vertically across all strings until mismatch.",
        "opt_obs": "Common prefix cannot be longer than shortest string.",
        "opt_intuition": "Look at column i across all strings. If all match, append char; at first mismatch return substring.",
        "opt_algo": "1. Check empty input.\n2. Iterate through characters of first string.\n3. Mismatch or end of any string -> return prefix.",
        "opt_code": "#include <vector>\n#include <string>\nclass Solution {\npublic:\n    std::string longestCommonPrefix(const std::vector<std::string>& strs) {\n        if (strs.empty()) return \"\";\n        for (size_t i = 0; i < strs[0].size(); ++i) {\n            char c = strs[0][i];\n            for (size_t j = 1; j < strs.size(); ++j) {\n                if (i >= strs[j].size() || strs[j][i] != c) {\n                    return strs[0].substr(0, i);\n                }\n            }\n        }\n        return strs[0];\n    }\n};",
        "opt_dry_run": "[\"flower\",\"flow\",\"flight\"] -> col 0 'f' ok -> col 1 'l' ok -> col 2 'o' vs 'i' mismatch -> \"fl\"",
        "opt_tc": "O(S)", "opt_sc": "O(1)", "opt_why_opt": "Reads only necessary characters up to first mismatch.",
        "opt_mistakes": "Out of bounds on short strings.",
        "summary": "Find longest common prefix across array of strings via vertical column scanning.",
        "pattern_rec": "Common prefix among multiple strings -> Vertical character scanning or Trie.",
        "clues": "Prefix match, early stop on mismatch.", "diagram": "f l o w e r\nf l o w\nf l i g h t -> match up to 'l'",
        "alt_sol": "Sort array of strings and compare first and last strings.",
        "edge_cases": "Empty vector, empty strings in vector, no common prefix.", "tips": "Vertical scanning stops earlier than horizontal scanning if mismatch is near start.",
        "similar": "LeetCode #20, #28",
        "rev_notes": "Loop column i in strs[0]. Check all strs[j][i] == c. Return substr(0, i) on mismatch. O(S) time, O(1) space."
    },
    # 014
    {
        "dir": phase0_dir, "id": "014", "name": "Roman to Integer", "lc_num": 13, "difficulty": "Easy",
        "url": "https://leetcode.com/problems/roman-to-integer/",
        "q_statement": "Given a roman numeral string `s`, convert it to an integer. Roman numerals are represented by seven symbols: I (1), V (5), X (10), L (50), C (100), D (500), M (1000).",
        "examples": "Input: s = \"MCMXCIV\"\nOutput: 1994",
        "constraints": "- 1 <= s.length <= 15\n- s contains only Roman symbols.",
        "bf_pattern": "Left-to-Right Scan with Subtraction Lookahead",
        "bf_intuition": "Map characters to values. If current value < next value, subtract current value; else add current value.",
        "bf_algo": "1. Create map of Roman symbol values.\n2. Iterate through string.\n3. If val[s[i]] < val[s[i+1]]: total -= val[s[i]], else total += val[s[i]].",
        "bf_code": "#include <string>\n#include <unordered_map>\nclass Solution {\npublic:\n    int romanToInt(const std::string& s) {\n        std::unordered_map<char, int> val = {{'I',1},{'V',5},{'X',10},{'L',50},{'C',100},{'D',500},{'M',1000}};\n        int total = 0, n = s.length();\n        for (int i = 0; i < n; ++i) {\n            if (i + 1 < n && val[s[i]] < val[s[i+1]]) total -= val[s[i]];\n            else total += val[s[i]];\n        }\n        return total;\n    }\n};",
        "bf_tc": "O(N)", "bf_sc": "O(1)", "bf_why_not_opt": "Single pass scan is already optimal.",
        "opt_pattern": "Left-to-Right Single Pass Value Comparison",
        "opt_concept": "If smaller Roman symbol appears before larger symbol, it is subtracted; otherwise added.",
        "opt_obs": "IV = 5 - 1 = 4, IX = 10 - 1 = 9. Subtraction rule occurs whenever val[i] < val[i+1].",
        "opt_intuition": "Scan from left to right. Look at current symbol and next symbol. If current < next, subtract; else add.",
        "opt_algo": "1. Define symbol helper function.\n2. Loop through s, compare symbol(s[i]) with symbol(s[i+1]).\n3. Add/subtract accordingly and return sum.",
        "opt_code": "#include <string>\nclass Solution {\nprivate:\n    int getValue(char c) {\n        switch(c) {\n            case 'I': return 1;\n            case 'V': return 5;\n            case 'X': return 10;\n            case 'L': return 50;\n            case 'C': return 100;\n            case 'D': return 500;\n            case 'M': return 1000;\n            default: return 0;\n        }\n    }\npublic:\n    int romanToInt(const std::string& s) {\n        int total = 0, n = s.length();\n        for (int i = 0; i < n; ++i) {\n            int cur = getValue(s[i]);\n            int next = (i + 1 < n) ? getValue(s[i+1]) : 0;\n            if (cur < next) total -= cur;\n            else total += cur;\n        }\n        return total;\n    }\n};",
        "opt_dry_run": "\"LVIII\" -> L(50)+V(5)+I(1)+I(1)+I(1) = 58",
        "opt_tc": "O(N)", "opt_sc": "O(1)", "opt_why_opt": "Single pass O(N) time and O(1) space (switch statement eliminates hash map overhead).",
        "opt_mistakes": "Out of bounds on s[i+1] check.",
        "summary": "Convert Roman numeral string to integer by scanning and applying subtractive rule when val[i] < val[i+1].",
        "pattern_rec": "Roman numeral parsing -> Right/Left comparative scan.",
        "clues": "7 standard symbols, subtractive notation (IV, IX, XL, XC, CD, CM).",
        "diagram": "M(1000) + C(-100) + M(1000) + X(-10) + C(100) + I(-1) + V(5) = 1994",
        "alt_sol": "Right-to-left scan tracking running maximum value.",
        "edge_cases": "Single symbol (\"I\" -> 1), max length string.", "tips": "Use switch statement instead of std::unordered_map for zero heap allocation.",
        "similar": "LeetCode #12: Integer to Roman",
        "rev_notes": "Switch function for values. If val[i] < val[i+1] subtract, else add. O(N) time, O(1) space."
    },
    # 015
    {
        "dir": phase0_dir, "id": "015", "name": "Integer to Roman", "lc_num": 12, "difficulty": "Medium",
        "url": "https://leetcode.com/problems/integer-to-roman/",
        "q_statement": "Given an integer `num`, convert it to a Roman numeral string.",
        "examples": "Input: num = 3749\nOutput: \"MMDCCXLIX\"",
        "constraints": "- 1 <= num <= 3999",
        "bf_pattern": "Greedy Symbol Subtraction",
        "bf_intuition": "Iterate through ordered list of Roman symbol values from largest to smallest, subtracting values and appending symbols.",
        "bf_algo": "1. Define pairs of {value, symbol} in descending order including subtractive combinations (1000:'M', 900:'CM', etc.).\n2. While num > 0: subtract largest value <= num and append symbol.",
        "bf_code": "#include <string>\n#include <vector>\n#include <utility>\nclass Solution {\npublic:\n    std::string intToRoman(int num) {\n        std::vector<std::pair<int, std::string>> val_sym = {\n            {1000, \"M\"}, {900, \"CM\"}, {500, \"D\"}, {400, \"CD\"},\n            {100, \"C\"}, {90, \"XC\"}, {50, \"L\"}, {40, \"XL\"},\n            {10, \"X\"}, {9, \"IX\"}, {5, \"V\"}, {4, \"IV\"}, {1, \"I\"}\n        };\n        std::string res = \"\";\n        for (const auto& [val, sym] : val_sym) {\n            while (num >= val) {\n                res += sym;\n                num -= val;\n            }\n        }\n        return res;\n    }\n};",
        "bf_tc": "O(1) since num <= 3999", "bf_sc": "O(1)", "bf_why_not_opt": "Greedy approach is already optimal.",
        "opt_pattern": "Greedy Subtraction / Value Table Lookup",
        "opt_concept": "Match largest possible value from Roman table greedily.",
        "opt_obs": "Roman numeral system is decimal-place based with fixed symbols for 1000s, 100s, 10s, 1s.",
        "opt_intuition": "Subtract the largest possible numeral value from num repeatedly, appending corresponding symbol.",
        "opt_algo": "1. Array of values: [1000,900,500,400,100,90,50,40,10,9,5,4,1].\n2. Array of symbols: [\"M\",\"CM\",\"D\",\"CD\",\"C\",\"XC\",\"L\",\"XL\",\"X\",\"IX\",\"V\",\"IV\",\"I\"].\n3. Loop through table, append symbol while num >= value.",
        "opt_code": "#include <string>\nclass Solution {\npublic:\n    std::string intToRoman(int num) {\n        const int values[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};\n        const char* symbols[] = {\"M\", \"CM\", \"D\", \"CD\", \"C\", \"XC\", \"L\", \"XL\", \"X\", \"IX\", \"V\", \"IV\", \"I\"};\n        std::string result = \"\";\n        for (int i = 0; i < 13; ++i) {\n            while (num >= values[i]) {\n                result += symbols[i];\n                num -= values[i];\n            }\n        }\n        return result;\n    }\n};",
        "opt_dry_run": "num = 58 -> subtract 50 (\"L\"), num=8 -> subtract 5 (\"V\"), num=3 -> 3x\"I\" -> \"LVIII\"",
        "opt_tc": "O(1)", "opt_sc": "O(1)", "opt_why_opt": "Bounded input range 1..3999 means fixed maximum operations.",
        "opt_mistakes": "Forgetting subtractive pair entries like 900 ('CM'), 400 ('CD'), 90 ('XC'), 40 ('XL'), 9 ('IX'), 4 ('IV').",
        "summary": "Convert integer to Roman numeral using greedy value matching from hardcoded symbol value lookup table.",
        "pattern_rec": "Integer conversion with fixed rules -> Greedy Table Lookup.",
        "clues": "Input range 1..3999, subtractive forms included.", "diagram": "3749 -> 3xM (3000) + DCC (700) + XL (40) + IX (9) = MMDCCXLIX",
        "alt_sol": "Hardcoded digit mapping for thousands, hundreds, tens, units positions.",
        "edge_cases": "Min num=1, max num=3999, numbers with zeroes (1004).", "tips": "Include subtractive symbols directly in lookup table.",
        "similar": "LeetCode #13: Roman to Integer",
        "rev_notes": "Table of 13 values/symbols including subtractive pairs. Loop table, while num >= val: append sym, num -= val. O(1) time, O(1) space."
    },
    # 016
    {
        "dir": phase1_dir, "id": "016", "name": "Two Sum II - Input Array Is Sorted", "lc_num": 167, "difficulty": "Medium",
        "url": "https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/",
        "q_statement": "Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific `target` number. Return 1-based indices.",
        "examples": "Input: numbers = [2,7,11,15], target = 9\nOutput: [1,2]",
        "constraints": "- 2 <= numbers.length <= 3 * 10^4\n- O(1) extra space requirement.",
        "bf_pattern": "Nested Loops / Binary Search",
        "bf_intuition": "For each element numbers[i], binary search for target - numbers[i] in numbers[i+1...n-1].",
        "bf_algo": "1. For i=0..n-2: binary search target - numbers[i].\n2. Return {i+1, match_idx+1}.",
        "bf_code": "#include <vector>\n#include <algorithm>\nclass Solution {\npublic:\n    std::vector<int> twoSum(const std::vector<int>& numbers, int target) {\n        for (int i = 0; i < numbers.size(); ++i) {\n            int complement = target - numbers[i];\n            auto it = std::lower_bound(numbers.begin() + i + 1, numbers.end(), complement);\n            if (it != numbers.end() && *it == complement) {\n                return {i + 1, static_cast<int>(it - numbers.begin()) + 1};\n            }\n        }\n        return {};\n    }\n};",
        "bf_tc": "O(N log N)", "bf_sc": "O(1)", "bf_why_not_opt": "Binary search takes O(N log N). Two pointers reduces this to linear O(N) time.",
        "opt_pattern": "Two Pointers (Opposite Ends)",
        "opt_concept": "Since array is sorted, sum of left and right pointers can be adjusted deterministically.",
        "opt_obs": "If sum < target, increase left pointer to increase sum. If sum > target, decrease right pointer to decrease sum.",
        "opt_intuition": "Start left at index 0, right at n-1. If numbers[left] + numbers[right] == target, return 1-based indices.",
        "opt_algo": "1. left = 0, right = numbers.size() - 1.\n2. While left < right:\n   sum = numbers[left] + numbers[right]\n   if sum == target: return {left + 1, right + 1}\n   else if sum < target: left++\n   else: right--.",
        "opt_code": "#include <vector>\nclass Solution {\npublic:\n    std::vector<int> twoSum(const std::vector<int>& numbers, int target) {\n        int left = 0, right = numbers.size() - 1;\n        while (left < right) {\n            int current_sum = numbers[left] + numbers[right];\n            if (current_sum == target) {\n                return {left + 1, right + 1};\n            } else if (current_sum < target) {\n                left++;\n            } else {\n                right--;\n            }\n        }\n        return {};\n    }\n};",
        "opt_dry_run": "[2,7,11,15], target=9 -> left=0 (2), right=3 (15) sum=17>9 -> right=2 (11) sum=13>9 -> right=1 (7) sum=9==9 -> return {1, 2}",
        "opt_tc": "O(N)", "opt_sc": "O(1)", "opt_why_opt": "Single pass O(N) time with strictly O(1) auxiliary space.",
        "opt_mistakes": "Forgetting 1-based index conversion requirement.",
        "summary": "Find 2 numbers adding to target in sorted array using opposite end two pointers in O(N) time and O(1) space.",
        "pattern_rec": "Pair sum on sorted array -> Two Pointers (Left / Right).",
        "clues": "Sorted array, exact target sum, 1-indexed response, O(1) space.",
        "diagram": "L -> [2, 7, 11, 15] <- R  (sum = 2 + 15 = 17 > 9 -> move R left)",
        "alt_sol": "Binary Search O(N log N), Hash Map O(N) time & O(N) space.",
        "edge_cases": "Negative numbers, duplicates, minimum size 2.", "tips": "Highlight how sorted property eliminates hash map space overhead.",
        "similar": "LeetCode #1, #15, #653",
        "rev_notes": "left=0, right=n-1. While left<right: sum = nums[left]+nums[right]. sum<target ? left++ : sum>target ? right-- : return {left+1, right+1}. O(N) time, O(1) space."
    }
]

# Build problem files
for p_data in problems:
    p_folder = os.path.join(p_data['dir'], f"{p_data['id']} {p_data['name']}")
    os.makedirs(p_folder, exist_ok=True)
    
    with open(os.path.join(p_folder, "00_Question.md"), "w", encoding="utf-8") as f:
        f.write(f"# {p_data['id']}. {p_data['name']}\n\n- **Platform**: LeetCode\n- **Problem Number**: #{p_data['lc_num']}\n- **Difficulty**: {p_data['difficulty']}\n- **URL**: [{p_data['name']}]({p_data['url']})\n\n---\n\n## Problem Statement\n\n{p_data['q_statement']}\n\n---\n\n## Examples\n\n{p_data['examples']}\n\n---\n\n## Constraints\n\n{p_data['constraints']}\n")
        
    with open(os.path.join(p_folder, "01_Brute_Force.md"), "w", encoding="utf-8") as f:
        f.write(f"# {p_data['name']}\n\n- **Problem Number**: {p_data['lc_num']}\n- **Platform**: LeetCode #{p_data['lc_num']}\n- **Difficulty**: {p_data['difficulty']}\n- **Pattern**: {p_data['bf_pattern']}\n\n---\n\n## Brute Force Intuition\n\n{p_data['bf_intuition']}\n\n---\n\n## Algorithm\n\n{p_data['bf_algo']}\n\n---\n\n## Code\n\n```cpp\n{p_data['bf_code']}\n```\n\n---\n\n## Time Complexity\n\n- **Time Complexity**: {p_data['bf_tc']}\n\n---\n\n## Space Complexity\n\n- **Space Complexity**: {p_data['bf_sc']}\n\n---\n\n## Why This Approach Is Not Optimal\n\n{p_data['bf_why_not_opt']}\n")

    with open(os.path.join(p_folder, "02_Optimal_Approach.md"), "w", encoding="utf-8") as f:
        f.write(f"# {p_data['name']}\n\n## Pattern Used\n\n- **Pattern**: **{p_data['opt_pattern']}**\n- **Concept**: {p_data['opt_concept']}\n\n---\n\n## Observation\n\n{p_data['opt_obs']}\n\n---\n\n## Intuition\n\n{p_data['opt_intuition']}\n\n---\n\n## Algorithm\n\n{p_data['opt_algo']}\n\n---\n\n## Clean C++17 Solution\n\n```cpp\n{p_data['opt_code']}\n```\n\n---\n\n## Dry Run\n\n{p_data['opt_dry_run']}\n\n---\n\n## Time Complexity\n\n- **Time Complexity**: {p_data['opt_tc']}\n\n---\n\n## Space Complexity\n\n- **Space Complexity**: {p_data['opt_sc']}\n\n---\n\n## Why This is Optimal\n\n{p_data['opt_why_opt']}\n\n---\n\n## Common Mistakes\n\n{p_data['opt_mistakes']}\n")

    with open(os.path.join(p_folder, "03_Explanation.md"), "w", encoding="utf-8") as f:
        f.write(f"# Problem Summary\n\n{p_data['summary']}\n\n---\n\n## Pattern Recognition\n\n{p_data['pattern_rec']}\n\n---\n\n## Important Clues\n\n{p_data['clues']}\n\n---\n\n## Example\n\n```text\n{p_data['diagram']}\n```\n\n---\n\n## Alternative Solutions\n\n{p_data['alt_sol']}\n\n---\n\n## Edge Cases\n\n{p_data['edge_cases']}\n\n---\n\n## Interview Tips\n\n{p_data['tips']}\n\n---\n\n## Similar Problems\n\n{p_data['similar']}\n\n---\n\n## Revision Notes\n\n{p_data['rev_notes']}\n")

print("Generated problems 011 to 016!")
