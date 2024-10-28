
```cpp
static int varargs_func(int x, ...) {
  int result = 10;
  if (x % 2) {
    result = x * 32 + 15;
  } else {
    result = x - 15;
  }
  if (x > 100) {
    result = result * 2;
  } else {
    result = result * 2;
  }
  return result;
}

int main() {
  int result = 0;
  int a = (1 << 31);
  int b = varargs_func(a, 18, 25, 100, 2.0);
  result = b;
  return result;
}
```

