
```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int*> v;

    for (int i = 0; i < 10; i++) {
        int* p = new int;
        *p = i;
        v.push_back(p);
    }

    for (int i = 0; i < 10; i++) {
        *(v[i]) = i*2;
    }

    int value = 0;
    for (int* ptr : v) {
        value += *ptr;
    }

    for (int* ptr : v) {
        delete ptr;
    }

    std::cout << "Result: " << value << std::endl;

    return value;
}
```

