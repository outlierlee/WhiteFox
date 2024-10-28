
```c
#include <stdio.h>

void example_function() {
  int a = 129 + 48;
  int b = 0;
  char op = 'w';
  int i;

  for(i = 0; i < 7; i++)
  { b += a % (i+i+1);
    b += a;
    b ++;
    b --;
  }

  if(op >= 'a' && op <= 'z')
    op = 'A' + op - 'a';

  printf("b is %d, op is %c \n", b, op);
}

int main() {
  example_function();

  return 0;
}
```
