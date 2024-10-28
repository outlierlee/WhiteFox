
```cpp
#include <iostream>
#include <random>

int main() {
    int size = rand(); // just an arbitrary number
    int *arr = new int[size];
    for (int i = 0; i < size/2; ++i) {
        arr[i] = i;
    }
    for (int i = size/2; i < size; ++i) {
        arr[i] = size-i;
    }
    delete[] arr;
    return 0;
}
```

