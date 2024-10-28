
```cpp
int main() {
    int x = 5, y = 8, z = 14;

    int *p = new int;
    *p = x + y + z;

    int result = *p;
    delete p;

    return result;
}
```

