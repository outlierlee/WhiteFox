
```cpp
#include <iostream>
#include <random>

void unused_func() {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(1, 6);
    for (int n=0; n<10; ++n)
        std::cout << dis(gen) << ' ';
}

int main() {
    int useless_variable = 15;
    int useless_variable2 = (1 << 31);
    int useless_variable3 = (1 << 32);
    int a = useless_variable;
    int b = a + 1;
    int c = b * 20;
    int d = c - b;
    if (1) {
        d = c + 5;
    }
    else {
        d = c - 5;
    }
    if (b > 100) {
        d = d + 1;
    } else {
        d = d - 1;
    }
    unused_func();
    return d;
}
```
