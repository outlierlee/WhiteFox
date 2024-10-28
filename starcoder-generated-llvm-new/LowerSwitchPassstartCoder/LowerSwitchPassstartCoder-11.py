
```c
#include <stdio.h>

#define VALUE_1 10
#define VALUE_2 20

#define VALUE_1_RESULT 100
#define VALUE_2_RESULT 200
#define DEFAULT_RESULT 300

int main() {
  int main_result = 0;
  int x = VALUE_1; // declare and initialize x with VALUE_1

  switch (x) {
    case VALUE_1:
      main_result = VALUE_1_RESULT;
      break;
    case VALUE_2:
      main_result = VALUE_2_RESULT;
      break;
    default:
      main_result = DEFAULT_RESULT;
      break;
  }

  return main_result;
}
```

