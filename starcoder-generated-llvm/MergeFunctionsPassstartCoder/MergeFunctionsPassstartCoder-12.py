
```c
#include <stdio.h>

int func1(int x, int y, int z) {
    int result = 0;
    if(x > 10 && y == z) {
        result = x + y - z + 42;
    } else {
        result = x + y * x - z - y + x + z;
    }
    return result;
}

int func2(int x, int y, int z) {
    int result = 0;
    if(x <= 10 && y != z) {
        result = x - y + z - 42;
    } else {
        result = x - y * x + z + y - x - z;
    }
    return result;
}

int main() {
    int result = 0, x = 10, y = 20, z = 30;
    if(x > y) {
        if(y > z) {
            result = func1(x, y, z);
        }
        else {
            result = func1(y, z, x);
        }
    }
    else {
        if(y <= z) {
            result = func2(x, y, z);
        }
        else {
            result = func2(z, y, x);
        }
    }
    printf("Result: %d\n", result);
    return 0;
}
```
