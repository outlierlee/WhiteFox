
```cpp
#include <iostream>
#include <cstdlib>
#include <time.h>

int main() {
    const int SIZE = 100;
    int array1[SIZE];
    int array2[SIZE];
    int i;

    srand (time(NULL));

    // First loop
    for (i = 0; i < SIZE; i++) {
        array1[i] = i * array1[i % (i+1)]; // Perform some operation on array1
    }

    // Second loop
    for (i = 0; i < SIZE; i++) {
        array2[i] = i * rand() % 99; // Perform some operation on array2
    }

    return 0;
}
```
