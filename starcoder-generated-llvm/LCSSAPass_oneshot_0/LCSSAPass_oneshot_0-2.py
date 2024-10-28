
```cpp
#include <vector>
#include <string>

int main() {
    int x = 1;
    int y = 2;
    int z = 3;
    int result = 0;

    std::vector<int> vec = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

    for (int i = 0; i < 10; ++i) {
        if (vec[i] % 2) {
            result += x + y;
        } else {
            result += z;
        }
    }

    return result;
}
```

