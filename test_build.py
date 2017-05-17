import sys
from nim import can_win_nim


def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
    
test(can_win_nim(4) == False)
test(can_win_nim(5) == True)
