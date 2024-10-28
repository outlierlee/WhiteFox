#include <stdio.h>

int main() {
    // Declare variables
    int x = ANY_VALUE; // Initialize x with any integer value
    int result;

    // Perform a multiplication operation that can be transformed
    // into a left shift operation by the compiler
    result = x * (1 << ANY_CONSTANT); // ANY_CONSTANT is a positive integer

    // Use the result in some way
    printf("%d\n", result);

    return 0;
}
