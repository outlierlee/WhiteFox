
```c
#include <setjmp.h>
#include <stdio.h>

jmp_buf buf;

void test_function() {
  int i = 0;
  if(setjmp(buf)) {
    i = (2<<30); // change the value only in case of longjmp
    goto DONE;
  } else {
    goto AFTER_SETJMP;

AFTER_SETJMP:
    longjmp(buf, 1); // start long jump
    printf("We should never reach here\n");
}

DONE:
    i = (2<<30); // change the value only in case of longjmp
}

int main() {
  int result = 0;
  test_function();
  result |= buf != 0;
  return result;
}
```

