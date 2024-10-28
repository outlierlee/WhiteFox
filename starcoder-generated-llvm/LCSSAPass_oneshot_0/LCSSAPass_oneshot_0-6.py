
```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> vec_i = {7, 5, 8};
    int i = vec_i[0];
    int x = 3;
    int y = 5;
    int z = 10;
    int result = 0;

    for (int j = 0; j < 10; ++j) {
        if (j < i) {
            result += x;
        } else if (j > i && j > x) {
            result += y;
        } else {
            result += z;
        }
    }
    return result;
}
```

