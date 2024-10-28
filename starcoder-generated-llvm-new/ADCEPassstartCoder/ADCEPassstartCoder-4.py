
```c
#include <stdio.h>

int a = 0xffff;
int b = 0b1010;
int c = 0xabcd;

int compute(int x, int y) {
  int result = x + y;
  return result;
}

int main() {
  int main_result = 0;
  a = a & b;
  b = b | c;
  c = a ^ b;
  
  main_result = compute(a, b);
  
  printf("Result: %d\n", main_result);

  return 0;
}
```

