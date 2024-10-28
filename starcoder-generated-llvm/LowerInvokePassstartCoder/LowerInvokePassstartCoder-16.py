
```cpp
#include <setjmp.h>
#include <stdio.h>

jmp_buf buf;

void test_function(int x) {
  if (setjmp(buf)) {
    printf("After longjmp with %d\n", x);
  } else {
    printf("Before longjmp with %d\n", x);
    int y = x * 2;
    longjmp(buf, y);
  }
}

int main() {
  int result = 0;
  test_function(10);
  test_function(20);
  result = x;
  return result;
}
```

