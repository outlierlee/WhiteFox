
```c
#include <stdio.h>

int main() {
    int initial_value_1 = 10;
    int initial_value_2 = 20;
    int common_result;

    if (initial_value_2 > 10) {
        common_result = initial_value_1 + initial_value_2;
    } else {
        common_result = initial_value_1 - initial_value_2;
    }

    printf("%d\n", common_result);

    return 0;
}
```

This C++ script performs the same logic as the example in c. It initializes two variables, then checks if variable initial_value_2 is greater than 10. If it is, the result will be the sum of initial_value_1 and initial_value_2, otherwise the result will be the difference of initial_value_1 and initial_value_2. The result is then printed to the console.

