
```c
#include <stdio.h>

const int global_array[] = {3, 5, 7, 9, 11, 13, 15, 17, 19, 21};
 
int main() {
    int result = 0;

    for (int i = 0; i < sizeof(global_array) / sizeof(global_array[0]); ++i) {
        if (global_array[i] >= 10 && global_array[i] <= 20) {
            result = i;
        }
    }

    return result;
}
```
