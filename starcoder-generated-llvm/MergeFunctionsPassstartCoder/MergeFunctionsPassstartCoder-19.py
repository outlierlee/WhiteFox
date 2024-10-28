
```cpp
#include <cstddef>
#include <iostream>

// Define two functions with identical bodies
int func1(int a, int b) {
    int result = a + b; // Perform some operation
    return result; // Return the result
}

int func2(int a, int b) [[gnu::hot]] {
    int result = a + b; // Perform the same operation as func1
    return result;     // Return the result
}

int main() {
    int x = 5, y = 10; // Declare and initialize variables
    int result1 = func1(x, y); // Call the first function
    int result2 = func2(x, y); // Call the second function
    std::cout << "Results: " << result1 << ", " << result2 << std::endl; // Print the results
    return 0; // Return from main
}
```
