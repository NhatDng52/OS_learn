import threading
import sys
from base_case import Base_solution

class PetersonSolution(Base_solution):
    def __init__(self):
        super().__init__()
        self.want = [0, 0]   # 0 = false, 1 = true
        self.turn = 0        # 0 hoặc 1

    def enter_critical_section_1(self, idx=0):
        self.want[0] = 1
        self.turn = 1
        while self.want[1] == 1 and self.turn == 1:
            pass  # busy wait

    def exit_critical_section_1(self, idx=0):
        self.want[0] = 0

    def enter_critical_section_2(self, idx=1):
        self.want[1] = 1
        self.turn = 0
        while self.want[0] == 1 and self.turn == 0:
            pass  # busy wait

    def exit_critical_section_2(self, idx=1):
        self.want[1] = 0

    def test_mutual_exclusion(self, rounds=100):
        self.shared_i = 0
        t1 = threading.Thread(target=self.worker, args=("T1", 0, rounds, 0, self.enter_critical_section_1, self.exit_critical_section_1))
        t2 = threading.Thread(target=self.worker, args=("T2", 0, rounds, 1, self.enter_critical_section_2, self.exit_critical_section_2))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        print("Final i =", self.shared_i)

    def test_progress(self, rounds=20):
        self.shared_i = 0
        self.want = [0, 1]
        t1 = threading.Thread(target=self.worker, args=("T1", 0, rounds, 0, self.enter_critical_section_1, self.exit_critical_section_1))
        t2 = threading.Thread(target=self.worker, args=("T2", 0, 1,     1, self.enter_critical_section_2, self.exit_critical_section_2))
        t1.start()
        t2.start()
        t1.join()
        t2.join()

    def test_bounded_waiting(self, rounds=100, sleep_time=0.01):
        self.shared_i = 0
        self.want = [1, 1]
        t1 = threading.Thread(target=self.worker, args=("T1", 0, rounds, 0, self.enter_critical_section_1, self.exit_critical_section_1))
        t2 = threading.Thread(target=self.worker, args=("T2", sleep_time, rounds, 1, self.enter_critical_section_2, self.exit_critical_section_2))
        t1.start()
        t2.start()
        t1.join()
        t2.join()

if __name__ == "__main__":
    base = PetersonSolution()
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
