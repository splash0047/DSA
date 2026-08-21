# 04 Interview Follow-ups: Word Pattern

## 1. What if `s` is an infinite stream of words?
- Stream words one-by-one from a socket/file reader rather than pre-tokenizing the entire string into memory.
- If stream terminates before pattern or pattern exhausts first, return `false`.
