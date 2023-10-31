from game_funcs import (
    is_user_input_valid,
    does_user_want_to_quit,
    mark_cell_as_selected,
    has_cell_been_used,
    check_winner,
    start_game,
    display_XOrO,
    display_board,
    next_turn,
    is_draw,
    valid_game_cells,
)


def setup_function(function):
    start_game()


def test_does_user_want_to_quit():
    assert does_user_want_to_quit("quit") == True
    assert does_user_want_to_quit("a1") == False


def test_is_user_input_valid():
    for cell in valid_game_cells:
        assert is_user_input_valid(cell) == True
    assert is_user_input_valid("broken") == False


def test_cell_selection():
    assert has_cell_been_used("b2") == False
    mark_cell_as_selected("b2")
    assert has_cell_been_used("b2") == True


def is_winning_selection(*args, character):
    mark_cell_as_selected(args[0], character)
    mark_cell_as_selected(args[1], character)
    mark_cell_as_selected(args[2], character)
    assert check_winner("X" if character == "X" else "O") == True
    assert check_winner("O" if character == "O" else "X") == True


def test_winning():
    assert check_winner("X") == False
    assert check_winner("O") == False

    # Horizontal
    is_winning_selection("a1", "a2", "a3", character="X")
    is_winning_selection("b1", "b2", "b3", character="X")
    is_winning_selection("c1", "c2", "c3", character="X")
    is_winning_selection("a1", "a2", "a3", character="O")
    is_winning_selection("b1", "b2", "b3", character="O")
    is_winning_selection("c1", "c2", "c3", character="O")

    # Vertical
    is_winning_selection("a1", "b1", "c1", character="X")
    is_winning_selection("a2", "b2", "c2", character="X")
    is_winning_selection("a3", "b3", "c3", character="X")
    is_winning_selection("a1", "b1", "c1", character="O")
    is_winning_selection("a2", "b2", "c2", character="O")
    is_winning_selection("a3", "b3", "c3", character="O")

    # Diagonals
    is_winning_selection("a1", "b2", "c3", character="X")
    is_winning_selection("a3", "b2", "c1", character="X")
    is_winning_selection("a1", "b2", "c3", character="O")
    is_winning_selection("a3", "b2", "c1", character="O")


def test_display_XOrO():
    mark_cell_as_selected("b2", "O")
    mark_cell_as_selected("a3", "X")
    assert display_XOrO("b2") == "O"
    assert display_XOrO("a3") == "X"


def test_display_board():
    for cell in valid_game_cells:
        mark_cell_as_selected(cell, "X")
    display_board()

    start_game()
    for cell in valid_game_cells:
        mark_cell_as_selected(cell, "O")
    display_board()


def test_next_turn():
    assert next_turn() == "O"  # Because a games always starts with 'X'
    assert next_turn() == "X"
    assert next_turn() == "O"  # Back to 0 after X


def test_is_draw():
    assert is_draw() == False
    for cell in valid_game_cells:
        mark_cell_as_selected(cell)
    assert is_draw() == True
