
```cpp
int main() {
  int x = (1 << 31); 
  int y = (1 << 29); 
  int z = (1 << 29); 

  // Following part is dead code
  int a = x + y; 
  int b = y * z; 

  int result = x * z;
  return result;
}
```
