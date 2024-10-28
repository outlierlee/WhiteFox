
```cpp
int main(){
    int x = 20; // declare variable x
    int y = 10; // declare variable y
    int z = 15; // declare variable z

    // define a loop with a single latch
    while (x * 2 > y) {
        int temp = x - y;
        x = temp + 1; // x is updated in each iteration
        if (z > x / y) {
            break; // a break statement with a condition that can be constant folded
        }
    }
    return x;
}
```

