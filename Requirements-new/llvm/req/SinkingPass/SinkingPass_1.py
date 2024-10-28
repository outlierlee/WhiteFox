#include <stdio.h>

int main() {
    int a = 10; // Declare and initialize a variable
    int b = 20; // Declare and initialize another variable
    int c; // Declare a variable to store the result

    if (a > 5) { // Conditional block
        c = a + b; // Perform an operation
    } else {
        c = a - b; // Perform a different operation
    }

    printf("%d\n", c); // Use the result

    return 0;
}
