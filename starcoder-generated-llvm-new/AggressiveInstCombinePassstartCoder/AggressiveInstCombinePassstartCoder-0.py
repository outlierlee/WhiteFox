
```cpp
#include <stdio.h>

int a = 10;
int b = 3;
int c = 2;

static int trunc_func(int a, int b, int c) {
  int result = 0;
  if (a > b) {
    result = (a % b) + c;
  } else if (a > 0) {
    result = (b << 1) * 3;
  } else {
    result = ((a >> 1) & c) | 1;
  }
  return result;
}

int main() {
  int main_result = 0;
  main_result = trunc_func(a, b, c);
  printf("%d\n", main_result);
  return 0;
}
```
