# Tower of Hanoi – Search Model / State Space

## 1. Problem Statement

The Tower of Hanoi is a classic problem involving three rods and a number of disks.

The objective is to move all disks from the source rod to the destination rod using an auxiliary rod.

### Rules

1. Only one disk can be moved at a time.
2. Only the top disk of a rod can be moved.
3. A larger disk cannot be placed on a smaller disk.
4. All disks must be moved from the source rod to the destination rod.

This project models the Tower of Hanoi problem as a **State Space Search Problem**.

---

## 2. Project Objective

The main objectives of this project are:

- To represent the Tower of Hanoi problem using states.
- To generate valid movements between states.
- To apply search techniques to find a solution.
- To understand state space representation.
- To display the sequence of moves required to solve the problem.

---

## 3. Approach

The Tower of Hanoi problem is represented using a state space model.

### State Representation

Each state represents the arrangement of disks on the three rods.

For example:

```text
State = ((3, 2, 1), (), ())
