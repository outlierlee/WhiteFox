
```cpp
#include <vector>
#include <string>

int main() {
    int x = -5;
    int y = 7;
    int z = 10;
    int result = 0;

    // define a loop
    for (int i = 0; i < 10; ++i) {
        if (i % 2 == 0) {
            result += x + y;
        } else {
            result += z;
        }
    }

    return result;
}
```

