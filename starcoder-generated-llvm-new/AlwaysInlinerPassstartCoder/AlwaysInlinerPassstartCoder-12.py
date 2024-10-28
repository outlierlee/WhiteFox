
```c
#include <stdio.h>

inline int inline_func(int a, int b) {
  int result = 0;
  if (a > b) {
    result = a + 3;
  } else {
    result = a - b;
  }
  return result;
}

int main() {
  int result = 0;
  int a = 5;
  int b = 10;
  result = inline_func(a, b);

  return result;
}
```

