#include <stdio.h>

int main() {
    float a = ANY_FLOAT_VALUE; // declare a float variable
    float b = ANY_FLOAT_VALUE; // declare another float variable
    float c = ANY_FLOAT_VALUE; // declare a third float variable
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
