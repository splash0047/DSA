# Reverse Linked List II - Deep Explanation

## Step-by-Step Node Insertion
Initial: `prev -> 1`, `curr -> 2`, `temp -> 3` (Target: reverse 2 to 4)
- Step 1: Insert 3 before 2: `1 -> 3 -> 2 -> 4 -> 5`
- Step 2: Insert 4 before 3: `1 -> 4 -> 3 -> 2 -> 5`
Loop finishes in exactly `right - left` iterations with zero extra memory!
