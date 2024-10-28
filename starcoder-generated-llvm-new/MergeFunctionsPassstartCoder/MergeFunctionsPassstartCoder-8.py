
```c
#include <stdio.h>

int func1(int a, int b) {
    int result = a / b + 10;
    return result;
}

int func2(int a, int b) {
    int result = a * b + 5;
    return result;
}

int main() {
    int result = 0;
    int a = 10;
    int b = 2;
    result = func1(a, b) + func2(a, b);
    printf("Result: %d\n", result);
    return 0;
}
```
