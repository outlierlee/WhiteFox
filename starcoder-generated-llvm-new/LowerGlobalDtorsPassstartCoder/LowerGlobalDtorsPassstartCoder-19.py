
```cpp
#include <cstddef>
#include <iostream>

// Define a destructor function
void __attribute__((destructor)) my_destructor() {
    // RANDOM_CODE: Any code that does not affect the global destructors
    std::cout << "Destructor called" << std::endl;
}

// Define another destructor function with a different priority
void __attribute__((destructor(101))) another_destructor() {
    // RANDOM_CODE: Any code that does not affect the global destructors
    std::cout << "Another destructor called" << std::endl;
}

int main() {
    // RANDOM_CODE: Any code that does not affect the global destructors
    std::cout << "Main function" << std::endl;
    return 0;
}
```

