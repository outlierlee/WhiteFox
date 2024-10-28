
```cpp
#include <iostream>
#include <vector>

int getNonZeroValue() {
    return 42;
}

int main() {
    int a = getNonZeroValue();
    int b = 0;

    for (int i = 0; i < 10; ++i) {
        if (i % 2 == 0) {
            b = a;
        } else {
            b = 0;
        }

        if (b == 0) {
            std::cout << "b is zero" << std::endl;
        } else {
            std::cout << "b is non-zero" << std::endl;
        }
    }

    return 0;
}
```
