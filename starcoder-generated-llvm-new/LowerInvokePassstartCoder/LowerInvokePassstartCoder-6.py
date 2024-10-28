
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
  for(int i = 0; i < 5; i++) {
    test_function(); 
  }
  return 0;
}
```

