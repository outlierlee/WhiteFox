
```cpp
#include <cstring>
#include <iostream>

const char* global_const = "Hello, World!";

void example_function(char* dest) {
    std::strncpy(dest, global_const, sizeof(global_const));
    // strncpy can actually use memcpy due to string minimum alignment requirement
}

int main() {
    char buffer[50]; 
    example_function(buffer);
    std::cout << buffer << std::endl;
    return 0;
}
```

