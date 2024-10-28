
```cpp
#include <iostream>
#include <vector>
#include <string>

void loop_with_condition(int n, int condition) {
    bool flag = condition == 1;

    for (int i = 0; i < n; ++i) {
        if (flag) {
            printf("Flag is true, iteration %d\n", i);
        } else {
            printf("Flag is false, iteration %d\n", i);
        }
    }
}

int main() {
    int n = 10;
    int condition = 1;

    loop_with_condition(n, condition);

    return 0;
}
```
