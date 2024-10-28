
```cpp
#include <iostream>
#include <vector>

#define CONSTANT_CONDITION 1

void loop_func(int x) {
    std::vector<int> vec(x, 0);
    for (std::vector<int>::iterator it = vec.begin(); it != vec.end(); ++it) {
        if (CONSTANT_CONDITION) {
            *it = 10;
        } else {
            *it = 20;
        }
    }
}

int main() {
    int x = (1<<10);
    loop_func(x);
    loop_func(x);
    std::cout << x << std::endl;
    return x;
}
```
