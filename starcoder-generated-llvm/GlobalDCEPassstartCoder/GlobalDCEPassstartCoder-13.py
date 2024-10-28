
```c
#include <stdio.h>
static int unused_function() {
  int result = 10;
  return result;
}

int main() {
  int* a = (int* )malloc(sizeof(int) * 10);
  int b = 0;
  int main_result = 10;
  for (int i = 0; i < 10; i++) {
    a[i] = i + 1;
    if (i < 5) {
      b += a[i] * 2;
    } else {
      b -= a[i] / 2;
    }
  }

  main_result = b;
  free(a);
  return main_result;
}
```

