
```cpp
int main() {
    int x = 10; // Declare and initialize variable x
    int y = 20; // Declare and initialize variable y
    int z = 30; // Declare and initialize variable z

    // Perform some operations that do not affect the final result
    int a = x + y; // a is not used afterwards
    int b = y * z; // b is not used afterwards

    // The final result is related to x and z
    int result = x * z; // result is only related to x and z

    return result;
}
```
