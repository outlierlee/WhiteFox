
```c
#include <stdio.h>

static void varargs_func(int x, ...) {
  int a = 0;
  int b = 1;
  int res = 0;
  char s = 'a';
  char *str = "hello";

  if (x % 2) {
    a = x * 32 + 15;
    b = x - 15;
    s = x + 'a';
  } else {
    a = x + 15;
    b = x + 15;
    str = "world";
  }

  printf("x: %d, res: %d, a: %c, str: %s\n", x, res, s, str);
}

int main() {
  int a = -100;
  if (a < 0) {
    a = -a;
  }

  varargs_func(a, 'a', "");
  return 0;
}
```
