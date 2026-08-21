# Group Anagrams - Optimal Approach

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
