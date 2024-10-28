
```c
#include <stdio.h>
static int my_function(int a, int b) {
  int result = 0;
  result = a - b;
  if ((a > 100) && (b % 2 == 0)) {
    result = result * 2;
  }
  if (a > 0) {
    result = result + a;
  }
  return result;
}

int main() {
  int x = -20;
  int y = 100;
  int main_result = 0;

  main_result = my_function(x, y);

  return main_result;
}
```

