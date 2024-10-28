
```c
#include <stdio.h>

int main() {
    int result = 0;
    int i, j;
    int array[10][10];

    for (i = 0; i < 10; ++i) {
        for (j = 0; j < 10; ++j) {
            array[i][j] = (i * j) % (1 << 2) + (1 << 1);
        }
    }

    for (i = 0; i < 10; ++i) {
        for (j = 0; j < 10; ++j) {
            if (array[i][j] == 0x00) {
                result += array[i][j] << 2;
            } else {
                result += array[i][j] >> 2;
            }
        }
    }

    return result;
}
```

This function uses a variable value as condition in the if statement. It initializes and uses the array elements with bitwise operations. The result generation function also involves some bitwise operations.

