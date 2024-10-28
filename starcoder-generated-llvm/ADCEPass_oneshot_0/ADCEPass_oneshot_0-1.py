
```cpp
int main() {
    int x = 10; // declare variable x
    int y = 20; // declare variable y
    int z = 30; // declare variable z

    int a = x + y; // a is not used afterwards
    int b = y * z; // b is not used afterwards

    int result = x * z; // result is only related to x and z

   return result;
}
```
