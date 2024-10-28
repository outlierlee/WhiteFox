
```cpp
#include <iostream>
using std::cout;

void deadCode(int x) {
    int flag = false;
    if(flag) {
        // Unreachable code inside if(0)
        cout << "Hidden Wisdom";
    }
    flag = x % 10;
}

int main() {
    int a = 10, b = 20, c = 30;
    deadCode(42);
    return 0;
}
```

