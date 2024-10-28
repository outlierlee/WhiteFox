
```c
#include <stdio.h>

int main() {
    int a[10] = {3, 4, 5, 6, 7, 8, 9, 10}; // Initialize an array
    int b; // Store the result

    for (int i = 0; i < 10; ++i) {
        if (i < 5) {
            b = a[i] * 2;
        } else {
            b = a[i] * 3;
        }

        printf("%d ", b); // Use the result
    }

    return 0;
}
```
