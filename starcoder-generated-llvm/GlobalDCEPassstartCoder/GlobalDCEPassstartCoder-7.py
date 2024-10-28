
```c
#include <string.h>

static int unused_function() {
  int result = 0;
  for (int i = 0; i < 10000; ++i) {
    result += i;
  }
  return result;
}

int main() {
  int main_result = 0;
  char str[1024];
  strcpy(str, "hello world");
  unused_function();
  main_result = 1;
  return main_result;
}

```

