import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../src")
    )
)

from main import solve_hanoi_bfs


def test_three_disk_solution():
    solution = solve_hanoi_bfs(3)

    assert solution is not None
    assert len(solution) == 7


def test_one_disk_solution():
    solution = solve_hanoi_bfs(1)

    assert solution is not None
    assert len(solution) == 1


def test_two_disk_solution():
    solution = solve_hanoi_bfs(2)

    assert solution is not None
    assert len(solution) == 3
