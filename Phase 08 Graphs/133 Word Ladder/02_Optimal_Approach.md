# Word Ladder

## Pattern Used

- **Pattern**: **On-the-Fly Character Substitution BFS** (or **Bidirectional BFS**)
- **Concept**:
  - Insert all words from `wordList` into an `unordered_set<string> wordSet` for $\mathcal{O}(1)$ existence checking.
  - If `endWord` is not in `wordSet`, return `0`.
  - Perform level-by-level BFS starting with `beginWord`:
    - For a word `curr` of length $L$:
      - Try changing each character from `'a'` to `'z'`.
      - If modified word `nextWord` exists in `wordSet`:
        - If `nextWord == endWord`, return `level + 1`.
        - Erase `nextWord` from `wordSet` (acts as visiting/marking).
        - Push `nextWord` into `queue`.

---

## Observation

1. Generating possible 1-character variations dynamically takes $L \times 26$ checks per word.
2. For short words ($L \le 10$), $L \times 26 \le 260$ operations per word, which is drastically faster than scanning $N = 5000$ words ($\mathcal{O}(N)$ vs $\mathcal{O}(L \times 26)$)!
3. Erasing visited words directly from `wordSet` eliminates the need for a separate `visited` set.

---

## Intuition

Think of the word transformation as a shortest path search in a state graph. At each step, generate all valid single-letter mutations of the current word. If a mutation exists in the dictionary, step into it and remove it from the dictionary so you never visit it again.

---

## Algorithm

1. `wordSet = unordered_set<string>(wordList.begin(), wordList.end())`.
2. If `endWord` not in `wordSet`, return `0`.
3. `queue<string> q`. Push `beginWord`. `level = 1`.
4. While `!q.empty()`:
   a. `sz = q.size()`.
   b. For `i` from `0` to `sz - 1`:
      - `curr = q.front(); q.pop();`
      - If `curr == endWord`, return `level`.
      - For position `p` from `0` to `L - 1`:
        - Save `origChar = curr[p]`.
        - For `ch` from `'a'` to `'z'`:
          - `curr[p] = ch`.
          - If `wordSet.count(curr)`:
            - `wordSet.erase(curr)`.
            - `q.push(curr)`.
        - Restore `curr[p] = origChar`.
   c. `level++`.
5. Return `0`.

---

## Clean C++17 Solution

```cpp
#include <string>
#include <vector>
#include <unordered_set>
#include <queue>

class Solution {
public:
    int ladderLength(std::string beginWord, std::string endWord, std::vector<std::string>& wordList) {
        std::unordered_set<std::string> wordSet(wordList.begin(), wordList.end());
        
        // If target endWord is not in dictionary, return 0
        if (wordSet.find(endWord) == wordSet.end()) {
            return 0;
        }
        
        std::queue<std::string> q;
        q.push(beginWord);
        
        int level = 1;
        
        // BFS Level Order Traversal
        while (!q.empty()) {
            int sz = q.size();
            
            for (int i = 0; i < sz; ++i) {
                std::string curr = q.front();
                q.pop();
                
                if (curr == endWord) {
                    return level;
                }
                
                // Try mutating every character of curr to 'a'-'z'
                for (int p = 0; p < curr.size(); ++p) {
                    char origChar = curr[p];
                    
                    for (char ch = 'a'; ch <= 'z'; ++ch) {
                        if (ch == origChar) continue;
                        
                        curr[p] = ch;
                        
                        // If mutated word exists in dictionary
                        if (wordSet.find(curr) != wordSet.end()) {
                            wordSet.erase(curr); // Mark as visited by erasing
                            q.push(curr);
                        }
                    }
                    
                    curr[p] = origChar; // Restore character
                }
            }
            
            level++;
        }
        
        return 0;
    }
};
```

---

## Dry Run

### Input
- `beginWord = "hit"`, `endWord = "cog"`, `wordList = ["hot","dot","dog","lot","log","cog"]`

### Execution Trace

- Level 1: `q = ["hit"]`, `wordSet = {"hot","dot","dog","lot","log","cog"}`.
  - Mutate `"hit"` $\implies$ finds `"hot"`. Erase `"hot"`. Push `"hot"`.
- Level 2: `q = ["hot"]`.
  - Mutate `"hot"` $\implies$ finds `"dot"`, `"lot"`. Erase them. Push `"dot"`, `"lot"`.
- Level 3: `q = ["dot", "lot"]`.
  - Mutate `"dot"` $\implies$ finds `"dog"`.
  - Mutate `"lot"` $\implies$ finds `"log"`.
  - Push `"dog"`, `"log"`.
- Level 4: `q = ["dog", "log"]`.
  - Mutate `"dog"` $\implies$ finds `"cog"`. Push `"cog"`.
- Level 5: Pop `"cog"` $\implies$ `curr == endWord` $\implies$ Return `level` = `5`.

### Result
- Output: `5`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N \times L \times 26)$
  - Where $N$ is number of words and $L$ is word length.
  - Generating and looking up mutations for each word takes $\mathcal{O}(L \times 26)$ time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N \times L)$
  - Hash set and queue store at most $N$ words of length $L$.

---

## Why This is Optimal

- On-the-fly character substitution reduces word neighbor lookup complexity from linear $\mathcal{O}(N)$ to constant $\mathcal{O}(L \times 26)$ for short words.
- Queue-based BFS guarantees finding the minimum transformation sequence length.

---

## Common Mistakes

1. **Not Restoring Character**: Forgetting `curr[p] = origChar` after inner loop alters the original string permanently.
2. **Missing `endWord` Check**: Forgetting to check if `endWord` exists in `wordList` up front.
