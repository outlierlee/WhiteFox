
```cpp
#include <vector>
#include <string>

int main() {
    int x = 4;
    int y = 7;
    int z = 3;

    for (int i = 0; i < x; ++i) {
        y = y + z;
        z = z + i;
    }

    return y;
}
```

In the generated code, the `x` is statically determined loop condition. At compilation time, the compiler can check if this loop can be statically determined, and if it can, directly calculate it at compile time. In the generated code, `x` = 4 and the loop can be statically determined, so the loop can be represented as plain C++ code with constant iterations and no extra overheads, no branch checks, no variable dependencies, and no runtime pitfalls.

