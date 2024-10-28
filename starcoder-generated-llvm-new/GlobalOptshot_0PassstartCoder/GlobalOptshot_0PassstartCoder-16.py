
```c
#include <stdio.h>

static __attribute__((fastcall)) int my_function(int a, int b) {
  int result = 0;
  if (a % 2) {
    result = a * 2 + b;
  } else {
    result = b * 2;
  }
  if(a > b) {
    result += a;
  } else {
    result += b;
  }
  return result;
}

int main() {
  int result = 0;
  int a = (1 << 31);
  int b = a - 1;
  result = my_function(a, b);
  return result;
}
```

