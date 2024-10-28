
```cpp
int main() {
    int x = 10; 
    int y = 20; 
    int z = 30; 

    int* p = new int; 
    *p = x + y + z; 

    int result = *p; 
    delete p; 

    return result;
}
```
