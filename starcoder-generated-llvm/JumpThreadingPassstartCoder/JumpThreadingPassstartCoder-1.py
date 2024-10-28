
```cpp
#include <iostream>

// Define a function with a simple conditional structure
int simple_conditional(int a, int b) {
    if (a > 0) {
        return b * 5;
    } else {
        return b;
    }
}

int main() {
    int x = 5; // Initialize variable x
    int y = 10; // Initialize variable y
    int multiplier1 = 42;

    // Call the function with a constant condition
    int result = simple_conditional(1, y * multiplier1);

    // Use the result in a conditional branch
    if (result > 4200) {
        std::cout << "Result is greater than 4200" << std::endl;
    } else {
        std::cout << "Result is 4200 or less" << std::endl;
    }

    return 0;
}
```
