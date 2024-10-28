
```cpp
#include <iostream>
#include <random>

int main() {
    int array1[5000]; 
    int array2[5000];

    std::default_random_engine generator;
    std::uniform_int_distribution<int> distribution(1,1000);

    for (int i = 0; i < 5000; i++) {
        array1[i] = distribution(generator);
        array2[i] = distribution(generator);
    }
    return 0;
}
```
