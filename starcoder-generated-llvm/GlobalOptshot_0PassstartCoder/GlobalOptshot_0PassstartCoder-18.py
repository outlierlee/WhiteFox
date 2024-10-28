
```cpp
static int my_function(int a, int b) {
  int res;
  res = a * b;
  if (a > b) {
    res = 5 * a;
  }
  return res;
}

int main() {
  int res = 0;
  res = my_function(4, 100);
  return res;
}
```
