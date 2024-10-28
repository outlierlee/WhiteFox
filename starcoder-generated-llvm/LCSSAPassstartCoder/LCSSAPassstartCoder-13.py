
```c
#include <stdio.h>

int main() {
    int result = 0;
    int x = 15;
    int y = 4;
    int z = 8;

    if (x < y) {
        result = x + y;
    } else {
        result = y + z - x;
    }

    if (result == 4) {
        printf("Result is 4!\n");
    } else {
        printf("Result is not 4!\n");
    }

    return 0;
}
```
