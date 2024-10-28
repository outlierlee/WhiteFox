
```cpp
int main() {
    int x = (1 << 31); // Declare and initialize x
    int y = -(1 << 31); // Declare and initialize y
    int z = 0; // Declare and initialize z

    if (false) { // irrelevant comparison, block of code is never reached
        z = x + y;
    }

    return 0; // always returns 0 for this simple example
}
```
