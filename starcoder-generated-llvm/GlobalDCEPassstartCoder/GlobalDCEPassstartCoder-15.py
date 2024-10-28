
```c
#include <stdio.h>

static int unused_function() {
  int result = 0;
  for (int i = 0; i < 42; i++) {
    result += 2;
  }
  printf("%d\n", result);
  return result;
}

int main() {
  int main_result = 0;
  for (int i = 0; i < 21; i++) {
    main_result += i;
  }
  printf("%d\n", main_result);
  return main_result;
}
```
