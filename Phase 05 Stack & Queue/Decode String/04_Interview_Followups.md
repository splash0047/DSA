# 04 Interview Follow-ups: Decode String

## 1. What if Decoded String Exceeds RAM (e.g. `1000000[a]`)?
- Stream chunks directly to disk/output socket without holding the expanded string in RAM.
