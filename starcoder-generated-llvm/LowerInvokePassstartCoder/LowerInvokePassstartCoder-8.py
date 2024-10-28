
```c
#include <setjmp.h>
#include <stdio.h>

jmp_buf buf;

void test_function() {
  if (setjmp(buf)) {
    printf("After longjmp\n");
  } else {
    printf("Before longjmp\n");
    longjmp(buf, 1);
  }
}

int main() {
  test_function();
  return 0;
}
```
# C Code ends