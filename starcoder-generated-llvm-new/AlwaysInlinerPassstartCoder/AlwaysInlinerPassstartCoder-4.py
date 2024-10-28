
```cpp
inline float inline_func(float a, int b) {
  return a + b;
}

int main() {
  float result = 0;
  float x = 5;
  int y = 10;

  result = inline_func(x, y);

  return result;
}
```
