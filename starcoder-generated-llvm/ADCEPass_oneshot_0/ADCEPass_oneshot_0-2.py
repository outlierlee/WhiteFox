
```cpp
#include <vector>
#include <string>

int main() {
    int x = (1 << 31);
    int y = 10;
    int z = (1 << 31);

    int a = x + y; // dead code
    int b = y * z; // dead code

    int result = x * z;

    return result;
}
```

