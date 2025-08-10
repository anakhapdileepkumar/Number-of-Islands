# Island Counting in a Grid

## Description

This program counts the number of islands in a 2D grid where each cell is either:

- 'L' — Land
- 'W' — Water

An **island** is defined as a group of connected land cells. Two cells are connected if they are adjacent horizontally, vertically, **or diagonally** (8-direction adjacency).


## How it Works

- The grid is traversed cell by cell.
- For each unvisited land cell, a Depth-First Search (DFS) is performed to mark all land cells connected to it.
- Each DFS call corresponds to finding one distinct island.
- The total number of such DFS calls is the number of islands.


## Usage

1. Define the grid as a list of lists, with 'L' and 'W' characters.
2. Call the function `count_islands(grid)` to get the number of islands.
3. Example:

```python
grid = [
    ['W','L','W','W','L'],
    ['L','L','W','L','L'],
    ['W','W','L','W','W'],
    ['L','L','W','W','W'],
    ['W','W','L','L','L']
]

print(count_islands(grid))  # Output: 1
```

---
