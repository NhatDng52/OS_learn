import csv
import sys


# đọc thuật toán từ command line
if len(sys.argv) < 2:
    print("Vui lòng nhập tên thuật toán, ví dụ: python schedule.py sjf")
    sys.exit(1)

algorithm = sys.argv[1].lower()   # vd: sjf
# đọc file process.csv
processes = []

with open('process.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # ép kiểu nếu cần
        process = (
            row['pid'],
            int(row['arrival_time']),
            int(row['burst_time']),
            int(row['priority'])
        )
        processes.append(process)

def fcfs(processes):
    time = 0
    schedule = []
    processes.sort(key=lambda x: x[1])  # Sắp xếp theo arrival_time
    # print("Processes sorted by arrival time:", processes)
    for pid, arrival_time, burst_time, priority in processes:
        if time < arrival_time:
            schedule.append(("idle", time, arrival_time))
            time = arrival_time  # Chờ đến khi process đến
            
        temp = time
        time += burst_time 
        schedule.append((pid, temp, time))
    print("FCFS Schedule:\n", schedule)
    
def sjf(processes):
    time = 0
    schedule = []
    processes.sort(key=lambda x: x[1])  # Sắp xếp theo arrival_time
    # print("Processes sorted by arrival time:", processes)
    queue = []
    while processes or queue:
        if processes and time < processes[0][1] :
            schedule.append(("idle", time, processes[0][1] ))
            time = processes[0][1]
        while processes and processes[0][1] <= time:
            queue.append(processes.pop(0))
        queue.sort(key=lambda x: x[2]) # Sắp xếp theo burst_time
        if queue:
            pid, arrival_time, burst_time, priority = queue.pop(0)
            temp = time
            time += burst_time
            schedule.append((pid, temp, time))
    print("SJF Schedule:\n", schedule)       
            
            
        
if __name__ == "__main__":
    if algorithm == 'fcfs':
        fcfs(processes)
    elif algorithm == 'sjf':
        sjf(processes)
    else:
        print(f"Thuật toán {algorithm} chưa được hỗ trợ.")
        sys.exit(1)
    