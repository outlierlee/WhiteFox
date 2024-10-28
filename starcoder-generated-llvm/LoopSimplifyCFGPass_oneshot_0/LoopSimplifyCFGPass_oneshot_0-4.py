
```cpp
int main() {
    int x = 50; // declare and initialize variable x to 50
    int y = 30; // declare and initialize variable y to 30
    int z = 20; // declare and initialize variable z to 20

    // define a loop with a single latch
    while (x > y) {
        // in this example, let us just multiply x with 3 so that on the 10th loop, x > y
        // i.e., after this loop, x == 500
        x = x * 3;
        if (z < 25) {
            break; // breaks when z < 25
        }
    }
    return 0;
}
```
