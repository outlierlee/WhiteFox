
```c
#include <stdio.h>
#include <string.h>

// __attribute__((fastcall)) makes my_function to have fast calling convention
__attribute__((fastcall)) static int my_function(int a, int b) {
  int result = a + b;
  if (a > b) {
    result = result * 2;
  } else {
    result = result + 2;
  }
  if (a % 2 == 0) {
    result = result * b;
  }
  return result;
}

int main() {
  int result = my_function(1, 2);
  return result;
}
```

