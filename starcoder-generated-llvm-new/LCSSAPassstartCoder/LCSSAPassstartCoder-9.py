
```c
#include <stdio.h>

int main() {
    int result = 0;

    int a = -10;
    int b = 20;
    int c = 30;

    for (int i = 0; i < 30; i++) {
        if ((a + i) % 5 == 0) {
            result += (a + i) * 5;
        } else {
            result += (b + i);
        }
    }

    if (result < c) {
        printf("Result is less than c\n");
    } else {
        printf("Result is greater than or equal to c\n");
    }

    return result;
}
```
