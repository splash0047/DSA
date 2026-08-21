# 04 Interview Follow-ups & System Variations: Asteroid Collision

The problem finds the state of asteroids after all collisions (positive = moving right, negative = moving left). The optimal solution uses a **Stack** in $\mathcal{O}(N)$ time and $\mathcal{O}(N)$ space.

In technical interviews, this problem tests collision logic isolation, annihilation edge cases, and variable speed physical simulations.

---

## 1. Collision Decision Matrix

- Collision happens **IF AND ONLY IF**: `stack.top() > 0` (moving right) AND `current < 0` (moving left).
- **All other combinations never collide**:
  - Positive followed by Positive ($+ 	o +$): Moving same direction.
  - Negative followed by Negative ($-	o -$): Moving same direction.
  - Negative followed by Positive ($-	o +$): Moving away from each other.

---

## Summary Matrix: Trade-offs at a Glance

| Collision Case | Condition | Outcome |
| :--- | :--- | :--- |
| **Top Wins** | `abs(top) > abs(curr)` | `curr` destroyed; top survives |
| **Current Wins** | `abs(top) < abs(curr)` | `top` destroyed; re-check new top |
| **Mutual Annihilation**| `abs(top) == abs(curr)`| Both destroyed |
