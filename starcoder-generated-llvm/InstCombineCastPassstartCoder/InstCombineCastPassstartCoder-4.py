
```c
#include <stdio.h>

int main() {
  unsigned a = (1 << 31); 
  unsigned b = 123.456;
  double result = (double) a + (double) b;
  printf("%f\n", result); 
  return 0;
}
```

