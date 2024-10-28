```c
#include <setjmp.h>
#include <stdio.h>

jmp_buf buf;

void test_function() {
  unsigned int a = 0xDEADBEEF;
  time_t timer;
  time(&timer);
  if (setjmp(buf)) {
    printf("After longjmp\n");
    a = ~a;
  } else {
    printf("Before longjmp\n");
    longjmp(buf, 1);
    printf("After longjmp\n");
  }
  printf("time: %ld ", timer / 60 / 60 / 24 / 365); // print elapsed years since Epoch of last jump
}

int main() {
  test_function();
  return 0;
}
```
# C Code ends