
```c
#include <stdio.h>

const int global_array[] = {10, 20, 30, 40, 50, 60, 70};

int main() {
    int result = 0;
    for (int i = 0; i < sizeof(global_array) / sizeof(global_array[0]); ++i) {
        if (global_array[i] > 30) {
            result = i;
        }
    }
    printf("%d\n", result);
    return result;
}
```
