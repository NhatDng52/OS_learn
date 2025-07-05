from multiprocessing import Process, Value
import time
import sys

    
class Base_solution:
    def worker(self,name, sleep_time, shared_i,want, rounds,enter_critical_section= None, exit_critical_section=None):
        for _ in range(rounds):
            time.sleep(sleep_time)  # mô phỏng process này xử lý chậm
            if want == 0 and _== rounds - 1:
                print(f"{name}: changing want to 1 ")
                want = 1
            if want == 1:
                # enter critical section 
                enter_critical_section()
                val = shared_i.value
        
                val += 1
                shared_i.value = val
                print(f"{name}: i={shared_i.value}",flush=True)
                exit_critical_section()
                # exit critical section 
    def enter_critical_section_1(self):
        pass
    def exit_critical_section_1(self):
        pass
    def enter_critical_section_2(self):
        pass
    def exit_critical_section_2(self):
        pass
    def test_mutual_exclusion(self, rounds=1000):
        "Test mutual exclusion, kết khác round x2 thì sẽ không thỏa  "
        self.shared_i = Value('i', 0, lock=False)  # lock=False để thực sự share raw
        p1 = Process(target=self.worker, args=("P1", 0, self.shared_i,1, rounds, self.enter_critical_section_1, self.exit_critical_section_1))
        p2 = Process(target=self.worker, args=("P2", 0, self.shared_i,1, rounds, self.enter_critical_section_2, self.exit_critical_section_2))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        print("Final i =", self.shared_i.value)
    def test_progress(self, rounds=200):
        "Test progress, nếu bị p2 bị chặn  vì p không muốn vào critical section thì p2 sẽ print đúng 1 dòng ở cuối do p1 chuyển want ở cuối, nếu không thì p2 print trước p1"   
        self.shared_i = Value('i', 0, lock=False)  # lock=False để thực sự share raw
        p1 = Process(target=self.worker, args=("P1", 0, self.shared_i,0, rounds, self.enter_critical_section_1, self.exit_critical_section_1)) 
        p2 = Process(target=self.worker, args=("P2", 0, self.shared_i,1, 1     , self.enter_critical_section_2, self.exit_critical_section_2))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
    def test_bounded_waiting(self, rounds=1000,sleep_time=0.01):
        "Test bounded waiting,mặc dù p2 sleep lâu hơn p1 nhưng vẫn có thể vào critical section" 
        self.shared_i = Value('i', 0, lock=False)  # lock=False để thực sự share raw
        p1 = Process(target=self.worker, args=("P1", 0         , self.shared_i,1, rounds, self.enter_critical_section_1, self.exit_critical_section_1)) 
        p2 = Process(target=self.worker, args=("P2", sleep_time, self.shared_i,1, rounds, self.enter_critical_section_2, self.exit_critical_section_2))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        
        
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