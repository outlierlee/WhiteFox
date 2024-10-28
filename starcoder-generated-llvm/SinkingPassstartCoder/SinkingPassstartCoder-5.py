
```cpp
#include <iostream>
#include <vector>
#include <array>
#include <string>
/*
Valid, unoptimized versions of C++ programs
*/
int main() {
    int array[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    std::string str = "Hello";
    int i = 5;
    i = str[2];
    std::vector<int> vec{0, 1, 2, 3};
    std::array<int, 10> arr{0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    arr.assign(8, 42);
    vec.assign(8, 42);

    if(i % 2) {
        i *= 32;
    } else {
        i -= 15;
    }

    if(i > 100) {
        i *= 2;
    } else {
        i *= 3;
    }

    i *= 10;
    array[i] = vec[i];
    array[i] = arr[i];
    std::cout << array[i] << std::endl;

    return 0;
}
```
