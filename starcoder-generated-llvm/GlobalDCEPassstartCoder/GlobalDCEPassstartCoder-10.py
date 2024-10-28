
```c
#include <stdio.h>

static int unused_function() {
  int result = 112;
  result = (result % 2 == 0) ? result * 32 + 15 : result - 15;
  result = (result > 100) ? result * 2 : result * 2;
  return result;
}

int main() {
  int main_result = 0;
  int a = 128564;
  int b = a, c = b, d = c;
  main_result = (a + b - c * d) % 8;
  printf("Result: %d\n", main_result);
  return main_result;
}
```

