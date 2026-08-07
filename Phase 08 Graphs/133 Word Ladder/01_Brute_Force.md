# Word Ladder

- **Problem Number**: 127
- **Platform**: LeetCode #127
- **Difficulty**: Hard
- **Pattern**: Full All-Pairs Graph Construction + BFS

---

## Brute Force Intuition

1. First check if `endWord` exists in `wordList`. If not, return `0`.
2. Construct an explicit graph where each word in `wordList` (plus `beginWord`) is a node, and an undirected edge exists between any two words that differ by exactly 1 character.
3. To determine if two words differ by 1 character, compare them character by character in $\mathcal{O}(L)$ time for all pair combinations $\mathcal{O}(N^2 \times L)$.
4. Run standard BFS starting from `beginWord` to find the shortest path length to `endWord`.

---

## Algorithm

1. `unordered_set<string> dict(wordList.begin(), wordList.end())`.
2. If `dict` does not contain `endWord`, return `0`.
3. Build explicit graph by checking all pairs $(w_1, w_2)$ for 1-character difference.
4. `queue<string> q`, push `beginWord`. `level = 1`.
5. Level-by-level BFS:
   - Pop words at current level.
   - If `curr == endWord`, return `level`.
   - Traverse neighbors, mark visited, push to queue.
   - `level++`.
6. Return `0`.

---

## Code

```cpp
#include <string>
#include <vector>
#include <unordered_set>
#include <unordered_map>
#include <queue>

class Solution {
private:
    bool isOneDiff(const std::string& a, const std::string& b) {
        int diff = 0;
        for (int i = 0; i < a.size(); ++i) {
            if (a[i] != b[i]) {
                diff++;
                if (diff > 1) return false;
            }
        }
        return diff == 1;
    }

public:
    int ladderLength(std::string beginWord, std::string endWord, std::vector<std::string>& wordList) {
        std::unordered_set<std::string> dict(wordList.begin(), wordList.end());
        if (dict.find(endWord) == dict.end()) return 0;
        
        std::vector<std::string> words = wordList;
        words.push_back(beginWord);
        
        std::unordered_map<std::string, std::vector<std::string>> adj;
        int n = words.size();
        
        // All-pairs graph construction
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (isOneDiff(words[i], words[j])) {
                    adj[words[i]].push_back(words[j]);
                    adj[words[j]].push_back(words[i]);
                }
            }
        }
        
        std::queue<std::string> q;
        std::unordered_set<std::string> visited;
        q.push(beginWord);
        visited.insert(beginWord);
        
        int level = 1;
        while (!q.empty()) {
            int sz = q.size();
            for (int i = 0; i < sz; ++i) {
                std::string curr = q.front();
                q.pop();
                
                if (curr == endWord) return level;
                
                for (const std::string& neighbor : adj[curr]) {
                    if (visited.find(neighbor) == visited.end()) {
                        visited.insert(neighbor);
                        q.push(neighbor);
                    }
                }
            }
            level++;
        }
        
        return 0;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N^2 \times L)$
  - Where $N$ is length of `wordList` and $L$ is word length. Comparing all word pairs takes $\mathcal{O}(N^2 \times L)$ time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N^2 \times L)$
  - Stores all edges in the explicit graph adjacency list.

---

## Why This Approach Is Not Optimal

All-pairs comparison takes $\mathcal{O}(N^2 \times L)$ time, which TLEs when $N = 5000$. Using **On-the-Fly 26-Letter Character Substitution BFS**, we generate neighbors dynamically in $\mathcal{O}(N \times L \times 26)$ time!
