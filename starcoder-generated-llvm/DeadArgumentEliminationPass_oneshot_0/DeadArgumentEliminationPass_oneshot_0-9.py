
```cpp
static int varargs_func(int x, ...) {
    int result = x + 1;
    if (x > 100) {
        result = result * 2;
    } else {
        result = result + 20;
    }
    if ((result & 3) == 1) {
        result = result + 1;
    } else if ((result & 3) == 2) {
        result = result * 2;
    } else if ((result & 3) == 3) {
        result = result + 3;
    }
    return result;
}

int main() {
    int result = 0;
    int x = (1 << 31);
    int a[5] = {0, 1, 2, 3, 4};
    result = varargs_func(x, a[1], ((int *) a)[2], x+1, false);
    return result;
}
```

