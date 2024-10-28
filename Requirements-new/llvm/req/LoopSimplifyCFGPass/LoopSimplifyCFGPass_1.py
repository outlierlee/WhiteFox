#include <stdio.h>

int main() {
    int x = ANY_VALUE; // declare and initialize x
    int y = ANY_VALUE; // declare and initialize y

    // A loop with a condition that can be constant-folded
    while (x < CONSTANT_CONDITION) {
        // Perform some operations
        x = x OPERATOR y; // x is updated with an operation involving y
    }

    return x; // return the result
}
