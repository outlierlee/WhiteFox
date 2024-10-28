
```cpp
int func(int x, int y) {
  int result = 0;
  if (x % 2) {
    result = x * 32 + y * 15;
  } else {
    result = x - y - 15;
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
  int b = func(a, -18);
  result = func(10, 20);
  short truncated_result = static_cast<short>(result);
  return truncated_result;
}
```

