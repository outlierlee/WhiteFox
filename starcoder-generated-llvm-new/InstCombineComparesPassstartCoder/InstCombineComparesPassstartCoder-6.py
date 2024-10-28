
```c
#include <stdio.h>

const int global_array[] = {2, 4, 6, 8, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160};

int main() {
    int result = 0;
    for (int i = 0; i < sizeof(global_array)/sizeof(int); ++i) {
        if (global_array[i] < 50) {
            result = i;
        }
        printf("%d,", global_array[i]);
    }
    return result;
}
```
