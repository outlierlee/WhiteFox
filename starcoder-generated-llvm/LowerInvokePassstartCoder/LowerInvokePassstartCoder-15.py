
```c
#include <setjmp.h>
#include <stdio.h>

jmp_buf buf;

void test_function() {
  if (setjmp(buf)) {
    printf("After longjmp in test_function\n");
  } else {
    printf("Before longjmp in test_function\n");
    longjmp(buf, 1);
  }
}

int main() {
  test_function();
  return 0;
}
```
