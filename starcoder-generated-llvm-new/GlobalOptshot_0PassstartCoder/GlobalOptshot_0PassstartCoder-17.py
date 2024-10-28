
```c
#include <stdio.h>

static __attribute__((fastcall)) int my_function(int a, int b) {
  a = a - b;
  b = a + b;
  return a > b ? a  : b;
}

int main() {
  int result = 0;
  // Call the function directly
  result = my_function(5, 10);
  return result; // Return the result
}
```
