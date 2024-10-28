
```cpp
int __attribute__((fastcall)) g(int a, int b, int c, int d) {
    return a + b + c + d;
}

int __attribute__((stdcall)) h(int a, int b, int c, int d) {
    return g(a, b, c, d);
}

int __attribute__((cdecl)) k(int a, int b, int c, int d) {
    return h(a, b, c, d);
}

int main() {
    int result = 0;
    result = k(1, 2, 3, 4);
    return result;
}
```

