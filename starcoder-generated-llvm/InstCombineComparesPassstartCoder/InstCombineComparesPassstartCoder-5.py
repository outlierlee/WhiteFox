
```c
#include <stdio.h>

const int global_array[] = {1, 3, 5, 7, 9};
const int ARRAY_SIZE = sizeof(global_array) / sizeof(global_array[0]);

#define MAX_ARRAY_SIZE_FOR_COMBINE 10

int main() {
    int result = 0;
    
    for (int i = 0; i < ARRAY_SIZE; ++i) {
        if (global_array[i] >= 2 && global_array[i] <= 5) {
            result = i + 1;
        }
    }
    printf("%d", result);
    return result;
}
```
