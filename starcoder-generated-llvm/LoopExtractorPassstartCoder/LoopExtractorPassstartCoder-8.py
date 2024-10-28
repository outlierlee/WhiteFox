
```cpp
#include <iostream>
#include <array>
#include <vector>
#include <chrono>

// Define a function that contains a loop
void loop_function() {
    std::array<int, 1000> arr = {};
    int sum = 0; // Initialize a variable to accumulate results

    // A simple loop that iterates a fixed number of times
    for (auto& elem : arr) {
        auto start = std::chrono::high_resolution_clock::now();
        elem = start.time_since_epoch().count() % 10000;
        sum += elem; // Accumulate the sum of the loop index
    }

    // Print the result to ensure the loop is not optimized away
    std::cout << "Sum: " << sum << std::endl;
}

int main() {
    // Call the function containing the loop
    loop_function();

    return 0; // Return 0 to indicate successful execution
}
```
