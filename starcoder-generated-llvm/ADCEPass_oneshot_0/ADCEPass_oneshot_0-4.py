
```cpp
int main() {
    int x = 5;
    int y = 10;
    int z = 20;

    // Perform some calculations which are not useful
    int a = x + y; // a is not used afterwards
    int b = y * z; // b is not used afterwards

    // The final result calculates only on x and z
    int result = x * z; // result is only related to x and z

    return result;
}
```

