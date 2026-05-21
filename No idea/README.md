    # No Idea! - Happiness Calculation

## Problem Statement
There is an array of integers. There are also two disjoint sets, **A** and **B**, each containing integers.

- You **like** all integers in set **A**
- You **dislike** all integers in set **B**

Your initial happiness is **0**.

For each integer in the array:

- If the integer exists in **A**, add **+1** to happiness.
- If the integer exists in **B**, subtract **-1** from happiness.
- Otherwise, happiness does not change.

At the end, output the final happiness value.

---

## Input Format
- First line contains two integers `n` and `m`
  - `n` = number of elements in the array
  - `m` = number of elements in each set

- Second line contains `n` integers (array elements)

- Third line contains `m` integers (set A)

- Fourth line contains `m` integers (set B)

---

## Output Format
Print a single integer representing the final happiness.

---

## Example

### Input
```text
3 2
1 5 3
3 1
5 7