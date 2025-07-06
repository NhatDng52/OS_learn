from multiprocessing import Process, Value
import sys
from base_case import Base_solution
class StrictAlternationSolution(Base_solution):
    def __init__(self):
        super().__init__()
        self.turn = Value('i', 0)
    def enter_critical_section_1(self):
        while self.turn.value !=0:
            pass
    def exit_critical_section_1(self):
        self.turn.value = 1
    def enter_critical_section_2(self):
        while self.turn.value != 1:
            pass
    def exit_critical_section_2(self):
        self.turn.value = 0
if __name__ == "__main__":
    base = StrictAlternationSolution()
    args = sys.argv


    if len(args) < 2:
        print("Usage: python a.py <test_case> [rounds]")
        print("test_case: 1=mutex, 2=progress, 3=bounded")
        sys.exit(1)

    test_case = int(args[1])
    rounds = int(args[2]) if len(args) >= 3 else 100

    if test_case == 1:
        print("Testing mutual exclusion")
        base.test_mutual_exclusion(rounds)
    elif test_case == 2:
        print("Testing progress")
        base.test_progress(rounds)
    elif test_case == 3:
        print("Testing bounded waiting")
        base.test_bounded_waiting(rounds)
    else:
        print("Invalid test_case")