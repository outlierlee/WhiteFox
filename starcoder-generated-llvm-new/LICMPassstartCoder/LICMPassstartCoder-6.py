
```c
#include <stdio.h>

int main() {
    int result = -1;
    int i, j;
    int array[10][10];
    for (i = 0; i < 10; ++i) {
        for (j = 0; j < 10; ++j) {
            if ((array[i][j] + 5) % 7 == 2 * (i % 7)) {
                result += (array[i][j] * 2) % 4;
            } else {
                result -= array[i][j];
            }
        }
    }
    return result;
}
```