
```cpp
#include <iostream>
#include <random>

int main() {
    float a = -1000.123;
    float b = +321.987;
    float c = -9.987;
    float result;

    // Use a floating-point comparison to create a condition
    if (a > b) {
        result = a;
    } else {
        result = b;
    }

    // Use a select-like pattern with a floating-point comparison
    result = (a > b) ? a : b;

    // Print the result to ensure the code is not optimized away
    std::cout << "Result: " << result << std::endl;

    return 0;
}
```
