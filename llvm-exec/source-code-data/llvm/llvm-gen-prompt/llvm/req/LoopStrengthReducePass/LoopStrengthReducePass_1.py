#include <stdio.h>

int main() {
    int sum = 0; // Initialize a variable to accumulate the sum
    int i; // Loop counter

    // A simple loop with a linear induction variable
    for (i = 0; i < 10; i++) {
        sum += i; // Accumulate the sum of the loop counter
    }

    printf("Sum: %d\n", sum); // Print the result
    return 0;
}
