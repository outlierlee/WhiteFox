
```cpp
#include <iostream>
#include <vector>
#include <string>

int main() {
    int x = (1 << 31);
    int y = x;
    while (x != y) {
        int sum = 0;
        for (int i = 0; i < x; i++) {
            sum += i;
        }
        y--;
    }
    return 0;
}
```

