from collections import deque


def get_valid_moves(state):
    """
    Generate all valid moves from the current state.
    """

    moves = []

    for source in range(3):
        if not state[source]:
            continue

        for target in range(3):
            if source == target:
                continue

            if not state[target] or state[source][-1] < state[target][-1]:

                new_state = [list(peg) for peg in state]

                disk = new_state[source].pop()
                new_state[target].append(disk)

                moves.append(
                    (
                        tuple(tuple(peg) for peg in new_state),
                        (source, target)
                    )
                )

    return moves


def solve_hanoi_bfs(number_of_disks):
    """
    Solve Tower of Hanoi using Breadth-First Search.
    """

    initial_state = (
        tuple(range(number_of_disks, 0, -1)),
        (),
        ()
    )

    goal_state = (
        (),
        (),
        tuple(range(number_of_disks, 0, -1))
    )

    queue = deque([(initial_state, [])])
    visited = {initial_state}

    while queue:

        current_state, path = queue.popleft()

        if current_state == goal_state:
            return path

        for next_state, move in get_valid_moves(current_state):

            if next_state not in visited:

                visited.add(next_state)

                queue.append(
                    (
                        next_state,
                        path + [move]
                    )
                )

    return None


def display_solution(number_of_disks):

    solution = solve_hanoi_bfs(number_of_disks)

    if solution is None:
        print("No solution found.")
        return

    print(f"Number of disks: {number_of_disks}")
    print(f"Minimum moves: {len(solution)}")
    print("\nMove sequence:")

    for step, (source, target) in enumerate(solution, start=1):

        print(
            f"Step {step}: Move disk from "
            f"Peg {source + 1} to Peg {target + 1}"
        )


if __name__ == "__main__":

    disks = int(input("Enter number of disks: "))

    display_solution(disks)
