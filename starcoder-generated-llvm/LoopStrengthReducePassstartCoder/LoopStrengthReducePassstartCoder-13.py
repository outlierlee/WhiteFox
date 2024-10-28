
```c
#include <stdio.h>

int main() {
    int sum = 0;
    int i = 0;
   
    for (;;) {
        for (;;) {
            for (;;) {
                if (i >= 10) {
                    goto L3;
                }
                sum += i;
                i++;
            }
        }
    }
L3:
    printf("Sum: %d\n", sum / 32 * 128 - 128);
    return 0;
}
```
# C Code ends