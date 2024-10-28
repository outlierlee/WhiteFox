
```cpp
static __attribute__((fastcall)) void func(int a, int b, int c, double f) {
    if (a + b + c == 3)
        a *= 2;
    else {
        a = 2 * a;
        while (a < f)
            a *= 2;
    }
}

int main() {
    int x = 10;
    int y = 20;
    func(x, y, 15, 1.5);
    return 0;
}
```

