
```c
#include <stdio.h>

int main() {
    int result = 0;
    int i, j;
    int array[10][10];

    for (i = 0; i < 10; ++i) {
        for (j = 0; j < 10; ++j) {
            array[i][j] = i + j;
        }
    }

    for (i = 0; i < 10; ++i) {
        for (j = 1; j < 10; ++j) {
            if (i > 3 && j > 7) {
                result += array[i][j];
            }
        }
    }

    return result;
}
```
