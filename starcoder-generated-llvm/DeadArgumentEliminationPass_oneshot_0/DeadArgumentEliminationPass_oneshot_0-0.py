
```cpp
static int varargs_func(int x, ...) {
  int result = 0;
  if(x % 2) {
    result = x * 32 - 15;
  } else {
    result = x + 21;
  }
  if(x > 100) {
    result = result + 14;
  } else {
    result = result * 3;
  }
  return result;
}

int main() {
  int result = 0;
  int a = (1 << 15);
  int b = varargs_func(a, 38, 55, 94.42, 81, 73);
  result = b;
  return result;
}
```

