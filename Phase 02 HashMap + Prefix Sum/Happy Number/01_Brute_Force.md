# Happy Number - Brute Force (Hash Set)

```cpp
#include <unordered_set>

class Solution {
    int getNext(int n) {
        int total = 0;
        while (n > 0) {
            int d = n % 10;
            total += d * d;
            n /= 10;
        }
        return total;
    }
public:
    bool isHappy(int n) {
        std::unordered_set<int> seen;
        while (n != 1 && !seen.count(n)) {
            seen.insert(n);
            n = getNext(n);
        }
        return n == 1;
    }
};
```
