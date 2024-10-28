
```c
#include <stdio.h>

int main() {
    int result = 0;
    int array[10][10];
    int i;

    // Initialize the array
    for (i = 0; i < 10; ++i) {
        array[0][i] = i * (i - 1);
        array[1][i] = i * (i - 1);
        array[2][i] = i * (i - 1);
        array[3][i] = i * (i - 1);
        array[4][i] = i * (i - 1);
        array[5][i] = i * (i - 1);
        array[6][i] = i * (i - 1);
        array[7][i] = i * (i - 1);
        array[8][i] = i * (i - 1);
        array[9][i] = i * (i - 1);
    }

    // Compute
    for (i = 0; i < 10; ++i) {
        if (array[1][i] % 2 == 0) {
            result += array[1][i];
        }
        if (array[2][i] % 2 == 0) {
            result += array[2][i];
        }
        if (array[3][i] % 2 == 0) {
            result += array[3][i];
        }
        if (array[4][i] % 2 == 0) {
            result += array[4][i];
        }
        if (array[5][i] % 2 == 0) {
            result += array[5][i];
        }
        if (array[6][i] % 2 == 0) {
            result += array[6][i];
        }
        if (array[7][i] % 2 == 0) {
            result += array[7][i];
        }
        if (array[8][i] % 2 == 0) {
            result += array[8][i];
        }
        if (array[9][i] % 2 == 0) {
            result += array[9][i];
        }
    }

    return result;
}
```
