#include "lock_variable_approach.h"

// lock biến kiểu tham chiếu để thật sự thay đổi biến gốc
void LockVariableSolution::enter_critical_section() {
    while (lock != 0) {
    }
    this_thread::sleep_for(chrono::milliseconds(10)); // simulate some delay
    lock = 1; // acquire lock
}

void LockVariableSolution::exit_critical_section() {
    this_thread::sleep_for(chrono::milliseconds(10)); // simulate some delay
    lock = 0; // release lock
}

int LockVariableSolution::lock = 0;