
```c
#include <stdio.h>

int func1(int a, int b) {
    int result = a * b;
    a = 2 * b;
    return result;
}

int func2(int a, int b) {
    int result = a * b;
    a = 2 * b;
    return result;
}

int main() {
    int x = 3, y = 4;
    int result1 = func1(x, y);
    int result2 = func2(x, y);
    printf("Results: %d, %d\n", result1, result2);
    return 0;
}
```
