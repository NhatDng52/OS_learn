#include "base_case.h"
#include <atomic>

class TestAndSetSolution : public BaseSolution {
private:
    static std::atomic<int> lock;

public:
    static void enter_critical_section() ;

    static void exit_critical_section() ;
};
