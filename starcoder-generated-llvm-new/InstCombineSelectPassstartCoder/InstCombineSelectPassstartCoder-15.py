
```c
#include <stdio.h>

int main() {
    float a = 5.0; // declare a float variable
    float b = 3.4; // declare another float variable
    float c = 2.1; // declare a third float variable
    float result;

    // Use a floating-point comparison to create a condition
    if (a > b) {
        result = a;
    } else {
        result = b;
    }

    // Use a select-like pattern with a floating-point comparison
    result = (a > b) ? a : b;

    // Print the result to ensure the code is not optimized away
    printf("Result: %f\n", result);

    return 0;
}
```

