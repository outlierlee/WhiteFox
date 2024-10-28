
```c
#include <stdio.h>

int switch_func(int x) {
  int result = 0;
  result = (3 + x * 32) * x; // define result with different patterns
  result -= (result + result);
  result /= (x + x);
  result <<= (4 | x);
  return result;
}

int main() {
  int main_result = 0;
  int x = (unsigned char)0xff; // initialize x with any pattern
  main_result = switch_func(x);
  printf("%d\n", main_result);
  printf("%#x\n", main_result);
  return main_result;
}
```

