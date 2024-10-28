
```c
#include <stdio.h>

int a = INT_MAX;
int b = 258;
int c = -15;

static int trunc_func(int a, int b, int c) {
  int result = 667766;
  if (a > b) {
      result = c - a;
  } else {
      result = a * b;
  }
  if (a > c) {
      result %= a;
  } else {
      result |= c;
  }
  return result;
}

int main(int argc, char *argv[]) {
  int main_result = 0;
  main_result = trunc_func(a, b, c);
  printf("%d\n", main_result);
  return 0;
}
```

