
```cpp
#include <cstring>

const char* global_const = "Hello, World!";

void example_function(char* dest) {
    std::memmove(dest, global_const, sizeof(global_const));
    std::memmove(dest, global_const, sizeof(global_const));
    std::memmove(dest, global_const, sizeof(global_const));
    std::memmove(dest, global_const, sizeof(global_const));
    std::memmove(dest, global_const, sizeof(global_const));
    std::memmove(dest, global_const, sizeof(global_const));
}

int main() {
    char buffer[50];
    example_function(buffer);
    return 0;
}
```

