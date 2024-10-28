
```cpp
int main() {
    int result = 0;
    int *p = new int;
    *p = 10;
    *p = 20;
    result = *p;
    delete p;
    return result;
}
```
