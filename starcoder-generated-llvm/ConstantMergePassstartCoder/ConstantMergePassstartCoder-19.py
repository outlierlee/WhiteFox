
```cpp
#include <cstddef>
#include <iostream>

// Define global variables with initial values
static const int global_const1 = 42;
static const int global_const2 = 42;

// Define a function that uses these global constants
int use_globals() {
    return global_const1 + global_const2;
}

int main() {
    int result = use_globals();
    std::cout << "Result: " << result << std::endl;
    return 0;
}
```
# Code ends