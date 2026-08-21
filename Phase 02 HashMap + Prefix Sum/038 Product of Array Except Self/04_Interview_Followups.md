# 04 Interview Follow-ups & System Variations: Product of Array Except Self

The problem calculates the product of all elements except `nums[i]` without using the division operator. The standard optimal approach uses the output array for prefix products and a running scalar for suffix products in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ extra auxiliary space.

In technical interviews, this problem is used to test division-free arithmetic, zero-handling edge cases, parallel prefix scans (Hillis-Steele), and logarithmic transformations for numerical overflow prevention.

---

## 1. Why Division is Prohibited in Production Systems

### 🛑 The 3 Major Hazards of Division
1. **Division by Zero**: If any element is `0`, total product becomes 0, and division `0 / 0` triggers a runtime exception / crash.
2. **Loss of Floating-Point Precision**: In floating-point calculations, dividing large numbers introduces rounding jitter.
3. **Integer Truncation & Modulo Arithmetic**: Division in modular arithmetic requires computing the modular multiplicative inverse (Fermat's Little Theorem / Extended Euclidean Algorithm), which does not exist if values are not coprime with the modulus.

---

## 2. Low-Memory $\mathcal{O}(1)$ Extra Space Code Template

### 💡 Output Array Reuse + Single Suffix Scalar
```cpp
vector<int> productExceptSelf(vector<int>& nums) {
    int n = nums.size();
    vector<int> ans(n, 1);
    
    // Pass 1: ans[i] stores product of all elements to the left of i
    for (int i = 1; i < n; i++) {
        ans[i] = ans[i - 1] * nums[i - 1];
    }
    
    // Pass 2: Multiply with running suffix product from the right
    int suffix = 1;
    for (int i = n - 1; i >= 0; i--) {
        ans[i] *= suffix;
        suffix *= nums[i];
    }
    return ans;
}
```
- **Space Complexity**: $\mathcal{O}(1)$ auxiliary memory (output array does not count towards extra space).

---

## 3. What if Array Contains Zeros (The 3 Case Analysis)?

### 💡 Zero Breakdown
1. **$\ge 2$ Zeros**: Every single entry in the output array is strictly `0`.
2. **Exact 1 Zero at index $z$**:
   - `ans[z] = product of all non-zero elements`.
   - `ans[i] = 0` for all $i \neq z$.
3. **0 Zeros**: Standard prefix-suffix multiplication applies to all elements.

---

## 4. How to Parallelize Product Computation on GPU (Parallel Scan)?

### 💡 Hillis-Steele / Blelloch Parallel Prefix Scan
- On GPU / CUDA, computing prefix products sequentially takes $\mathcal{O}(N)$ time on 1 core.
- Using parallel scan algorithms across $P$ threads:
  - In step $d = 1, 2, 4, 8 \dots$: each thread $i$ multiplies its value with element at $i - 2^{d-1}$.
  - Runs in $\mathcal{O}(\log N)$ parallel steps on $N$ cores.

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Space Model | Time | Extra Memory | Handles Zeros? |
| :--- | :--- | :--- | :--- | :--- |
| **Total Product + Division** | Division allowed | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | Requires 3-case if-else |
| **Prefix & Suffix Arrays** | No division | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ | Naturally safe |
| **Output Buffer + Suffix Scalar**| No division | $\mathcal{O}(N)$ | **$\mathcal{O}(1)$** | **Naturally safe** |
| **Parallel Scan (GPU/SIMD)** | GPU threads | $\mathcal{O}(\log N)$ parallel | $\mathcal{O}(N)$ registers | Naturally safe |
