def test_initial_state():
    initial_state = (("A", "B", "C"), (), ())

    assert initial_state[0] == ("A", "B", "C")
    assert initial_state[1] == ()
    assert initial_state[2] == ()


def test_goal_state():
    goal_state = ((), (), ("A", "B", "C"))

    assert goal_state[0] == ()
    assert goal_state[1] == ()
    assert goal_state[2] == ("A", "B", "C")


def test_minimum_moves():
    number_of_disks = 3
    expected_moves = 2**number_of_disks - 1

    assert expected_moves == 7


def test_single_disk():
    number_of_disks = 1
    expected_moves = 2**number_of_disks - 1

    assert expected_moves == 1
