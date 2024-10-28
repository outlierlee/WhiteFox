
```cpp
#include <iostream>
#include <vector>

// Define a function that contains a basic block structure
void example_function() {
    int result = 0;
    for (int i = 1; i <= 100; i++) {
        if (i % 2) {
            result += i; // Increment the result by the value of i
        } else {
            result -= i; // Decrement the result by the value of i
        }
    }
    // Use the variable to prevent dead code elimination
    std::cout << result << std::endl;
}

int main() {
    example_function(); // Call the function
    return 0;
}
```
