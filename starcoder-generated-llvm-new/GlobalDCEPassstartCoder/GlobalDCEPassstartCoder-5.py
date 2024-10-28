
```c
#include <stdio.h>

static int unused_function() {
  int result = 0;
  while (1) {}
  return result;
}

int main() {
  int main_result = 0;
  int a = 32;
  int b = 1024;
  for (int i = 0; i < a; ++i) {
    main_result += 1;
  }
  if (main_result > b) {
    main_result = main_result / 2;
  } else {
    main_result = main_result * 2;
  }
  return main_result;
}
```

