
```cpp
#include <vector>

int main() {
    std::vector<std::vector<int>> vec(10, std::vector<int>(10));
    int result = 0;

    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            vec[i][j] = i * j;
        }
    }

    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            if (vec[i][j] % 2 == 0) {
                result += vec[i][j];
            }
        }
    }

    return result;
}
```
The C++ version used std::vector to represent the 2D array.

