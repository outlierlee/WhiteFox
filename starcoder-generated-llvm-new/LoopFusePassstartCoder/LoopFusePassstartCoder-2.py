
```cpp
#include <iostream>
#include <random>

int main() {
    int size = 10000;
    std::default_random_engine generator;
    std::uniform_int_distribution<int> distribution(1,100);
    int* array1 = new int[size];
    int* array2 = new int[size];
    int* array3 = new int[size];

    // Initialize arrays
    for (int i = 0; i < size; i++) {
        array1[i] = distribution(generator);
        array2[i] = distribution(generator);
    }

    // Fusion of loops
    for (int j = 0; j < size; j++) {
        array1[j] += 1;
        array2[j] += 2;
        array3[j] = array1[j] + array2[j];
    }

    // Print the results
    for (int k = 0; k < size; k++) {
        std::cout << array3[k] << " ";
    }

    delete[] array1;
    delete[] array2;
    delete[] array3;

    return 0;
}
```

This code takes advantage of loop fusion, which aims to increase efficiency by eliminating redundant computation in programs. It does this by transforming sequences of irregular instructions into more efficient sequences of regular instructions. To accomplish this, the loops must have independent loop control flow and identical data dependency patterns. The arrays `array1`, `array2`, and `array3` are initialized in separate loops, but on the third loop, all results are written into the third array, simple yet effective loop fusion allows the compiler to perform loop fusion after the loop merge optimization.