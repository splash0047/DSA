# 04 Interview Follow-ups & System Variations: Word Break

The problem determines if string $S$ can be segmented into dictionary words. Optimal approaches include **1D DP with Trie** in $\mathcal{O}(N^2 + \sum L)$ time and $\mathcal{O}(N + 	ext{Trie})$ space.

In technical interviews, this problem is extended to Word Break II (reconstructing all valid sentences via memoized DFS).

---

## 1. 1D DP with Trie Optimization

```cpp
bool wordBreak(string s, vector<string>& wordDict) {
    unordered_set<string> dict(wordDict.begin(), wordDict.end());
    int n = s.size();
    vector<bool> dp(n + 1, false);
    dp[0] = true;
    
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j < i; j++) {
            if (dp[j] && dict.count(s.substr(j, i - j))) {
                dp[i] = true;
                break;
            }
        }
    }
    return dp[n];
}
```

---

## Summary Matrix: Trade-offs at a Glance

| Problem | Goal | Optimal Approach | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Word Break I (#139)** | Boolean check | 1D Dynamic Programming | $\mathcal{O}(N^2)$ | $\mathcal{O}(N)$ |
| **Word Break II (#140)** | All sentences | Memoized DFS Backtracking | $\mathcal{O}(N^2 + 	ext{Sentences})$ | $\mathcal{O}(N^2)$ |
