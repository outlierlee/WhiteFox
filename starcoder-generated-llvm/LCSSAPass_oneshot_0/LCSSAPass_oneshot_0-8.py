
```cpp
int main() {
  int x = 2;
  int y = 3;
  int z = 4;
  int result = 0;

  for (int i = 0; i < 10; ++i) {
    if (y == 2) {
      result += x + y;
    } else {
      result += z;
    }
    z += 2;
  }

  return result;
}
```
