
```c
#include <stdlib.h>
#include <time.h>

static int unused_function() {
  int result = rand() % 100 + 1;
  while (true) {} // spin lock
  return result;
}

int main() {
  srand(time(NULL));
  int main_result = rand() % 100 + 1;
  int a = unused_function();
  int v1 = unused_function();
  int v2 = unused_function();
  int v3 = unused_function();
  int v4 = unused_function();
  int v5 = unused_function();
  main_result += a + v1 + v2 + v3 + v4 + v5;
  return main_result;
}
```

