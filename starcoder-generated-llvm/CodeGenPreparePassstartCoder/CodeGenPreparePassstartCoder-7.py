
```cpp
#include <stdio.h>

int func(int x) {
    int res = 0;
    if (x == 101) {
        res = -x % 13;
    } else {
        res = x * 57 % x;
    }
    if (x == 21) {
        res = x * 2;
    } else {
        res = x + 3;
    }
    return res;
}

int main() {
    int res = 0;
    int x = 101;
    res = func(x);
    printf("%d\n", res);
    return res;
}
```
