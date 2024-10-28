
```cpp
int main() {
    int array1[10];
    int array2[10];
    int i;

    // First loop
    for (i = 0; i < 10; i++) {
        array1[i] = i * 2;
    }

    // Second loop
    for (i = 0; i < 10; i++) {
        array2[i] = array1[i] * 3;
    }

    return 0;
}
```

