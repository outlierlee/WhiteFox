
```c
#include <stdio.h>

inline int inline_func(int a, int b, int c) {
  int result = a + b * c;
  if (result > 100) {
    result -= 50;
  } else {
    result += c;
  }
  return result;
}

int main() {
  int result = 0;
  int x = 10;
  int y = 20;
  int z = 100;
  result = inline_func(x, y, z) - 10;
  printf("result = %d\n", result);
  return result;
}
```

The `inline_func` function multiplies the first two parameters and adds the third one. In the main function, this multiplication is done with the variables x, y and z. The operation x + y*z is performed first, followed by an addition or subtraction depending on whether the result is larger than 100 or not, then returned.

