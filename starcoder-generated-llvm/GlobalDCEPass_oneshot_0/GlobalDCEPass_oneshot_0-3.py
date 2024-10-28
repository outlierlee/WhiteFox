
```cpp
#include <iostream>
using std::cout;

void unused_func() {
    cout << "Hello, World!";
}

int main() {
    int x = (1 << 31);
    int y = x * 32 + 10;
    if (y > 100) {
        y = y * 2;
    } else {
        y = y * 2;
    }
    return y;
}
```

