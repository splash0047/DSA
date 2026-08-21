# Design Circular Queue - Deep Explanation

## Modulo Arithmetic
`tail = (tail + 1) % capacity` wraps around to 0 when reaching capacity, maintaining $\mathcal{O}(1)$ insertion and deletion without memory relocation.
