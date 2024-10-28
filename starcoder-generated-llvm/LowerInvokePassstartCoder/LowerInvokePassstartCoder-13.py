
```c
#include <setjmp.h>
#include <stdio.h>

jmp_buf buf;

void test_function() {
  if (!setjmp(buf)) {
    printf("Before longjmp\n");
    longjmp(buf, 1);
  } else {
    printf("After longjmp\n");
  }
}

int main() {
  test_function();
  return 0;
}
```

