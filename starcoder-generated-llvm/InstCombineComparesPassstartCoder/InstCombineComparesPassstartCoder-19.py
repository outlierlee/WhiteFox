
```cpp
#include <cstddef>
#include <iostream>

// Define a global constant array
const int global_array[] = {0, 5, 10, 15, 20, 25, 30, 35, 40, 45};
const size_t ARRAY_SIZE = sizeof(global_array) / sizeof(global_array[0]);

int main() {
    // Declare a variable to store the result
    int result = 0;

    // Use a loop or direct access to index into the global array
    for (size_t i = 0; i < ARRAY_SIZE; ++i) {
        // Perform a comparison operation with a constant
        if (global_array[i] < 20) {
            // Update the result based on the comparison
            result += static_cast<int>(i) * 2;
        }
    }

    // Return the result
    return result;
}
```
