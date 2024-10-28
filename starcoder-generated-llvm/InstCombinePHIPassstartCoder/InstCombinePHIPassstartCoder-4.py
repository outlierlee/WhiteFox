
```c
#include <stdio.h>

int getNonZeroValue() {
    return 1;
}

int main() {
    int a = getNonZeroValue();
    int b = 0;

    for (int i = 0; i < 10; ++i) {
        if (i % 2 == 0) {
            b = a;
        } else {
            b = -i;
        }

        if (b == 0) {
            printf("b is zero\n");
        } else if (b == 1) {
            printf("b is non-zero but optimized away\n");
        }else {
            printf("b is non-zero %d\n", b);
        }
    }

    return 0;
}
```

