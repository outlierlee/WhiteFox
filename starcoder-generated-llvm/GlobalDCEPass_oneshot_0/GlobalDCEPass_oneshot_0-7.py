
```cpp
#include <string>

// define a function which is not used
void unused_func() {
    int a = 5;
    int b = 10;
    int c = a * b;
}

int main() {
    int result = 0;
    std::string str = "Hello, this is an unused function";
    char ch = str[1];
    result = ch;
    return result;
}
```
