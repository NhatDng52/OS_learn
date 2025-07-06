#pragma once
#include <iostream>
#include <thread>
#include <mutex>
#include <string>
using namespace std;

extern mutex print_mtx;

class BaseSolution {
public:
    BaseSolution() = default;

    void worker(
        string name,
        int sleep_time_ms,
        int& shared_i,
        int want,
        int rounds,
        void (*enter_critical_section)() = nullptr,
        void (*exit_critical_section)() = nullptr
    );

    void test_mutual_exclusion(
        int rounds = 1000,
        void (*enter_critical_section_1)() = nullptr,
        void (*exit_critical_section_1)() = nullptr,
        void (*enter_critical_section_2)() = nullptr,
        void (*exit_critical_section_2)() = nullptr
        
    );

    void test_progress(
        int rounds = 20000,
        void (*enter_critical_section_1)() = nullptr,
        void (*exit_critical_section_1)() = nullptr,
        void (*enter_critical_section_2)() = nullptr,
        void (*exit_critical_section_2)() = nullptr
    );

    void test_bounded_waiting(
        int rounds = 1000,
        int sleep_time_ms = 100,
        void (*enter_critical_section_1)() = nullptr,
        void (*exit_critical_section_1)() = nullptr,
        void (*enter_critical_section_2)() = nullptr,
        void (*exit_critical_section_2)() = nullptr
    );
};
void dummy(); // Dummy function to be used as a placeholder for critical section functions
