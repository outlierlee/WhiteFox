
```c
#include <stdio.h>

// Define a function that returns a non-zero integer value
int getNonZeroValue() {
    return 17; // or any other non-zero constant
}

int main() {
    int a = getNonZeroValue(); // Call the function to get a non-zero value
    int b = 0; // Initialize a variable to zero

    // Use a loop or conditional structure to create a PHI node scenario
    for(int i = 0; i < 10; i++) {
        if(i <= 5) {
            b = a; // Assign the non-zero value to b
        } else {
            b = 1; // Assign another non-zero value to b
        }

        // Compare the variable with zero
        if(b == 0) {
            printf("b is zero\n");
        } else {
            printf("b is non-zero\n");
        }
    }

    return 0;
}
```

