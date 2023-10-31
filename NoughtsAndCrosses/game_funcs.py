valid_game_cells = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]

selections_X = set()
selections_O = set()

turn = "X"


def start_game():
    global selections_X, selections_O, turn
    selections_X = set()
    selections_O = set()
    turn = "X"


def is_user_input_valid(user_input):
    return user_input.lower() in valid_game_cells


def does_user_want_to_quit(user_input):
    return user_input.lower() == "quit"


def has_cell_been_used(cell):
    return cell in selections_X or cell in selections_O


def mark_cell_as_selected(cell, selectedXOrO=None):
    if (turn == "X" and selectedXOrO == None) or (
        selectedXOrO != None and selectedXOrO.lower() == "x"
    ):
        selections_X.add(cell)
    if (turn == "O" and selectedXOrO == None) or (
        selectedXOrO != None and selectedXOrO.lower() == "o"
    ):
        selections_O.add(cell)


def check_winner(checkXOrO):
    set_to_check = selections_X if checkXOrO.lower() == "x" else selections_O
    return (
        len(set_to_check.intersection(["a1", "a2", "a3"])) == 3
        or len(set_to_check.intersection(["b1", "b2", "b3"])) == 3
        or len(set_to_check.intersection(["c1", "c2", "c3"])) == 3
        or len(set_to_check.intersection(["a1", "b1", "c1"])) == 3
        or len(set_to_check.intersection(["a2", "b2", "c2"])) == 3
        or len(set_to_check.intersection(["a3", "b3", "c3"])) == 3
        or len(set_to_check.intersection(["a1", "b2", "c3"])) == 3
        or len(set_to_check.intersection(["a3", "b2", "c1"])) == 3
    )


def is_draw():
    return len(selections_X) + len(selections_O) == 9


def display_XOrO(cell):
    if cell.lower() in selections_X:
        return "X"
    if cell.lower() in selections_O:
        return "O"
    return " "


def display_board():
    print()
    rows = ["A", "B", "C"]
    columns = ["1", "2", "3"]
    print(" ", end=" ")
    for column_header in columns:
        print(column_header, end=" ")
    print(" ")
    print("  -----")
    for row in rows:
        print(row, end=" ")
        for column in columns:
            print(f"{display_XOrO(row+column)}", end=" ")
        print(" ")


def next_turn():
    global turn
    turn = "X" if turn == "O" else "O"
    return turn
