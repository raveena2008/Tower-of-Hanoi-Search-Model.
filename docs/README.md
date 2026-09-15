# Project Documentation

## Project Title
Tower of Hanoi Search Model – State Space

## 1. Introduction
The Tower of Hanoi is a mathematical puzzle involving three
pegs and a set of disks of different sizes.

This project models the puzzle as a state space and solves it
using Breadth-First Search (BFS).

## 2. Objective
- Represent the puzzle using peg configurations.
- Generate valid moves between states.
- Apply a search algorithm to find a solution.
- Display the sequence of moves from the initial state to the goal.

## 3. State Representation
Each state consists of three pegs.

Example for 3 disks:

Initial State:
((3, 2, 1), (), ())

Goal State:
((), (), (3, 2, 1))

The largest disk is represented by 3, and the smallest disk
is represented by 1.

## 4. Search Algorithm
Breadth-First Search (BFS) explores the state space level by
level.

Each valid disk movement generates a new state.

The algorithm maintains:
- A queue of unexplored states.
- A visited set to avoid repeated states.
- A path containing the moves taken.

## 5. Working Process
1. Initialize the puzzle with all disks on Peg 1.
2. Generate all possible valid moves.
3. Add new states to the BFS queue.
4. Check whether the goal state has been reached.
5. Return the sequence of moves.

## 6. Technologies Used
- Python
- Breadth-First Search
- State-Space Search
- GitHub
- Pytest

## 7. Expected Results
For 3 disks, the BFS algorithm should find a solution
requiring 7 moves.

For 2 disks, the solution requires 3 moves.

For 1 disk, the solution requires 1 move.

## 8. Conclusion
This project demonstrates how a familiar puzzle can be
represented as a state-space problem.

Instead of directly using recursive Tower of Hanoi logic,
the program explores possible configurations using BFS.
