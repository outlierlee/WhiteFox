
```cpp
#include <iostream>
#include <vector>
#include <string>

int main() {
    int x = (1 << 7) + (1 << 6);
    int y = (1 << 5);
    int z = (1 << 4);

    while (x > y) {
        y += 2;
        if (z % 2 != 0) {
            break;
        }
    }
    return x;
}
```
