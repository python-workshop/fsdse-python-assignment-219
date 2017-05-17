def can_win_nim(num_stones_left):
        if num_stones_left % 4 != 0:
            print("You Will Win")
            return True
        else:
            print("You will lose this game")
            return False
can_win_nim(4)
