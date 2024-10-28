```c
#include <setjmp.h>
#include <stdio.h>

jmp_buf buf;

void test_function() {
  if (setjmp(buf)) {
    printf("After longjmp\n");
    // Immediately trigger another jump back to the setjmp point
    longjmp(buf, 1); 
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
