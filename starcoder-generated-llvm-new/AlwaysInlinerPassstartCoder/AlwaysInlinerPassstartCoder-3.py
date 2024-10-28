
```c
#include <stdio.h>

inline double inline_func(int a, int b) {
  return a / (double)b;
}

int main() {
  double result = 0;
  int x = 12;
  int y = 3;
  
  result = inline_func(x, y);
  printf("Result: %.2f\n", result);
  
  return 0;
}
```

