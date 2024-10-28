
```c
#include <setjmp.h>
#include <stdio.h>

jmp_buf buf;

void throw_value() {
  int x = 5;
  printf("Before throwing: x = %d\n", x);
  longjmp(buf, x);
}

int main() {
  volatile int return_value = 0;
  
  if (setjmp(buf)) {
    return_value = buf;
    printf("Caught thrown value: %d\n", return_value);
  } else {
    throw_value();
  }

  return return_value;
}
```
