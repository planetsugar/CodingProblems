from game_funcs import (
    does_user_want_to_quit,
    is_user_input_valid,
    display_board,
    mark_cell_as_selected,
    check_winner,
    has_cell_been_used,
    next_turn,
    is_draw,
    start_game,
)

display_board()
turn = "X"

while True:
    user_input = input(f"\nEnter a cell for {turn}: ")

    if does_user_want_to_quit(user_input):
        break
    elif not is_user_input_valid(user_input):
        print(f"\nThat input is not valid: {user_input}")
    elif has_cell_been_used(user_input):
        print(f"\nThat cell has been used: {user_input}")
    else:
        mark_cell_as_selected(user_input)

        winner = check_winner(turn)
        draw = is_draw()

        if winner or draw:
            display_board()
            if winner:
                print(f"\n*** {turn} IS THE WINNER ***")
            else:
                print("\n*** IT IS A DRAW ***")

            print("\n*** NEW GAME ***")
            start_game()
        else:
            turn = next_turn()

    display_board()
