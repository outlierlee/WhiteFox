
```c
#include <stdio.h>

int varargs_func(int a) {
    for (int i = 0; i < a; i++) {
        a = a + i;
    }
    for (int i = 0; i < a; i++) {
        a = a + i;
    }
    return a;
}

int main() {
    int result = -1;
    int x = 10;
    int y = 5;
    
    if (x > y) {
        result = 1;
    } else if (y > x) {
        result = -1;
    } else {
        result = 0;
    }
    int b = varargs_func(100);
    printf("%d, %d\n", result, b);
    return result;
}
```

