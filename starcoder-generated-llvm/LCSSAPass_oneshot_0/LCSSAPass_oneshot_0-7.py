
```cpp
int main() {
    int x = 10;
    int y = 20;
    int z = 30;
    int result = 0;

    for (int i = 0; i < 10; ++i) {
        if (i > 5) {
            result += x + y;
            break;
        } else {
            result += z;
            continue;
        }
    }

    result += x + y + z;
    return result;
}
```
