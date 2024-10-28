
```c
#include <stdio.h>

// declare a static function that is never called 
static int unused_function() {
  int result = 1;
  result = 1 ^ 1;
  return result;
}

int main() {
  int unused_function_called = unused_function();
  int main_result = unused_function_called + 1;

  for (int i = 0; i < 10; i++) {
    main_result += i;
  }

  return main_result;
}
```

