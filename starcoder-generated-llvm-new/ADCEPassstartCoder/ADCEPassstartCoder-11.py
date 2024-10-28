
```cpp
#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>

int compute(int x, int y) {
    int result = x + y;
    return result;
}

int main() {
    int main_result = 0;
    int a = (1 << 31);
    int b = a;
    int c = a + b;
    std::vector<int> vec(10);
    std::srand(std::time(nullptr));
    c = 0;
    vec[2] = a;
    vec.assign(10, vec[2]);
    vec[5] = vec.size();
    main_result = compute(vec[2], vec[5]);
    if(vec[2] > vec[5]) {
        main_result += a * b;
    } else {
        main_result -= a * b;
    }
    
    std::cout << "Result: " << main_result << std::endl;

    return main_result;
}
```
