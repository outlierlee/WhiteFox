
```c
#include <setjmp.h>
#include <stdio.h>

char buf[1024] __attribute__ ((aligned (16)));
jmp_buf state;

void catch_function() {
  longjmp(state, 1);
}

int main() {
  volatile int result = 0;
  if (setjmp(state) == 0) {
    fprintf(stderr, "Printing before longjmp\n");
    catch_function();
  } else {
    fprintf(stderr, "Printing after longjmp\n");
    result = 1;
  }
  return result;
}
```
