# Problem Summary

Given two strings `s` and `t` containing characters and backspaces `'#'`, determine if they are equal after backspaces are applied. The optimal approach scans **backwards from right to left** using Two Pointers and `skip` counters to ignore backspaced characters on the fly, comparing surviving characters in $\mathcal{O}(N + M)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- Leftward deletion operators (like backspaces or undo operations) modify past inputs.
- Backward traversal allows processing future control symbols *before* the data symbols they affect.

---

## Important Clues

1. **"#' means a backspace character"**: Backspace deletes preceding character.
2. **"O(1) extra space follow-up"**: Signals backward two-pointer scan.

---

## Example

### Input
`s = "ab#c"`, `t = "ad#c"`

### Visual Step-by-Step Progression

```text
s: "a b # c" <- i
    |   |___| (b deleted by #)
    'a'       'c' -> Resulting s: "ac"

t: "a d # c" <- j
    |   |___| (d deleted by #)
    'a'       'c' -> Resulting t: "ac"

Both yield "ac" -> return true
```

---

## Alternative Solutions

### Stack Simulation (O(N+M) Time, O(N+M) Space)
- Process `s` and `t` into string buffers using a stack.
- Compare resulting strings.

---

## Edge Cases

1. **All Characters Deleted**: `s = "a#b#"`, `t = "c#d#"` -> Both reduce to `""`, returns `true`.
2. **More Backspaces than Characters**: `s = "a###"`, `t = ""` -> Returns `true`.
3. **Different Length Output**: `s = "ab#c"`, `t = "a"` -> Returns `false`.

---

## Interview Tips

- **Explain Why Backward Scan Eliminates Stack**: State *"By scanning backwards, we encounter backspaces before the characters they delete. We can simply maintain a `skip` counter without allocating a stack."*

---

## Similar Problems

1. [LeetCode #1047: Remove All Adjacent Duplicates In String](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/)
2. [LeetCode #1598: Crawler Log Folder](https://leetcode.com/problems/crawler-log-folder/)

---

## Revision Notes

- Problem: Compare strings with backspaces `'#'`.
- Strategy: Two Pointers scanning backwards (`i = s.length() - 1`, `j = t.length() - 1`).
- Maintain `skip_s`, `skip_t`.
- Inner loops skip backspaced chars:
  - If `s[i] == '#'`: `skip_s++`, `i--`.
  - Else if `skip_s > 0`: `skip_s--`, `i--`.
  - Else: break to target valid char.
- Compare valid chars `s[i] == t[j]`.
- Optimal Complexity: Time $\mathcal{O}(N + M)$, Space $\mathcal{O}(1)$.
