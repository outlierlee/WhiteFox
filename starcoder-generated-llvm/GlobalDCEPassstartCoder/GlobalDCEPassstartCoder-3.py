
```c
#include <stdio.h>

static int unused_function() {
  int result = 0;
  int flag = result > 0;
  if (flag) {
    result = (flag * 0xFFFFFFFF) + 1;
  }
  if (result <= 10) {
    if (result > 0) {
      result -= 5;
    }
  } else {
    result += 5;
  }
  return result;
}

int main() {
  int main_result = 0;
  int x = (1 << 16);
  for (int i = 0; i < x ; ++i) {
    main_result += i;
  }
  for (int i = x; i > 0; --i) {
    int value = i;
    value &= value -1;
    if (value == 0) {
      if (i > main_result) {
        main_result = i;
      }
    }
  }
  unused_function();
  return main_result;
}
```
