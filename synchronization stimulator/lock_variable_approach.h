#pragma once
#include "base_case.h"
#include <mutex>

extern std::mutex print_mtx;

class LockVariableSolution : public BaseSolution {
public:
    static int lock;
public:
    static void enter_critical_section();
    static void exit_critical_section();
};
