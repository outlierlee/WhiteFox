
```cpp
#include <iostream>
#include <vector>
#include <string>

// Define a function with a simple conditional structure
int simple_conditional(int a, int b) {
    if (a > 50) {
        return b + 10;
    } else {
        return b - 10;
    }
}

int main() {
    std::vector<int> vec = {10, 20, 30, 40, 50};
    std::string str = "Hello";

    int y = 60;
    int result = simple_conditional(60, y);

    if (result > 40) {
        std::cout << "Result is greater than 40\n";
    } else {
        std::cout << "Result is 40 or less\n";
    }
    return result;
}
```

# C code ends
Please generate a valid C++ Code (as C Code in the description) which meet the requirements mentioned in the description and also please check that you can compare or check the optimization result after optimization.