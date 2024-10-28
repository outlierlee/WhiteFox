
```c
#include <stdio.h>

const int global_array[] = {123, 456, 789}; 

int main() {
    int result = 0;

    for (int i = 0; i < 3; ++i) {
        if (global_array[i] == 456) {
            result = i;
        }
    }

    return result;
}
```

