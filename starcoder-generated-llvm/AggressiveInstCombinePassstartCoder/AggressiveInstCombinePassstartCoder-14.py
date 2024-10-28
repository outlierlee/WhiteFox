
```c
#include <stdio.h>

static int trunc_func(char a, unsigned char b, int c) {
  int result;
  if (a > b) {
    result = a - b;
  } else {
    result = c;
  }
  if (c > 0) {
    result = result * 2;
  } else {
    result = result / 2;
  }
  if (b > 2) {
    result = result + a;
  } else {
    result = result - a;
  }
  return result;
}

int main() {
  char a = 127;
  unsigned char b = 100;
  int c = -1;
  int main_result = trunc_func(a, b, c);
  printf("%d\n", main_result);
  return 0;
}
```
