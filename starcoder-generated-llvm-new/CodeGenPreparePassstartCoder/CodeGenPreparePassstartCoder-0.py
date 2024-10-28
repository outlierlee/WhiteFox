
```c
#include <stdio.h>

// Define a function with a switch statement
int switch_func(int x) {
  int result = 0;
  switch (x) {
    case 1:
      result = x + 1;
      break;
    case 2:
      result = x + 2;
      break;
    default:
      int y = x - 5;
      switch (y > 0 ? 0 : 1) {
        case 1: 
          result = -1; 
          break;
        default:
          result = 42;
          break;
      }
      result = result * 2;
      break;
  }
  return result;
}

int main() {
  int main_result = 0;
  unsigned int x = (1 << 31);
  main_result = switch_func((int) x);
  printf("%d\n", main_result);
  return main_result;
}
```
