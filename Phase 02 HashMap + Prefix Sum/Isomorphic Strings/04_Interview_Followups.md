# 04 Interview Follow-ups: Isomorphic Strings

## 1. What if Character Set is Unicode (UTF-32)?
- Fixed 256 array cannot hold $2^{20}$ code points.
- Use two `std::unordered_map<char32_t, int>` structures. Time remains $\mathcal{O}(N)$ average, space is $\mathcal{O}(U)$ where $U$ is distinct characters.
