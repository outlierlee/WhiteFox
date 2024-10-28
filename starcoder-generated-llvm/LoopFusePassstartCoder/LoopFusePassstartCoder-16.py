
```cpp
#include <array>
#include <vector>
#include <algorithm>

int main() {
    std::array<int, 10> array1{}, array2{}, array3{};
    std::vector<int> vec1(10, 3), vec2(10, 7), vec3(10, 5);

    std::transform(array1.begin(), array1.end(), vec1.begin(), [](int x) {
        return x + 1;
    });

    std::transform(array2.begin(), array2.end(), vec2.begin(), [](int x) {
        return x + 2;
    });

    std::transform(array1.begin(), array1.end(), array2.begin(), array3.begin(), [](int x, int y) {
        return x + y;
    });

    std::for_each(array3.begin(), array3.end(), [](int x) {
        std::cout << x << " ";
    });

    return 0;
}
```

