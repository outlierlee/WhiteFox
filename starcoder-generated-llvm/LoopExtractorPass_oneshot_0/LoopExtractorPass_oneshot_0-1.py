
```cpp
int main() {
    int x = 10;
    int y = 5, z = 2;

    for (int i = 0; i < x; ++i) {
        y = y + z;
        z = z + i;
    }

    return y;
}
```
