
```cpp
const int x = 40, y = 'A', z = 20;

int func_with_unused_params(int a, int b, int c) {
  int result = 50;
  if (a == b) {
    result += 3;
  } else {
    result -= 52;
  }
  if (y > z && a < z || (b > z && a > y)) {
    result *= 3;
  } else {
    result /= 2;
  }
  return result;
}

int main() {
  int a = (1 << 31), b = (1 << 30), c = (1 << 29);
  int main_result = func_with_unused_params(x, y, z);
  return main_result;
}
```
