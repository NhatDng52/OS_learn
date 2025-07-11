#pragma once
#include "base_case.h"
#include <mutex>

extern std::mutex print_mtx;

class StrictAlternationSolution : public BaseSolution {
public:
    static int turn;
public:
    static void enter_critical_section_1();
    static void exit_critical_section_1();
    static void enter_critical_section_2();
    static void exit_critical_section_2();
};
