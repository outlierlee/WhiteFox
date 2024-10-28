
```c
#include <stdio.h>

int func1(int a, int b) {
    int result = a;
    if(b > 10) {
        result = a * 2;
    } else {
        result = a + 1;
    }
    if(a < 50) {
        result *= 3;
    } else {
        result *= 2;
    }
    if(b > (a << 3)) {
        result = (a + b) * 2;
    } else {
        result = a - b;
    }
    return result;
}

int func2(int a, int b) {
    int result = a * 2;
    if(b < 50) {
        result = a - 1;
    } else {
        result = a * 3;
    }
    if(a > 50) {
        result *= 2;
    } else {
        result = a + b;
    }
    return result;
}

int main() {
    int x = 100, y = 20;
    int result1 = func1(x, y);
    int result2 = func2(x, y);
    printf("Results: %d, %d\n", result1, result2);
    return 0;
}
```

