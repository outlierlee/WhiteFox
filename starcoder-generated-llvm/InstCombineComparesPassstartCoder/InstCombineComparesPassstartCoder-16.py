
```c
#include <stdio.h>

const int global_array[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

int main() {
    int result = 0;
    for (int i = 0; i < 10; ++i) {
        if (global_array[i] != 1) {
            result = i;
        }
    }
    return result;
}
```
# C Code ends