
```cpp
#include <iostream>

// Define a function that returns a non-zero integer value
int getNonZeroValue() {
    return 1; // or any other non-zero constant
}

using int_p = int*;

int main() {
    int a = getNonZeroValue(); // Call the function to get a non-zero value
    int b = 0; // Initialize a variable to zero

    int_p ptr = &b;

    // Use a loop or conditional structure to create a PHI node scenario
    for(int i = 0; i < 10; ++i) {
        if (i % 2 == 0) {
            *ptr = a; // Assign the non-zero value to b
        } else {
            *ptr = 0; // Assign zero to b
        }

        // Compare the variable with zero
        if (b == 0) {
            std::cout << "b is zero" << std::endl;
        } else {
            std::cout << "b is non-zero" << std::endl;
        }
    }

    return 0;
}
```

