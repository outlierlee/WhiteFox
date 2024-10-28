
```c
#include <stdio.h>

int main() {
    int sum = 0;
    int i;

    for (i = 0; i < 100000; i++) {
        if (i % 64 == 0) {
            sum += i * 2;
        } else if (i % 32 == 0) {
            sum += i * 3;
        } else if (i % 16 == 0) {
            sum += i * 4;
        } else if (i % 8 == 0) {
            sum += i * 5;
        } else if (i % 4 == 0) {
            sum += i * 6;
        } else if (i % 2 == 0) {
            sum += i * 7;
        } else {
            sum += i * 8;
        }
    }

    printf("Sum: %d\n", sum);
    return 0;
}
```
