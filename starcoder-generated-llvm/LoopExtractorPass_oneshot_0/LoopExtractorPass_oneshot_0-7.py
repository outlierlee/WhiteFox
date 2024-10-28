
```cpp
int main() {
    const int size = 100;
    int x = 1;
    int y = 0;
    int z = 0;

    for (int i = 0; i < size; ++i) {
        y += z;
        z += i;
    }

    return y;
}
```
