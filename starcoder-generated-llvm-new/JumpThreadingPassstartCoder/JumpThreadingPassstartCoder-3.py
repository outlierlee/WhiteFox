
```c
#include <stdio.h>

int simple_conditional(int a, int b) {
    if (a > 5) {
        return b / 2;
    } else {
        return b * 2;
    }
}

int main() {
    int x = 10;
    int y = 5;
    int result = 0;
    int e = simple_conditional(x % 5, y);
    if (e) {
        printf("e is nonzero\n");
    } else {
        printf("e is zero\n");
    }
    result = e;
    return result;
}
```
