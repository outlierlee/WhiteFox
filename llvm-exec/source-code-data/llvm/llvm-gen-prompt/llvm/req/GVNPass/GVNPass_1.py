#include <stdio.h>

// Define a function that contains a basic block structure
void example_function() {
    int a = 10; // Initialize a variable
    int b = 20; // Initialize another variable

    // Create a simple control flow with a conditional branch
    if (a < b) {
        a = a + 1; // Increment a
    } else {
        a = a - 1; // Decrement a
    }

    // Another conditional branch that can be optimized
    if (a < b) {
        a = a + 1; // Increment a again
    } else {
        a = a - 1; // Decrement a again
    }

    // Use the variable to prevent dead code elimination
    printf("%d\n", a);
}

int main() {
    example_function(); // Call the function
    return 0;
}
