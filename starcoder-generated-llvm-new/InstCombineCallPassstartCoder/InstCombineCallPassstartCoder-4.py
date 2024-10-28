
```cpp
#include <string>
#include <iostream>

const char* global_const = "Hello, World!";

void example_function(char* dest) {
    std::memmove(dest, global_const, sizeof(global_const));
}

int main() {
    auto buffer = new char[sizeof(global_const)];
    example_function(buffer);
    std::cout << buffer;
    delete[] buffer;
    return 0;
}
```

