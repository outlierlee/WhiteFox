
```c
#include <stdio.h>

// Define a function that returns a non-zero integer value
int getNonZeroValue() {
    return 1; // or any other non-zero constant
}

int main() {
    int a = getNonZeroValue(); // Call the function to get a non-zero value
    
    for (int i = 0; i < 10; ++i) {
        int b = 0; // Initialize a variable to zero
        if (i % 2 == 0) {
            b = a; // Assign the non-zero value to b
        }

        // PHI node optimization scenario
        if (b - 1) {
            printf("b is non-zero\n");
        } else {
            printf("b is zero\n");
        }
    }

    return 0;
}
```
