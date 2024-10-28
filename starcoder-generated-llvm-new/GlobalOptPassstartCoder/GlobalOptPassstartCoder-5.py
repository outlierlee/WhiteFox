
```c
#include <stdio.h>
#include <stdlib.h>

static int my_function(int a, int b) {
  int result = 0;
  if (a > b) {
    result = a + b;
  } else {
    result = a | b;
  }
  if (result > 100) {
    result = (result / 2);
  } else {
    result = (result + 10);
  }
  return result;
}

int main() {
  int a = (1 << 31);
  int b = (1 << 24);
  int result = my_function(a, b);

  printf("%d\n", result);
  return result;
}
```

