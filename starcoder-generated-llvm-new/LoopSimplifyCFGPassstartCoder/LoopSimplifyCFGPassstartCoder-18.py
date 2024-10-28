
```cpp
#include<stdio.h>

int main() {
    int x = 8, i = 0;
    int y = 5;

    while (x < 20) {
        x = (x % 2) ? x + (y + 2): x - (y + 5);
        y = (i++ < 5) ? y - 1: y + 1;
    }
    return x;
}
``` 

