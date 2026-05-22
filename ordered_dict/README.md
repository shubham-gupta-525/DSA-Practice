# Collections.OrderedDict – HackerRank Solution

## Problem Statement

You are given a list of items purchased in a supermarket along with their prices.

Your task is to calculate the **net price** for each unique item while maintaining the order of their **first occurrence**.

- `item_name` → Name of the item
- `net_price` → Total price accumulated for that item

The order of output must match the order in which items first appeared.

---

## Example

### Input
```text
9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30
```

### Output
```text
BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20
```

---

## Approach

We use Python's `OrderedDict` from the `collections` module because:

- It preserves insertion order.
- It allows easy updating of item totals.

### Steps
1. Read the number of items.
2. Extract item name and price from each input line.
3. Store items in an `OrderedDict`.
4. If the item already exists, add the price.
5. Otherwise, insert it into the dictionary.
6. Print the final accumulated totals.

---

## Python Solution

```python
from collections import OrderedDict

n = int(input())

items = OrderedDict()

for _ in range(n):
    data = input().split()

    # Item name may contain spaces
    item_name = " ".join(data[:-1])
    price = int(data[-1])

    if item_name in items:
        items[item_name] += price
    else:
        items[item_name] = price

for item, total in items.items():
    print(item, total)
```

---

## Complexity Analysis

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

Where `n` is the number of input items.

---

## Key Concepts Used

- `collections.OrderedDict`
- Dictionary operations
- String manipulation
- Input parsing

---

## Author

Solution implemented in **Python 3** for the HackerRank challenge.