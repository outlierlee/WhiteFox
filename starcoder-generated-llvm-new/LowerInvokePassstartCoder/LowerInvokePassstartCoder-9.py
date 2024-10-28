
```c
#include <setjmp.h>
#include <stdio.h>

jmp_buf buf;

void test_function() {
  if (setjmp(buf)) {
    printf("After longjmp in test_function\n");
  } else {
    printf("Before longjmp in test_function\n");
    short x=10, y=20;
    float z = x / y;
    if (z == 0.5)
      longjmp(buf, 1);
  }
}

int main() {
  int x=10 , y=0;
  double z;

  test_function();

  if (setjmp(buf)) {
    z = (double) x / y;
    printf("Inside main after longjmp, z = %.1lf\n", z);
  }
  
  return 0;
}
```
