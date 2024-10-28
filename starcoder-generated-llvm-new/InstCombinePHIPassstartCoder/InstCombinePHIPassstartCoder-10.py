
```c
#include <stdio.h>

// Function will return 1"
int getNonZeroValue() {
    return 1;
}

int main() {
    int a = getNonZeroValue();
    int b = 0;

    for (int i = 0; i < 10; ++i) {
        if (i % 2 == 0) {
            b = a * 25; // Multiply by non-zero constant for optimization
        } else {
            b = 0; // Set the value to 0
        }

        // Comparison to check if b is zero
        if (b <= 0) {
            printf("b is zero\n");
        } else {
            printf("b is non-zero\n");
        }
    }

    return 0;
}
```

