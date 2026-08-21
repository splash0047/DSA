# 04 Interview Follow-ups & System Variations: LFU Cache

The LFU (Least Frequently Used) Cache evicts the least frequently used key, breaking frequency ties using LRU. The optimal design uses two Hash Maps: `key_to_node` and `freq_to_dll` alongside a `min_freq` scalar, achieving $\mathcal{O}(1)$ time for both `get` and `put`.

In top-tier technical interviews (FAANG Hard), this is the ultimate cache eviction design test. Interviewers probe frequency promotions, minimum frequency invariants, and W-TinyLFU (Caffeine Cache).

---

## 1. The Dual-Map Architecture & `min_freq` Invariant

### 💡 The Structural Components
1. **`key_map`**: `unordered_map<int, Node>` mapping `key -> {val, freq, ...}`.
2. **`freq_map`**: `unordered_map<int, DoublyLinkedList>` mapping `frequency -> DLL of nodes`.
3. **`min_freq` Scalar**: Tracks the global minimum frequency across all stored items.

### 💡 Frequency Increment Step (`updateFreq`)
- When a key is accessed via `get` or updated via `put`:
  - Remove node from `freq_map[node.freq]`.
  - If `freq_map[node.freq]` becomes empty AND `node.freq == min_freq`:
    - Increment `min_freq++`.
  - Increment `node.freq++`.
  - Insert node into head of `freq_map[node.freq]`.

### 💡 Eviction Step (When Cache is Full)
- Pop the tail node (LRU node) from `freq_map[min_freq]`.
- Erase its key from `key_map`.
- Set `min_freq = 1` for the new incoming key.

---

## 2. Real-World Systems Limitation of Pure LFU & Modern Evolution (W-TinyLFU)

### 🛑 The Historical Bias Flaw in Pure LFU
If an old key received 1,000,000 requests during a burst 1 hour ago and is never requested again, its frequency counter remains at 1,000,000, preventing newer useful keys from entering the cache.

### 💡 Modern Solution: W-TinyLFU (Used in Caffeine Cache)
- Combines a small **Window LRU** for burst items with a **Count-Min Sketch** frequency tracker with periodic aging (decaying all frequency counters over time).

---

## Summary Matrix: Trade-offs at a Glance

| Cache Type | Eviction Policy | Data Structures | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **LRU Cache** | Recency only | Map + 1 DLL | $\mathcal{O}(1)$ | $\mathcal{O}(C)$ |
| **LFU Cache** | Frequency + Recency tie-break | Map + Map of DLLs + `min_freq` | $\mathcal{O}(1)$ | $\mathcal{O}(C)$ |
| **W-TinyLFU** | Recency Window + Count-Min Sketch | Window LRU + Slotted Probabilistic Map | $\mathcal{O}(1)$ | Sublinear frequency memory |
