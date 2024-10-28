
```cpp
#include <vector>
#include <string>

void loop_func(int x) {
    for (int i = 0; i < x; ++i) {
        if (i % 2) {
            i = i * 32 + 15;
        } else {
            i = i - 15;
        }
    }
}

int main() {
    int a = (1 << 31);
    std::vector<int> vec = {0, 1, 2, 3};
    std::string str = "hello";
    vec.assign(5, 42);
    loop_func(a);
    return 0;
}
```
