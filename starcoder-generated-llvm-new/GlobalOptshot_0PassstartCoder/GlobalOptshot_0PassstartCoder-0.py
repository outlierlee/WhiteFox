
```c
#include <stdio.h>

static __attribute__((used,fastcall)) int my_function(int a, int b) {
  return a + b;
}

int main() {
  int result;
  result = my_function(5, 10);
  return result;
}
```
