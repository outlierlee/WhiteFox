
```cpp
int main() {
    int x = 10; // declare variable x
    int y = 20; // declare variable y
    int z = 5; // declare variable z

    // define a loop with a single latch
    while (x < y) {
        if (z < 10) {
            break; // a break statement with a condition that can be constant folded
        }
        x = x + 3; // x is updated in each iteration
    }
    return 0;
}
```

