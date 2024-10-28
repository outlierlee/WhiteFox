
```c
#include <stdio.h>

int getNonZeroValue() {
    return 10;
}

int main() {
    int a = getNonZeroValue();
    int b = 0;

    for (int i = 0; i < 100; ++i) {
        if (i % 2 == 0) {
            b = a;
        } else {
            b = -a;
        }

        if (b == 0) {
            printf("b is zero\n");
        } else {
            printf("b is non-zero\n");
        }
    }

    return 0;
}
```
