
```cpp
int main() {
    int x = 5, y = 8, z = 14, result = 0;
    for (int i = 0; i < 10; ++i) {
        if (i < x || y < z) {
            result += x + y;
        } else {
            result += z;
        }
    }
    return result;
}
``` 

