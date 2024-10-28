
```c
#include <stdio.h>

// Define a global constant array
const int global_array[] = {1,2,3,4,5};
#define ARRAY_SIZE sizeof(global_array)/sizeof(global_array[0])

int main() {
    // Declare a variable to store the result
    int result = 0;

    // Use a loop or direct access to index into the global array
    for (int i = 0; i < ARRAY_SIZE; ++i) {
        // Perform a comparison operation with a constant
        if (global_array[i] > 3) {
            // Update the result based on the comparison
            result = i;
        }
    }

    // Return the result
    return result;
}
```
