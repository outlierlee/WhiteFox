
```cpp
#include <vector>
#include <string>

void __attribute__((noinline)) func(int arg1, void* arg2, std::vector<int> arg3, char const* arg4, double arg5, int* arg6){
    arg1 = 10;
    arg5 = 20.0;

    arg2 = arg6;

    if (arg3[0] < 5) {
        arg1 = arg1 + 10;
    }
    else {
        arg1 = arg1 - 10;
    }
    if (*arg6 > 10) {
        arg5 = arg5 * 2.0;
    } else {
        arg5 = arg5 / 2.0;
    }
    if (arg2 != NULL) {
        *(int*)(arg2) = arg1;
    }
}

int main() {
    int x = 1;
    void* y = &x;
    std::vector<int> z = {1, 2, 3, 4};
    std::string w = "character";
    int* v = new int;

    *v = 123;

    func(x, y, z, &(w[2]), w[0], v);

    delete v;
    return 0;
}
```

