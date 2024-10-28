
```cpp
#include <iostream>
#include <vector>
#include <string>

int main() {
    int result = 0;

    int a = 1 << 31;
    int b = 1 << 10;
    int c = 3;
    std::vector<int> vec = {1, 2, 3};
    std::string str = "hello";

    for (int i = 0; i < b; ++i) {
        result += vec[i];
    }

    if (result > str[2]) {
        printf("Result is greater\n");
    } else {
        printf("Result is less\n");
    }

    return result;
}
```

