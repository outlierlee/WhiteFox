
```cpp
#include <iostream>
#include <vector>
#include <string>

int main() {
    int x = (1 << 7) + (1 << 6);
    int y = (1 << 5) + (1 << 4);
    int z = 111 + 222;
    int *p = new int;
    *p = x + y + z;
    int result = *p;
    delete p;
    return result;
}
```

