
```cpp
int main() {
    int x = 5, y = 8, z = 14;

    // define a dead code block
    if (false) {
        z = x + y;  // this code will never be executed
    }

    return 0;
}
```

