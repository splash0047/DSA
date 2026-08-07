# 092. Online Stock Span

- **Platform**: LeetCode
- **Problem Number**: #901
- **Difficulty**: Medium
- **URL**: [LeetCode #901 - Online Stock Span](https://leetcode.com/problems/online-stock-span/)

---

## Problem Statement

Design an algorithm that collects daily price quotes for some stock and returns **the span** of that stock's price for the current day.

The **span** of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was **less than or equal to** the price of that day.

- For example, if the prices of the stock in the last four days were `[7, 3, 4, 12]` and the price of the stock today is `8`, then the span of today is `3` because starting from today and going backward, the price of the stock was less than or equal to `8` for `3` consecutive days.
- Also, if the prices of the stock in the last four days were `[7, 3, 4, 12]` and the price of the stock today is `7`, then the span of today is `1` because starting from today and going backward, the price of the stock was less than or equal to `7` for `1` consecutive day.

Implement the `StockSpanner` class:

- `StockSpanner()` Initializes the object of the class.
- `int next(int price)` Returns the **span** of the stock's price given the current day's `price`.

---

## Examples

### Example 1
```text
Input
["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
[[], [100], [80], [60], [70], [60], [75], [85]]
Output
[null, 1, 1, 1, 2, 1, 4, 6]

Explanation
StockSpanner stockSpanner = new StockSpanner();
stockSpanner.next(100); // return 1
stockSpanner.next(80);  // return 1
stockSpanner.next(60);  // return 1
stockSpanner.next(70);  // return 2
stockSpanner.next(60);  // return 1
stockSpanner.next(75);  // return 4, because the last 4 prices (including today's price of 75) were <= 75.
stockSpanner.next(85);  // return 6
```

---

## Constraints

- $1 \le \text{price} \le 10^5$
- At most $10^4$ calls will be made to `next`.
