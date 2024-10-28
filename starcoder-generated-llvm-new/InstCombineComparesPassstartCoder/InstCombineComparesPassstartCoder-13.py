
```c
#include <stdio.h>

const int global_array[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
const int array_size = sizeof(global_array)/sizeof(global_array[0]);

int main() {
    int result = 0;

    for (int i = 0; i < array_size; ++i) {
        if (global_array[i] != i) {
            result = i;
        }
    }

    return result;
}
```

