
```c
#include <stdio.h>

int main() {
    int result = 0;

    int array[10][10];
    int i, j;

    for (i = 0; i < 10; ++i) {
        for (j = 0; j < 10; ++j) {
            array[i][j] = i * j;
        }
    }

    for (i = 0; i < 10; ++i) {
        for (j = 0; j < 10; ++j) {
            if (array[i][j] % 2 == 0) {
                result += array[i][j];
            }
        }
    }

    return result;
}
```
