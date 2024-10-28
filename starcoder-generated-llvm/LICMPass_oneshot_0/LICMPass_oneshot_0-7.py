
```cpp
#include <vector>
#include <string>

int no_side_effect_func(int x) {
    int result = x % 37;
    return result;
}

int main() {
    int result = 0;
    std::vector<int> vec = {0, 1, 2, 3};
    std::string str = "hello";

    for (int i = 0; i < 10; ++i) {
        int x = vec[i] + 2 * str[i];
        int b = no_side_effect_func(x);
        if (b) {
            result += b;
        }
    }

    return result;
}
```
