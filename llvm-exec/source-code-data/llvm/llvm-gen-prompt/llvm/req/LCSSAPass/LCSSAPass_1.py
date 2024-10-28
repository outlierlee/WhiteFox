#include <stdio.h>

int main() {
    int result = 0; // declare a result variable

    // declare and initialize variables
    int a = 10;
    int b = 20;
    int c = 30;

    // create a loop with a condition that involves the variables
    for (int i = 0; i < 10; i++) {
        if (a < b) {
            result += a; // perform some operation
        } else {
            result += b;
        }
    }

    // create a condition that uses the result of the loop
    if (result > c) {
        printf("Result is greater than c\n");
    } else {
        printf("Result is less than or equal to c\n");
    }

    return 0; // return the result
}
