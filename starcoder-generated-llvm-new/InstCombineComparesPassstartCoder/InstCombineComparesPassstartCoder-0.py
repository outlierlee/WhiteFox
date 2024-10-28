
```c
#include <stdio.h>

const char string_literal[] = "some fixed-size string literal";
const int global_array[] = {'a', 'b', 'c', 'd', 'e'};

int main() {
    int result = -1;
    for (int i = 0; i < ARRAY_SIZE; ++i) {
        if (global_array[i] != 'c') {
            result = i;
        }
    }
    return result;
}
```
