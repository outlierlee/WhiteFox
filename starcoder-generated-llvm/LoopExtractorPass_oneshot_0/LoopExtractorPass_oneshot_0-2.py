
```cpp
#include <iostream>
#include <random>

int main() {
    int x = rand();
    int y = 0;
    int z = 0;
    bool cond = (x % 2 == 0);
    int i = 0;
    while (i < x) {
        if (cond) {
            y += 1;
            z += i;
        }  
        ++i;
    }
    return y;
}
```

