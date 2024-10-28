
```cpp
#include <iostream>
#include <vector>

void loop_with_condition(int n, bool flag) {
    for (int i = 0; i < n; ++i) {
        if (flag) {
            std::cout << "Flag is true, iteration " << i << std::endl;
        } else {
            std::cout << "Flag is false, iteration " << i << std::endl;
        }
    }
}

int main() {
    int n = 10;
    bool flag = true;

    loop_with_condition(n, flag);

    return 0;
}
```

