# 04 Interview Follow-ups & System Variations: LRU Cache

The LRU (Least Recently Used) Cache problem designs a data structure with `get(key)` and `put(key, value)` operating in strictly $\mathcal{O}(1)$ average time. The optimal solution uses a **Hash Map** combined with a **Doubly Linked List (DLL)** with dummy head and tail nodes.

In system design and senior engineering interviews, LRU Cache is the absolute centerpiece. Interviewers test concurrency, sharded caches, lock-free eviction, and Redis-style approximations.

---

## 1. Why a Doubly Linked List (DLL) Instead of a Singly Linked List?

### 🛑 The Deletion Bottleneck
- In a Singly Linked List, deleting a node requires finding its **previous node**, which takes $\mathcal{O}(N)$ traversal time.
- In a Doubly Linked List, given a pointer to a node `Node*`, we can unlink it in strictly $\mathcal{O}(1)$ time:
  ```cpp
  node->prev->next = node->next;
  node->next->prev = node->prev;
  ```

---

## 2. Multi-Threading & Concurrency in High-Scale Systems

### 🛑 Global Lock Contention
In high-throughput systems, protecting an LRU Cache with a single global mutex creates a severe performance bottleneck.

### 💡 3 Production Concurrency Strategies
1. **Sharded / Partitioned LRU (e.g., Guava Cache / Caffeine)**:
   - Partition keys across $S$ independent LRU segments via `hash(key) % S`.
   - Each shard has its own independent mutex, reducing lock contention by $S	imes$.
2. **Read-Write Lock (Shared Mutex)**:
   - `get()` acquires shared read lock; `put()` acquires exclusive write lock.
   - *Gotcha*: In strict LRU, `get()` updates node position (write operation!), requiring promotion queues (read buffers) drained asynchronously.
3. **Approximated LRU (Redis Algorithm)**:
   - Instead of maintaining a strict DLL (which consumes 24 bytes of pointer overhead per entry), sample $K = 5$ random keys and evict the one with the oldest timestamp.

---

## Summary Matrix: Trade-offs at a Glance

| Architecture | Strategy | Get / Put Latency | Concurrency | Memory Overhead |
| :--- | :--- | :--- | :--- | :--- |
| **Standard In-Memory** | Map + Doubly Linked List | $\mathcal{O}(1)$ | Single Thread | Map + 2 Pointers / node |
| **Sharded LRU** | $N$ Independent Strips | $\mathcal{O}(1)$ | High (Segmented Locks) | Moderate |
| **Sampled LRU (Redis)**| Random $K$-Sampling | $\mathcal{O}(1)$ | Lock-free / High | **0 Pointers (Ultra Low)** |
