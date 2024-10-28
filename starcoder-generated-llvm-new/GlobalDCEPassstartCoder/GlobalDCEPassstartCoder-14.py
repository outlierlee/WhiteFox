
```c
#include <stdlib.h>

static int unused_function() {
  srand(10);
  int result =  rand() % 2048;
  return result;
}

int main() {
  int main_result = 2048;
  void *ptr = malloc(2048);
  if (ptr) {
    free(ptr);
  }
  return main_result;
}
```
