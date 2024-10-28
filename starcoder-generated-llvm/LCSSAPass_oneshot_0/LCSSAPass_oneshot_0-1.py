
```cpp
int main() {
    int x = 10; // declare variable x
    int y = 20; // declare variable y
    int z = 30; // declare variable z
    int result = 0;

    // define a loop
    for (int i = 0; i < 100; ++i) {
        if ((i % 2) == 0) { // CONDITION can be any condition that uses i, x, y, z
            result += x + y;
        } else {
            result += z;
        }
    }

    return result;
}
```

