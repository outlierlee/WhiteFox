
```cpp
int main() {
    int x = 10; // declare variable x
    int y = 12; // declare variable y
    while (x == y) {
        int a = x * y;
        int b = a * x;
        int c = b * a;
        while (c > 100)
            c--;
    }
    return 0;
}
```

