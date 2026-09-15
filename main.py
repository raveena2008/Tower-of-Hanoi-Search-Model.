from collections import deque


class TowerOfHanoiSearch:
    def __init__(self, disks):
        self.disks = disks
        self.start = tuple(
            [tuple(range(disks, 0, -1)), (), ()]
        )
        self.goal = ((), (), tuple(range(disks, 0, -1)))

    def get_moves(self, state):
        moves = []

        for source in range(3):
            if not state[source]:
                continue

            disk = state[source][-1]

            for target in range(3):
                if source == target:
                    continue

                if not state[target] or state[target][-1] > disk:
                    new_state = [list(rod) for rod in state]

                    new_state[target].append(
                        new_state[source].pop()
                    )

                    moves.append(
                        (tuple(tuple(rod) for rod in new_state),
                         source, target)
                    )

        return moves

    def bfs(self):
        queue = deque([(self.start, [])])
        visited = {self.start}

        while queue:
            state, path = queue.popleft()

            if state == self.goal:
                return path

            for new_state, source, target in self.get_moves(state):
                if new_state not in visited:
                    visited.add(new_state)

                    new_path = path + [
                        (source + 1, target + 1)
                    ]

                    queue.append((new_state, new_path))

        return None

    def display_solution(self):
        solution = self.bfs()

        if solution is None:
            print("No solution found.")
            return

        print("\nTower of Hanoi Search Model")
        print("---------------------------")
        print("Number of disks:", self.disks)
        print("Algorithm: Breadth-First Search")
        print("Total moves:", len(solution))
        print("\nSolution steps:")

        for step, move in enumerate(solution, 1):
            source, target = move
            print(
                f"Step {step}: Move disk from "
                f"Tower {source} to Tower {target}"
            )


if __name__ == "__main__":
    try:
        disks = int(input("Enter number of disks: "))

        if disks <= 0:
            print("Please enter a positive number.")
        elif disks > 8:
            print("Please enter 8 or fewer disks.")
        else:
            model = TowerOfHanoiSearch(disks)
            model.display_solution()

    except ValueError:
        print("Please enter a valid number.")
