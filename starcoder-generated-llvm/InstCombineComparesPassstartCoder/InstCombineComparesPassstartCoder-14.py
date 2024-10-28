
```c
#include <stdio.h>

const int global_array[15] = {98, 7, 4, 33, 56, 11, 45, 67, 3, 5, 64, 99, -2, 9, 16};

int main() {
    int result = 0;
    for (int i = 0; i < 15; ++i) {
        if (global_array[i] > 30) {
            result = i;
        }
    }
    return result;
}
```

# C Code ends