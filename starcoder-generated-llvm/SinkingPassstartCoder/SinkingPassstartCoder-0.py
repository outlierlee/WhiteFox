
```cpp
#include <iostream>

int main() {
    int a = (1 << 31); // Declare and initialize a variable (max integer value)
    int b = 30; // Declare and initialize another variable
    int c; // Declare a variable to store the result

    if (a > 5) { // Conditional block
        if (b < 10) {
            c = a * 2; // Perform an operation
        } else {
            c = a / 2; 
        }
    } else {
        if (b > 10) {
            c = a / 2; // Perform a different operation
        } else {
            c = b * b;
        }
    }

    std::cout << c << std::endl; // Use the result

    return 0;
}
```

