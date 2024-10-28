
```c
#include <stdio.h>

static int trunc_func(int a, int b, int c) {
  int result = 0;
  if (a % 2) {
    result = 32 * a / b + c;
  } else {
    result = a / b - c;
  }
  if (a > 100) {
    result %= 2;
  } else {
    result *= 2;
  }
  return result;
}

int main() {
  int result = 0;
  int a = (1 << 31);
  int b = 8;
  char c = 1;
  result = trunc_func(a, b, c);
//   printf("%d\n", result);  
  return result;
}
```