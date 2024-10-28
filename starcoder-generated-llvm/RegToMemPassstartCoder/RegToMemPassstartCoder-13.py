
```c
#include <stdio.h>
#include <stdlib.h>

void varargs_func() {
  int a = rand() % 100;
  int b = rand() % 100;
  int c = 1500;
  float d = 123.1;
  char e = 'E';
  
  a *= 2;
  d *= b; 
  b += a;
  a /= c / 10; 
  
  printf("a: %d, b: %d, d: %f, e: %c\n", a, b, d, e);
}

int main() {
  varargs_func();

  return 0;
}
```

