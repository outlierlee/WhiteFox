
```cpp
int main() {
  int x = 25;
  int y = 25;
  int z = 25;
  while (x < y) {
    y = y - 1;
    if (z < x) {
      x = x + 10;
      break;
    }
  }
  return 0;
}
```

