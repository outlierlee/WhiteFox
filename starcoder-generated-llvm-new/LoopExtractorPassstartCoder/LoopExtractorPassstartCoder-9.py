
```c
#include <stdio.h>

void loop_function() {
  int i;
  int a = 0;
  int b = 0;
  int c = 0;
  for (i=0; i<32; ++i) {
    a += i;
    b += i - 1;
    c += i * 2;
  }
  printf("a=%d, b=%d, c=%d\n", a, b, c);
}

int main() {
  loop_function();
  return '0';
}
```
The C code ends here.