
```c
#include <stdio.h>

int func1(int a, int c) {
    int result = a + c;
    return result;
}

int func2(int b, int c) {
    int result = b - 10;
    return result;
}

int main() {
    int x = 5, y = 10;
    int result1 = func1(x, y);
    int result2 = func2(x, y);
    printf("Results: %d, %d\n", result1, result2);
    return 0;
}
```

