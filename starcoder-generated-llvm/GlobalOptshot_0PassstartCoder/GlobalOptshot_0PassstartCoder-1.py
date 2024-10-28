
```c
#include <stdio.h>

static int __attribute__((fastcall)) my_function(int a, int b) {
  #define var(x, y) x ## y
  return var(a, b);
}

int main() {
  int result = 0;
  result = my_function(5, 34); // Recall the function
  return result;
}
```
