# Tower of Hanoi Search Model

## Foundations of Artificial Intelligence

### Project Overview

The Tower of Hanoi Search Model is an AI-based project that represents the Tower of Hanoi puzzle as a state-space search problem.

The project uses Breadth-First Search (BFS) to explore possible disk configurations and find a path from the initial state to the goal state.

### Problem Statement

The Tower of Hanoi is a puzzle consisting of three pegs and a number of disks of different sizes.

The objective is to move all disks from the source peg to the destination peg while following these rules:

1. Only one disk can be moved at a time.
2. Only the top disk of a peg can be moved.
3. A larger disk cannot be placed on a smaller disk.

### Objectives

- Represent the puzzle using states.
- Generate valid disk movements.
- Apply state-space search techniques.
- Find a solution using Breadth-First Search.
- Display the solution steps.

### Algorithm Used

Breadth-First Search (BFS)

BFS explores the search space level by level.

Each valid Tower of Hanoi configuration is treated as a state.

The algorithm continues searching until the goal state is reached.

### Technologies Used

- Python
- Breadth-First Search
- State-Space Search
- GitHub

### Input

The user enters the number of disks.

Example:

3

### Output

The program displays the sequence of movements required to solve the puzzle.

Example:

Move 1: Tower 1 to Tower 3

Move 2: Tower 1 to Tower 2

Move 3: Tower 3 to Tower 2

### Project Structure

```text
Tower-of-Hanoi-Search-Model/
│
├── main.py
├── README.md
└── .gitignore
```