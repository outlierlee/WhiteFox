
```cpp
static int func_with_ptr_args(int* arg1, float* arg2, const char* arg3) {
    int result = 0;
    if (*arg1 > 0) {
        result = *arg1 * 3;
    } else {
        result = *arg1 / 2;
    }
    if (*arg2 < 0.5) {
        result += (int)(*arg2 * 10);
    } else {
        result -= (int)(*arg2 * 10);
    }
    if (*arg3 == 'a') {
        result = result - 5;
    } else {
        result = result + 5;
    }
    return result;
}

int main() {
    int result = 0;
    int x = 10;
    float y = 1.0;
    const char* z = "a";
    int* ptr_x = &x;
    float* ptr_y = &y;
    const char* ptr_z = z;
    result = func_with_ptr_args(ptr_x, ptr_y, ptr_z);
    return result;
}
```
