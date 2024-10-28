
```c
#include <setjmp.h>
#include <stdio.h>

jmp_buf buf;

void varargs_func(int x, ...) {
  va_list args;
  va_start(args, x);

  if (setjmp(buf) != 0) {
    printf("Test passed man. Hooray! Starting exception chain. %d\n", x);
  } else {
    printf("Testing the inner call with argument: %d\n", x);
    if (x > 10) {
      longjmp(buf, 1);
    }
  }
  va_end(args);
}

int main() {
  varargs_func(5, 1, 2, 3);
  return 0;
}
```
