# 04 Interview Follow-ups & System Variations: Backspace String Compare

The problem determines if two strings $S$ and $T$ are equal when typed into empty text editors where `'#'` represents a backspace character. While a Stack achieves $\mathcal{O}(M + N)$ time and $\mathcal{O}(M + N)$ space, the optimal solution scans backwards using **Two Pointers with Skip Counters** in $\mathcal{O}(M + N)$ time and strictly $\mathcal{O}(1)$ extra space.

In technical interviews, this problem is used to test stack elimination, editor buffer data structures (Gap Buffer, Rope), and streaming text comparison.

---

## 1. Why Scanning Backwards Eliminates the Need for a Stack

### 💡 The Forward vs. Backward Asymmetry
- **Scanning Forward**: When you encounter `'a'`, you cannot know if it will survive or be deleted by a future `'#'` without buffering all characters.
- **Scanning Backward**: When you encounter `'#'`, you know immediately that the **next non-backspace character to the left** must be deleted.
- By tracking `skip_count`:
  - If character is `'#'`, increment `skip_count++`.
  - If character is alphanumeric and `skip_count > 0`, decrement `skip_count--` and skip the character.
  - If character is alphanumeric and `skip_count == 0`, this character is an active surviving character ready for direct comparison.

---

## 2. Text Editor Follow-up: What if We Have Both Backspace and Cursor Movements?

### 🛑 The Scenario
Keyboard stream contains characters, `LEFT` arrow, `RIGHT` arrow, and `BACKSPACE`.

### 💡 Real-World Editor Data Structures
1. **Two Stacks (Left Stack & Right Stack)**:
   - Characters before cursor reside in `LeftStack`, characters after cursor reside in `RightStack`.
   - `LEFT`: Pop from `LeftStack`, push to `RightStack`.
   - `RIGHT`: Pop from `RightStack`, push to `LeftStack`.
   - `BACKSPACE`: Pop from `LeftStack`.
   - Used in classic text editor engines.
2. **Gap Buffer (Used in GNU Emacs)**:
   - A single contiguous dynamic array with a movable empty gap where typing and deleting occur in $\mathcal{O}(1)$ time.
3. **Rope / Piece Table (Used in VS Code)**:
   - Tree of immutable text chunks, avoiding massive memory copies when inserting or deleting text in 100MB+ files.

---

## 3. What if Strings Are 10GB Files Streaming Over a Network Pipe?

### 🛑 The Constraint
Data is read one-way from a socket; seeking backwards is impossible.

### 💡 Rolling Hash with Reversible Stack Tokens
- If streaming one-way, we must buffer tokens or use a streaming compression digest.
- Alternatively, if data is written to disk sequentially, stream in reverse from the file tail in 64KB blocks.

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Time | Space | Suitability |
| :--- | :--- | :--- | :--- |
| **Stack Simulation** | $\mathcal{O}(M+N)$ | $\mathcal{O}(M+N)$ | Simple forward parsing |
| **Backward Two Pointers** | $\mathcal{O}(M+N)$ | $\mathcal{O}(1)$ | Memory-constrained systems / Embedded |
| **Two Stacks (Cursor)** | $\mathcal{O}(1)$ / op | $\mathcal{O}(N)$ | Interactive text editors with arrow keys |
| **Gap Buffer / Piece Table** | $\mathcal{O}(1)$ amortized | $\mathcal{O}(N)$ | Production IDE text buffer management |
