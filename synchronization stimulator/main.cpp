#include <cstdlib>
#include "base_case.h"
#include "lock_variable_approach.h"

int main(int argc, char* argv[]) {

    // thay đổi phần này để test
    
    auto solution = new LockVariableSolution();
    auto enter_critical_section_1 = solution->enter_critical_section;
    auto exit_critical_section_1  = solution->exit_critical_section;
    auto enter_critical_section_2 = solution->enter_critical_section;
    auto exit_critical_section_2  = solution->exit_critical_section;

    
    // nhận tham số từ cmd
    if (argc < 2) {
        cout << "Usage: program <test_case> [rounds]" << endl;
        return 1;
    }
    int test_case = atoi(argv[1]);
    int rounds = (argc >= 3) ? atoi(argv[2]) : 100;

    if (test_case == 1) {
        cout << "Testing mutual exclusion" << endl;
        solution->test_mutual_exclusion(
            rounds, 
            enter_critical_section_1, exit_critical_section_1,
            enter_critical_section_2, exit_critical_section_2
        );
    }
    else if (test_case == 2) {
        cout << "Testing progress" << endl;
        solution->test_progress(
            rounds, 
            enter_critical_section_1, exit_critical_section_1,
            enter_critical_section_2, exit_critical_section_2
        );
    }
    else if (test_case == 3) {
        cout << "Testing bounded waiting" << endl;
        solution->test_bounded_waiting(
            rounds, 1000,
            enter_critical_section_1, exit_critical_section_1,
            enter_critical_section_2, exit_critical_section_2
        );
    }
    else {
        cout << "Invalid test_case" << endl;
    }

    delete solution; // cleanup
    return 0;
}
