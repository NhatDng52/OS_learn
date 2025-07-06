#include "tsl.h"

// Static member definition
std::atomic<int> TestAndSetSolution::lock{0};

// Method implementations
void TestAndSetSolution::enter_critical_section() {
    while (lock.exchange(1) == 1) {
        // busy wait
    }
}

void TestAndSetSolution::exit_critical_section() {
    lock.store(0);
}
