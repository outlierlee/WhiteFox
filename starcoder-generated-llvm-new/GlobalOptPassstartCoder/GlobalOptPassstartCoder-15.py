
```c
#include <stdio.h>

static int my_function(int a, int b) {
  int result = 0;
  if (a % 2 == 0) {
    result = a * 2 + b;
  } else {
    result = a / 2;
  }
  if (a > 50) {
    result = result * 2;
  } else {
    result = result / 2;
  }
  return result;
}

int main() {
  int a = 31;
  int b = 3;
  int main_result = 0;

  main_result = my_function(a, b);

  return main_result;
}
```

