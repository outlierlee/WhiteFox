```c
#include <stdio.h>

static int trunc_func(int a, float b, char c) {
  int result = (int)((char)(a * b)) * c;
  return result;
}

int main() {
  int result = 0;
  int a = 256;
  float b = 5.6789;
  char c = -30;

  result = trunc_func(a, b, c);

  printf("%d\n", result);

  return 0;
}
```
