
```cpp
#include <iostream>
#include <vector>
#include <string>

int main() {
    int x = 0, y = 1;

    if (x < y) {
        std::cout << "Unreachable block\n";
    } else {
        std::cout << "Reachable block\n";
    }

    while (x < y) {
        std::cout << "Unreachable loop block\n";
    }

    if (x > y) {
        std::vector<int> vec = {0,1,2,3};
        std::string str ="hello";
        vec.assign(5, 42);
        int b = 1;
        b += vec[1] + 1.0;

        if (y) {
            std::cout << b;
        } else {
            std::cout << str[3];
        }
    }
    
    return 0;
}
```
