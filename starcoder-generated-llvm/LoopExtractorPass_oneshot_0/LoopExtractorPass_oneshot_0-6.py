
```cpp
#include <iostream>
#include <vector>
#include <string>

int main() {
    int x = 10;
    int y = 15;
    int z = 20;

    for (int i = 0; i < x; ++i) {
        y = y + z;
        z = z + i;
    }

    return y;
}
```

