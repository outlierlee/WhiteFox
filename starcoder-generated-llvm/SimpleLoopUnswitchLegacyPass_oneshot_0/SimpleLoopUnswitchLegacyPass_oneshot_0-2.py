
```cpp
#include <vector>
#include <string>

void loop_func(int x) {
    std::vector<int> vec;
    int i = 0;
    do {
        vec.push_back(i);
        i += 2;
    } while (i < x);
}

int main() {
    int x = vec.size();
    loop_func(vec.size());
    return 0;
}
```

