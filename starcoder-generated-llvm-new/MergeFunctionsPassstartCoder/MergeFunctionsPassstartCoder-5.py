
```c
#include <stdio.h>

int func1(int a, int b) {
    int result = a + b;
    return result;
}

int func2(int a, int b) {
    int result = a + b;
    return result;
}

int main() {
    int x = 5;
    int y = func1(x, x) + func1(x, x);
    int result1 = func1(x, y);
    int result2 = func2(x, y);
    printf("Result: %d, %d\n", result1, result2);
    return 0;
}
```
