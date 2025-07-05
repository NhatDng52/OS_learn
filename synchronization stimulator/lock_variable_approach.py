from multiprocessing import Process, Value
import time
from base_case import Base_solution
class LockVariableSolution(Base_solution):
    def __init__(self):
        super().__init__()
        self.lock = Value('i', 0)
    def enter_critical_section_1(self):
        while self.lock.value == 1:
            pass  # Chờ cho đến khi lock = 0
        self.lock.value = 1  # Đặt lock = 1 để vào critical section
    def exit_critical_section_1(self):
        self.lock.value = 0
    def enter_critical_section_2(self):
        while self.lock.value == 1:
            pass # Chờ cho đến khi lock = 0
        self.lock.value = 1
    def exit_critical_section_2(self):
        self.lock.value = 0
if __name__ == "__main__":
    solution = LockVariableSolution()
    print("Testing mutual exclusion:")
    solution.test_mutual_exclusion(rounds=20000)
    print("\nTesting progress:")
    solution.test_progress(rounds=200)
    print("\nTesting bounded waiting:")
    solution.test_bounded_waiting(rounds=200, sleep_time=0.01)  # sleep_time = 0.01 để p2 chậm hơn p1