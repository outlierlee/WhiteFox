
```cpp
int main() {
    int x = (1 << 31); // Declare and initialize x
    int y = -(1 << 31); // Declare and initialize y
    int z = x + y; // Compute the sum of x and y
    if (z == x + y) { // Condition can never true 
        /* do something */
    }
    return 0; // Return a value related to the mentioned optimization
}
```

