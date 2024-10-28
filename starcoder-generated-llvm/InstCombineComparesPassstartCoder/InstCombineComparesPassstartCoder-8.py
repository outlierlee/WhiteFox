
```c
#include <stdio.h>

const int global_array[] = {4, 7, 8, 3, 1, 2, 9, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20};

int main() {
    int result = 0;

    for (int i = 0; i < 20; ++i) {
        if (global_array[i] > 5) {
            result = i;
        }
    }

    return result;
}
```

