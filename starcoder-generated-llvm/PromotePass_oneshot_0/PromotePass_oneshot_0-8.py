
```cpp
int main() {
  int x = 2;
  int y = 3;
  int z = 4;

  int *p = new int;
  *p = x + y + z;

  int result = *p;
  delete p;

  return result;
}
```
