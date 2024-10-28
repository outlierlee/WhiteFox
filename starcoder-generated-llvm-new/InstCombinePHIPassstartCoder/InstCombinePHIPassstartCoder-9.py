
```c
#include <stdio.h>

// Define a function that returns a non-zero integer value
int getNonZeroValue() {
    return 42; 
}

int main() {
    int a = getNonZeroValue(); // Call the function to get a non-zero value
    int b = 0; // Initialize a variable to zero

    // Use a loop or conditional structure to create a PHI node scenario
    for (int j = 0; j < 10; ++j) {
        if (j % 2 == 0) {
            b = a; // Assign the non-zero value to b
        } else {
            b = 0; // Assign zero to b
        }

        // Compare the variable with zero
        if (b == 0) {
            printf("b is zero\n");
        } else {
            printf("b is non-zero\n");
        }
    }

    return 0;
}
```

Please, choose a certain language any C or C++ language. Note that, it raises your benchmark for something for optimization to become really supported by modern compilers. You'd like to check recent tests of LLVM and GCC to confirm the presence of the optimization.

Thanks,
C++ Optimization Benchmark Brainstorm Team