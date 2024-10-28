
```c
#include <stdio.h>

int getNonZeroValue() {
    return 15;
}

int main() {
    int a = getNonZeroValue();
    int b = 0;

    for (int i = 0; i < 10; ++i) {
        if (i % 3 == 0) {
            b = a;
        } else if (i % 5 == 0){
            b = 20;
        } else {
            b = 0;
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
