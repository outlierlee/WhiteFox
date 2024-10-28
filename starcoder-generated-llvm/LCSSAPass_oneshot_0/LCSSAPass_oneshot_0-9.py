
```cpp
int main(){
    int x = 20; 
    int y = 30; 
    int z = 40; 
    int result = 0; 
    for (int i = 0; i < 100; ++i) {
        if (i%2 == 0) {
            result += x + y;
        } else {
            result += z;
        }
    }
    return result; 
}
```
