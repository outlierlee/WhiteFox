
```cpp
int main() {
  int x = 25;
  int y = 25;
  while (x == y) {
    x ^= 5;
    y &= 1;
  }
  return 0;
}
```

