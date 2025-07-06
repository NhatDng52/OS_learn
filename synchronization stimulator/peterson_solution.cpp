#include "peterson_solution.h"

// lock biến kiểu tham chiếu để thật sự thay đổi biến gốc
void PetersonSolution::enter_critical_section_1() {
    want[0] = 1; // thread 1 wants to enter
    turn = 1; // set turn to thread 2
    while (want[1] == 1 && turn == 1) {
        // busy wait until thread 2 is done or turn is not 1
        // print_mtx.lock();
        // cout <<"flag j = " << want[1] << ", turn: " << turn << endl;
        // cout << "Thread 0 is waiting, turn: " << turn << endl;
        // print_mtx.unlock();
    }
    // print_mtx.lock();
    // cout<<"want[0] = " << want[0] << ", turn: " << turn << endl;
    // cout<<"want[1] = " << want[1] << ", turn: " << turn << endl;
    // print_mtx.unlock();
    this_thread::sleep_for(chrono::milliseconds(10)); // simulate some delay
}

void PetersonSolution::exit_critical_section_1() {
    this_thread::sleep_for(chrono::milliseconds(10)); // simulate some delay
    want[0] = 0; // thread 1 is done, reset its want
}
void PetersonSolution::enter_critical_section_2() {
    want[1] = 1; // thread 2 wants to enter
    turn = 0; // set turn to thread 1
    while (want[0] == 1 && turn == 0) {
        // print_mtx.lock();
        // cout <<"flag i = " << want[0] << ", turn: " << turn << endl;
        // cout << "Thread 1 is waiting, turn: " << turn << endl;
        // print_mtx.unlock();
        // // busy wait until thread 1 is done or turn is not 0
    }
    // print_mtx.lock();
    // cout<<"want[0] = " << want[0] << ", turn: " << turn << endl;
    // cout<<"want[1] = " << want[1] << ", turn: " << turn << endl;
    // print_mtx.unlock();
    this_thread::sleep_for(chrono::milliseconds(10)); // simulate some delay
}
void PetersonSolution::exit_critical_section_2() {
    this_thread::sleep_for(chrono::milliseconds(10)); // simulate some delay
    want[1] = 0; // thread 2 is done, reset its want
}
int PetersonSolution::turn = 0;
int PetersonSolution::want[2] = {0, 0}; // both threads initially do not want to enter