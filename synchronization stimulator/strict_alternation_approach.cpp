#include "strict_alternation_approach.h"

// lock biến kiểu tham chiếu để thật sự thay đổi biến gốc
void StrictAlternationSolution::enter_critical_section_1() {
    while (turn != 0) {
    }
    this_thread::sleep_for(chrono::milliseconds(10)); // simulate some delay
}

void StrictAlternationSolution::exit_critical_section_1() {
    this_thread::sleep_for(chrono::milliseconds(10)); // simulate some delay
    turn = 1; // switch to the other thread
}
void StrictAlternationSolution::enter_critical_section_2() {
    while (turn != 1) {
    }
    this_thread::sleep_for(chrono::milliseconds(10)); // simulate some delay
}
void StrictAlternationSolution::exit_critical_section_2() {
    this_thread::sleep_for(chrono::milliseconds(10)); // simulate some delay
    turn = 0; // switch to the other thread
}
int StrictAlternationSolution::turn = 0;