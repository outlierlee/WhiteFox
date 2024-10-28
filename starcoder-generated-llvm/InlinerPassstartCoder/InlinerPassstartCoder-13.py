
```c
#include <stdio.h>

static inline long long int simple_function(long long int a, long long int b, int c) {
    long long int result = 0;
    result = a;
    for (int i = 0; i < b; i++)
    {
        result += c;
        if (i % 2)
            result -= 1;
    }
    return result;
}

int main() {
    long long int x = -100000000000;
    long long int y = 100000;
    int z = 1;
    long long int result = simple_function(x, y, z);
    return 0;
}
```
