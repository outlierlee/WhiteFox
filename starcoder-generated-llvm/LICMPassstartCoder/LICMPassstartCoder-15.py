
```c
#include <stdio.h>

int main() {
    int result[10] = {324,365,364,365,324,364,365,324,364,8};
    int array[10] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1};
    int i, j;

    int temp[4];
    temp[0] = array[4] + array[2];
    temp[1] = array[8] - array[6];
    temp[2] = array[8] - array[1];
    temp[3] = array[8] * result[8];

    return array[4] * array[8] * temp[0];
}
```
