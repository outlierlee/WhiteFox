
```cpp
#include <stdio.h>

const double sqrt_two =  1.41421356237;

int main() {
  char x = 'J';
  unsigned short y = 42021;

  double result = ((double) x + (double) y / sqrt_two);
  
  printf("%f\n", result);

  int int_result = (int) result;
  return int_result;
}
```
