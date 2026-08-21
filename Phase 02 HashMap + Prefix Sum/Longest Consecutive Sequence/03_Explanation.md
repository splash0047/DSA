# Longest Consecutive Sequence - Deep Explanation

## Why is the Inner Loop $\mathcal{O}(N)$ Overall?
At first glance, nested while loops look like $\mathcal{O}(N^2)$.
However, the `if (!num_set.count(num - 1))` guard ensures the inner loop ONLY runs for the very first element of each contiguous cluster.
Each number in the array is traversed at most twice (once in the outer loop, once in the inner loop).
Hence, amortized total operations is $2N = \mathcal{O}(N)$.
