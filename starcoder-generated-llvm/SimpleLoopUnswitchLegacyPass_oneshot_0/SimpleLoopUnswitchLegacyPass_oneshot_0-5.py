
```cpp
#include <vector>

void loop_func(int x) {
    for (int i = 0; i < x; i++) {
        if (i != x >> 1) {
            i *= 2;
        } else {
            i /= 2;
        }
    }
    std::vector<int> vec = {0, 1, 2, 3};
    vec.push_back(4);
    vec.resize(x);
    for (int i = 0; i < (x >> 1); i++) {
        if (i == x >> 2) {
            vec.push_back(1);
        } else {
            vec.push_back(0);
        }
    }
    for (int i = 0; i < vec.size(); i++) {
        if (vec[i]) {
            i += x;
        } else {
            i -= x;
        }
    }
}

int main() {
    int x = (1 << 10);
    loop_func(x);
    return 0;
}
```

