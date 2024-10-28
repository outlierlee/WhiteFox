
```cpp
int main() {
    const int size = 10;
    int *arr = new int[size]; // allocate memory
    for (int i = 0; i < size; i++)
        arr[i] = 10; // store values
    for (int i = 0; i < size; i++)
        arr[i] = 20; // overwrite the values
    delete[] arr; // deallocate memory
    return 0;
}
```
The C++ code should contain the following pattern:

