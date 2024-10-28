
```cpp
#include <vector>
#include <string>

static int func_with_ptr_args(int* arg1, int* arg2, int* arg3) {
    int result = *arg1 + *arg2 * *arg3;
    if (*arg1 == 1) {
        result += 10;
    } else {
        result *= 2;
    }
    if (*arg1 < *arg2) {
        result = result + *arg1;
    } else {
        result = result + *arg2;
    }
    if(*arg1 < *arg3) {
        result = result + *arg1;
    } else {
        result = result + *arg3;
    }
    return result;
}

int main() {
    int x = (1 << 31);
    int y = x + 10;
    int z = y + 15;
    int* ptr_x = &x; 
    int* ptr_y = &y;
    int* ptr_z = &z;
    int result = func_with_ptr_args(ptr_x, ptr_y, ptr_z);
    return result;
}
```
