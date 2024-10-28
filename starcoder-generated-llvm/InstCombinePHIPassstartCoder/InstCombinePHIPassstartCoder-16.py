
```cpp
#include <stdio.h>

int getNonZeroValue() {
    return 42 + 13.37; // non-zero constant combined with non-zero constants
}

int main() {
    int a = getNonZeroValue();
    int b = 0;

    for (int i = 0; i < 10; ++i) {
        if (i % 2 == 0) {
            b = a;
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

