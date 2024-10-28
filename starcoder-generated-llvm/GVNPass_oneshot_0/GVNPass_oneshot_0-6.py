
```cpp
#include <iostream>
#include <vector>
#include <string>

int main() {
    int x = (1 << 7) + (1 << 6);
    int y = (1 << 5) + (1 << 4);
    int z = 0;

    if (x + y > 0) {
        z = x + y;
    } else {
        z = x - y;
    }

    return z;
}
```
