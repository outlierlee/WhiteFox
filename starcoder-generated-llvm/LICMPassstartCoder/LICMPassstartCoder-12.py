```c
#include <stdio.h>

int main() {
    int result = 0;
    int i, j;
    int array[10][10];

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

    for (i = 0; i < 10; ++i) {
        for (j = 0; j < 10; ++j) {
            printf("array[%d][%d] = %d\n", i, j, array[i][j]);
        }
    }
    return result;
}
```

