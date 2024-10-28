
```c
#include <stdio.h>

const int global_array[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

#define MAX_SIZE 10
#define OPERATOR ==

int main() {
    int result = 0;
    for (int i = 0; i < MAX_SIZE; ++i) {
        if (global_array[i] OPERATOR 5) {
            result = i;
        }
    }
    return result;
}
```

