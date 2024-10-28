
```cpp
#include <vector>
#include <string>

void loop_func(int x) {
    int sum = 0;
    for (int i = 0; i < x; ++i) {
        if (i % 2) {
            sum += i;
        } else {
            sum -= i;
        }
    }
}

int main() {
    int a = (1 << 11);
    loop_func(a);
    return 0;
}
```

