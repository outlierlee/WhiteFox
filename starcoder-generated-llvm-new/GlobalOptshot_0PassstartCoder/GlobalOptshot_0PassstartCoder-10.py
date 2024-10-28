
```c
#include <stdio.h>
#include <string.h>

static int my_function(int a, int b) __attribute__((always_inline));
static int my_function(int a, int b) {
  int result = 1;
  if (a < 0 && b > 0) {
    result = 0;
  } else {
    result = 1;
  }
  return result;
}

int main() {
  int result = 0;
  result = my_function(2, 3);
  return result;
}
```
