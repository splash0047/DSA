# Sum of Subarray Minimums - Deep Explanation

## Handling Duplicate Elements
Notice:
- Left uses `arr[st.top()] > arr[i]` (Strictly greater).
- Right uses `arr[st.top()] >= arr[i]` (Greater or equal).
This asymmetry strictly avoids double-counting identical minimum elements in subarrays.
