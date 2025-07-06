#include "base_case.h"

mutex print_mtx;  

void BaseSolution::worker(
    string name,
    int sleep_time_ms,
    int& shared_i,
    int want,
    int rounds,
    void (*enter_critical_section)(),
    void (*exit_critical_section)()
) {
    for (int i = 0; i < rounds; i++) {
        // this_thread::sleep_for(chrono::milliseconds(sleep_time_ms));
        if (want == 0 && i == rounds - 1) {
            print_mtx.lock();
            cout << name << ": changing want to 1" << endl;
            print_mtx.unlock();
            want = 1;
            this_thread::sleep_for(chrono::milliseconds(5000));
        }
        if (want == 1) {
            if (enter_critical_section) {
                enter_critical_section();
            }

            int val = shared_i;
            this_thread::sleep_for(chrono::milliseconds(10));
            val += 1;

            print_mtx.lock();
            cout << name << ": val=" << val << endl;
            print_mtx.unlock();

            this_thread::sleep_for(chrono::milliseconds(10));

            shared_i = val;

            if (exit_critical_section) {
                exit_critical_section();
            }
        }
    }
}

void BaseSolution::test_mutual_exclusion(
    int rounds,
    void (*enter_critical_section_1)(),
    void (*exit_critical_section_1)(),
    void (*enter_critical_section_2)(),
    void (*exit_critical_section_2)()
) {
    int shared_i = 0;
    thread t1(&BaseSolution::worker, this, "T1", 0, ref(shared_i), 1, rounds,
              enter_critical_section_1, exit_critical_section_1);
    thread t2(&BaseSolution::worker, this, "T2", 0, ref(shared_i), 1, rounds,
              enter_critical_section_2, exit_critical_section_2);
    t1.join();
    t2.join();
    cout << "Final i = " << shared_i << endl;
}

void BaseSolution::test_progress(
    int rounds,
    void (*enter_critical_section_1)(),
    void (*exit_critical_section_1)(),
    void (*enter_critical_section_2)(),
    void (*exit_critical_section_2)()
) {
    int shared_i = 0;
    thread t1(&BaseSolution::worker, this, "T1", 0, ref(shared_i), 0, rounds,
              enter_critical_section_1, exit_critical_section_1);
    thread t2(&BaseSolution::worker, this, "T2", 0, ref(shared_i), 1, 1,
              enter_critical_section_2, exit_critical_section_2);
    t1.join();
    t2.join();
}

void BaseSolution::test_bounded_waiting(
    int rounds,
    int sleep_time_ms,
    void (*enter_critical_section_1)(),
    void (*exit_critical_section_1)(),
    void (*enter_critical_section_2)(),
    void (*exit_critical_section_2)()
) {
    int shared_i = 0;
    thread t1(&BaseSolution::worker, this, "T1", 0, ref(shared_i), 1, rounds,
              enter_critical_section_1, exit_critical_section_1);
    thread t2(&BaseSolution::worker, this, "T2", sleep_time_ms, ref(shared_i), 1, rounds,
              enter_critical_section_2, exit_critical_section_2);
    t1.join();
    t2.join();
}

void dummy() {
    //do nothing
}