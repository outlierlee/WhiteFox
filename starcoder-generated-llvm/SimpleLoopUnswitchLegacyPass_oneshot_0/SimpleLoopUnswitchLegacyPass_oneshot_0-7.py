
```cpp
#include <chrono>

void loop_func(int x) {
    x *= 100;
    for (int i = 0; i < x; ++i) {
        if (i % 2 == 0) {
            // Do something here
        } else {
            // Do something else here
        }
    }
}

int main() {
    auto start = std::chrono::system_clock::now();
    loop_func(100);
    auto end = std::chrono::system_clock::now();
    std::chrono::duration<double> elapsed_seconds = end-start;
    return 0;
}
```

