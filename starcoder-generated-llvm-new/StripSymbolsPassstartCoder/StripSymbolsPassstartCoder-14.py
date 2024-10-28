
```c
#include <stdio.h>

typedef struct {
   int a;
   float b;
   double c;
} MyStruct;

MyStruct globalVar = {1, 1.1, 1.01};

void useStruct(MyStruct s) {
  printf("a: %d, b: %f, c: %lf\n", s.a, s.b, s.c);
}

int main() {
  useStruct(globalVar);
  return 0;
}
```
