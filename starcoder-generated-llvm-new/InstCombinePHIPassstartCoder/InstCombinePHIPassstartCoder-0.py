
```cpp
#include <stdio.h>

// Define a function that returns a non-zero integer value
int getNonZeroValue() {
    return 5; // or any other non-zero constant
}

int main() {
    int a = getNonZeroValue(); // Call the function to get a non-zero value
    int b = 0; // Initialize a variable to zero

    // Use a loop or conditional structure to create a PHI node scenario
    for (int i = 0; i < 10; ++i) {
        if (i % 2 == 0) {
            b = a; // Assign the non-zero value to b
        } else {
            b = 0xFFFFFFFFFFFFFFFF; // Assign zero to b
        }

        // Forcing comparision with zero
        if (a > b) {
            printf("a is positive\n");
        } else {
            printf("a is zero or negative\n");
        }
    }

    return 0;
}
```
