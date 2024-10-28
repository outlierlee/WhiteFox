
```cpp
int main() {
    int x = 10;
    int y = 20;
    int z = 30;
    int result = 0;

    for (int i = 0; i < 5; ++i) {
        if (i < x) {
            result += x + y;
        } else {
            result += z;
        }
    }

    return result;
}
```

