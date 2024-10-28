
```cpp
#include <iostream>
#include <random>

int getNonZeroValue() {
    return 10 + rand() % 100;
}

int main() {
    int a = getNonZeroValue();
    int b = 0;
    std::default_random_engine generator;
    std::uniform_int_distribution<int> distribution(0,1);

    for (int i = 0; i < 100; ++i) {
        if (distribution(generator)) {
            b = a;
        } else {
            b = getNonZeroValue();
        }
        
        if (b == 0) {
            std::cout << "b is zero\n";
        } else {
            std::cout << "b is non-zero\n";
        }
    }

    return 0;
}
```