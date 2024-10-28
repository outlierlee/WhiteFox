
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
  int x = 15;
  int y = 27;
  int main_result = 0;
  if (x < y) {
    main_result = my_function(x, y);
  } else {
    main_result = my_function(y, x);
  }
  return main_result;
}
```
