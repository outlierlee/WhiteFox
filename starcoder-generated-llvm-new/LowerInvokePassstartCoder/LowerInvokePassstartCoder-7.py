
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
  int result = 0; 
  test_function();
  int var = 10;
  while (var < 20) {
    if (var == 15) {
      longjmp(buf, 1);
      break;
    }
    if (var >= 20) {
      setjmp(buf);
      break;
    }
    var++;
  }
  
  if (var > 20) {
    result = var;
  } else {
    result = var - 10;
  }
  return result;
}
```

