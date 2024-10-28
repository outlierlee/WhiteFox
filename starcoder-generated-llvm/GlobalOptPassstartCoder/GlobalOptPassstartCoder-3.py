
```c
#include <stdio.h>

static int my_function(int a, int b) {
  int result = 0;
  if (a > b) {
    result = a - b;
  } else {
    result = b - a;
  }
  return result;
}

int main() {
  int x = 10;
  int y = 5;
  int main_result = 0;

  main_result = my_function(x, y);

  return main_result;
}
```

