
```c
#include <stdio.h>

const int global_array[] = {0, 1, 4, 9, 16, 25, 36, 49}; // size 8, less than MaxArraySizeForCombine

int main() {
    int result = 0;
    for (int i = 0; i < 8; ++i) {
        if (global_array[i] == i*i) {
            result = i;
        }
    }
    return result;
}
```

