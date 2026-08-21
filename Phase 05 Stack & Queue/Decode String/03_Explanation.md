# Decode String - Deep Explanation

## Walkthrough: `"3[a2[c]]"`
1. `currNum = 3`
2. `'['` $\to$ push `3` and `""`
3. `c = 'a'` $\to$ `currStr = "a"`
4. `currNum = 2`
5. `'['` $\to$ push `2` and `"a"`
6. `c = 'c'` $\to$ `currStr = "c"`
7. `']'` $\to$ pop `2` and `"a"`, `currStr = "a" + "cc" = "acc"`
8. `']'` $\to$ pop `3` and `""`, `currStr = "" + "accaccacc" = "accaccacc"`
