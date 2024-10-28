
```cpp
int main() {
    int x = 10; // declare variable x
    int y = 20; // declare variable y
    int z = 30; // declare variable z

    while (x < y) {
        x = x - z; // Do something with x, y, z
        if (z >= 100) {
            break; // a break statement with a condition that can be constant folded
        }
    }
    return 0; // this return value should relate to the optimization
}
```

