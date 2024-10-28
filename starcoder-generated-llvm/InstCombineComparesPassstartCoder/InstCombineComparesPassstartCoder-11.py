
```c
#include <stdio.h>

const double global_array[] = {1.32, 1.34, 1.4, 2.5, 3.2, 4.5, 100.25, 205.4, 206.24};

int main() {
    int result = 0;

    for (int i = 0; i < 9; ++i) {
        if (global_array[i] > 10.5) {
            result = i;
            break;
        }
    }
    return result;
}
```

