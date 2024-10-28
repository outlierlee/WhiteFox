
```c
#include <stdio.h>
#include <setjmp.h>

jmp_buf buf;

void inverse(int n) {
  if (n > 0) {
    inverse(n - 1);
    if (!setjmp(buf)) {
      longjmp(buf, 1);
    } else {
      printf("%d ", n);
    }
  }
}

int main() {
  inverse(10);
  return 0;
}
```
