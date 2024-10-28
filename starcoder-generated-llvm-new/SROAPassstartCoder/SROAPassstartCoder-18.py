
```c
#include <stdio.h>

typedef struct {
  unsigned short a;
  long double b;
  char *c;
} MyStruct;

void useStruct(MyStruct *s) {
  s->a = 65535;
  s->b = 3.141592653589793238462643383279502884197169399375105820974944592307816406286;
  s->c = "structstring";
}

int main() {
  MyStruct s;
  useStruct(&s);
  printf("%hu %Lf %s\n", s.a, s.b, s.c);

  return 0;
}
```

