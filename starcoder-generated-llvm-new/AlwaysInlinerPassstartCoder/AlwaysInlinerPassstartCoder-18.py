
```cpp
inline int inline_func(int a, int b) {
  int res;
  res = a * b;
  if (a > b) {
    res = 5 * a;
  }
  return res;
}

int main() {
  int result = 0;
  int a = 5, b = 10;
  int c = 5, d = 1;
  result = inline_func(a, b);
  result += inline_func(c, d);
  return result;
}
```

