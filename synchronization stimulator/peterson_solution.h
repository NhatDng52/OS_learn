#pragma once
#include "base_case.h"
#include <mutex>

extern std::mutex print_mtx;

class PetersonSolution : public BaseSolution {
public:
    static int turn;
    static int want[2];
public:
    static void enter_critical_section_1();
    static void exit_critical_section_1();
    static void enter_critical_section_2();
    static void exit_critical_section_2();
};

int PetersonSolution::turn = 0;
int PetersonSolution::want[2] = {0, 0}; // both threads initially do not want to enter