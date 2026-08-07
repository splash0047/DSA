# Reorganize String

## Pattern Used

- **Pattern**: **Greedy Choice + Max-Heap (Prev Pointer Holding)**
- **Concept**:
  - Count frequencies of all characters in `s`.
  - Impossibility Condition: If max character frequency is greater than `(N + 1) / 2`, it's impossible to place characters without adjacent duplicates $\implies$ return `""`.
  - Push `{frequency, char}` into a **Max-Heap**.
  - Maintain a `prev` holding variable initialized to `{0, '#'}`.
  - At each step:
    - Pop the most frequent character `curr` from Max-Heap.
    - Append `curr.char` to the result string.
    - Decrement `curr.freq`.
    - If `prev.freq > 0`, re-insert `prev` back into the Max-Heap.
    - Update `prev = curr`.

---

## Observation

1. To avoid placing identical characters side-by-side, we should prioritize placing characters with the **highest remaining frequency** first!
2. Holding the previously placed character `prev` temporarily out of the heap prevents it from being picked twice in immediate succession.

---

## Intuition

Always pick the character that appears most often, append it to our result, and temporarily hold it aside. In the next step, pick the second most frequent character. Then release the held character back into the choice pool.

---

## Algorithm

1. Count frequency of each character in `unordered_map<char, int> freq`.
2. Check max frequency: If `max_freq > (n + 1) / 2`, return `""`.
3. Push `{count, char}` into `priority_queue<pair<int, char>> maxHeap`.
4. `pair<int, char> prev = {0, '#'}`.
5. While `!maxHeap.empty()`:
   a. `auto curr = maxHeap.top(); maxHeap.pop();`
   b. `ans += curr.second;`
   c. `curr.first--;`
   d. If `prev.first > 0`: `maxHeap.push(prev)`.
   e. `prev = curr`.
6. Return `ans`.

---

## Clean C++17 Solution

```cpp
#include <string>
#include <vector>
#include <unordered_map>
#include <queue>

class Solution {
public:
    std::string reorganizeString(std::string s) {
        int n = s.size();
        std::unordered_map<char, int> freq;
        int maxFreq = 0;
        
        for (char c : s) {
            freq[c]++;
            maxFreq = std::max(maxFreq, freq[c]);
        }
        
        // Impossibility Pigeonhole principle check
        if (maxFreq > (n + 1) / 2) {
            return "";
        }
        
        // Max-heap storing pair<frequency, character>
        std::priority_queue<std::pair<int, char>> maxHeap;
        for (const auto& [ch, count] : freq) {
            maxHeap.push({count, ch});
        }
        
        std::string ans = "";
        std::pair<int, char> prev = {0, '#'};
        
        while (!maxHeap.empty()) {
            auto curr = maxHeap.top();
            maxHeap.pop();
            
            ans += curr.second;
            curr.first--; // Use one instance
            
            // Re-insert previously used character if it still has remaining frequency
            if (prev.first > 0) {
                maxHeap.push(prev);
            }
            
            // Update prev to current character
            prev = curr;
        }
        
        return ans;
    }
};
```

---

## Dry Run

### Input
- `s = "aab"`

### Execution Trace

1. `freq = {'a': 2, 'b': 1}`. `n = 3`, `maxFreq = 2 <= (3+1)/2 = 2`. Valid!
2. `maxHeap`: `[{2, 'a'}, {1, 'b'}]`. `prev = {0, '#'}`.
3. Iteration 1:
   - Pop `{2, 'a'}`. `ans = "a"`. Decrement to `{1, 'a'}`.
   - `prev.first` (0) not > 0.
   - `prev` becomes `{1, 'a'}`.
4. Iteration 2:
   - Pop `{1, 'b'}`. `ans = "ab"`. Decrement to `{0, 'b'}`.
   - `prev` `{1, 'a'}` pushed back into `maxHeap`.
   - `prev` becomes `{0, 'b'}`.
5. Iteration 3:
   - Pop `{1, 'a'}`. `ans = "aba"`. Decrement to `{0, 'a'}`.
   - `prev` `{0, 'b'}` not pushed.
   - `prev` becomes `{0, 'a'}`.
6. `maxHeap` empty. Return `"aba"`.

### Result
- Output: `"aba"`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N \log \Sigma)$
  - Where $N$ is string length and $\Sigma \le 26$ is alphabet size.
  - Heap operations take $\mathcal{O}(\log 26) = \mathcal{O}(1)$ time.
  - Total time is linear $\mathcal{O}(N)$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(\Sigma) = \mathcal{O}(1)$
  - Priority queue stores at most 26 elements.

---

## Why This is Optimal

- Always greedy-selects the character with largest remaining frequency while strictly preventing adjacent identical placements.
- Runs in linear $\mathcal{O}(N)$ time.

---

## Common Mistakes

1. **Missing Impossibility Check**: Failing to check `maxFreq > (n + 1) / 2` up front.
2. **Re-inserting Immediately**: Re-inserting `curr` immediately into `maxHeap` before picking the next character permits adjacent duplicate placement!
