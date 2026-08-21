# Word Pattern - Deep Explanation

## Walkthrough
Pattern: `"abba"`, Words: `["dog", "cat", "cat", "dog"]`
- `i=0`: `c='a'`, `w="dog"` $\to$ both not seen $\to$ set both to index $1$.
- `i=1`: `c='b'`, `w="cat"` $\to$ both not seen $\to$ set both to index $2$.
- `i=2`: `c='b'`, `w="cat"` $\to$ both had index $2$ $\to$ match! set both to index $3$.
- `i=3`: `c='a'`, `w="dog"` $\to$ both had index $1$ $\to$ match! set both to index $4$.
Result: `true`.
