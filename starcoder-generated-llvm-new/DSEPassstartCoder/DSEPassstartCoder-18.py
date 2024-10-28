
```cpp
#include<iostream>
using namespace std;

void FillWithValue(int *array, int size, int value) {
    for(int i = 0; i < size; i++) {
        array[i] = value;
    }
}

int main() {
    const int SIZE = 100;
    int* buffer = new int[SIZE];
    if(buffer == NULL) return -1;

    FillWithValue(buffer, SIZE, 0);
    FillWithValue(buffer, SIZE, 1);

    delete[] buffer;

    return 0;
}
```

