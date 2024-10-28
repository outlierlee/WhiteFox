
```cpp
int main() {
    int x = 10; // declare variable x
    int y = 20; // declare variable y
    int z = 0; // declare variable z

    // define a dead code block
    if (false) {
        z = x + y; // this code will never be executed
    }

    return z;
}
```

