import threading
import time
import sys
class Base_solution:
    def worker(self,name, sleep_time, shared_i,want, rounds,enter_critical_section= None, exit_critical_section=None):
        for _ in range(rounds):
            time.sleep(sleep_time)
            if want == 0 and _== rounds - 1:
                print(f"{name}: changing want to 1 ")
                want = 1
            if want == 1:
                enter_critical_section()
                val = shared_i[0]
                val += 1
                shared_i[0] = val
                print(f"{name}: i={shared_i[0]}", flush=True)
                exit_critical_section()
                
    def enter_critical_section_1(self):
        pass
    def exit_critical_section_1(self):
        pass
    def enter_critical_section_2(self):
        pass
    def exit_critical_section_2(self):
        pass
    
    def test_mutual_exclusion(self, rounds=1000):
        self.shared_i = [0]   # dùng list 1 phần tử làm shared
        t1 = threading.Thread(target=self.worker, args=("T1", 0, self.shared_i,1, rounds,self.enter_critical_section_1,self.exit_critical_section_1))
        t2 = threading.Thread(target=self.worker, args=("T2", 0, self.shared_i,1, rounds,self.enter_critical_section_2,self.exit_critical_section_2))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        print("Final i =", self.shared_i[0])
        
    def test_progress(self, rounds=20000):
        self.shared_i = [0]
        t1 = threading.Thread(target=self.worker, args=("T1", 0, self.shared_i,0, rounds,self.enter_critical_section_1,self.exit_critical_section_1))
        t2 = threading.Thread(target=self.worker, args=("T2", 0, self.shared_i,1, 1,self.enter_critical_section_2,self.exit_critical_section_2))
        t1.start()
        t2.start()
        t1.join()
        t2.join()

    def test_bounded_waiting(self, rounds=1000,sleep_time=0.01):
        self.shared_i = [0]
        t1 = threading.Thread(target=self.worker, args=("T1", 0, self.shared_i,1, rounds,self.enter_critical_section_1,self.exit_critical_section_1))
        t2 = threading.Thread(target=self.worker, args=("T2", sleep_time, self.shared_i,1, rounds,self.enter_critical_section_2,self.exit_critical_section_2))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
if __name__ == "__main__":
    base = Base_solution()
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