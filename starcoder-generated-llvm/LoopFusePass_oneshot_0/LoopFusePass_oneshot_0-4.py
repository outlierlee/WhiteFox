
```cpp
#include <array>

int main() {
    std::array<int, 10> array1 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    std::array<int, 10> array2 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    int i = 0;

    for (i = 0; i < 10; i++) {
        array1[i] = (2*i)%10;
    }

    for (i = 0; i < 10; i++) {
        array2[i] = (3*i)%10;
    }

    return 0;
}
```

