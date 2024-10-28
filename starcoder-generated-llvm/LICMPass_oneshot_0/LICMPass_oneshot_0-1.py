
```cpp
static int no_side_effect_func(int x) {
  if (x > (1 << 31)) {
    x = x * 3 + 1;
  } else {
    x = x * 3 - 1;
  }
  return x;
}

int main() {
  int result = 0;
  for (int i = 0; i < (1 << 25); ++i) {
    int a = i * 2 - (1 << 25);
    int b = no_side_effect_func(a);
    if (b > 0) {
      result += b;
    }
  }
  return result;
}
```

