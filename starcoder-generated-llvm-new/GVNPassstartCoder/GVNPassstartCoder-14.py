
```c
#include <stdio.h>

void example_func() {
  int a = 15;
  int b = 25;
  if (a < b) {
    a = a + 1;
  } else {
    a = a - 1;
  }
  if (a < b) {
    a = a + 1;
  } else {
    a = a - 1;
  }
  printf("%d\n", a);
}

int main() {
  example_func();
  return 0;
}
```

