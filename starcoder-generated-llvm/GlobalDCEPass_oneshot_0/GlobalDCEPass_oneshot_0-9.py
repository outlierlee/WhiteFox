
```cpp
#include <vector>
#include <string>

void unused_func() {
    int i = 10;
    i += 10;
    i += -10;
    double d = i;
    std::vector<int> vec(5,i);
    vec.assign(5, 4);
    std::string str = "Hello";
    str.append("World");
}

int main() {
    int result = 0;
    int a = (1 << 31);
    std::vector<int> vec = {0, 1, 2, 3};
    std::string str = "hello";
    vec.assign(5, 42);
    int varargs_func(int x, ...);
    int b = varargs_func(a, 18, 25, vec[1], vec, str[3]);
    result = b * 2;
    unused_func();
    return result;
}
```
