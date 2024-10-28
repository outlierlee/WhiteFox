```c
#include <stdio.h>

// declare variables
int x = 10; // declare x

int main() {
  int main_result = 0; // declare the result

  // switch statement with multiple cases
  switch (x) {
    case 10:
      // code block for case VALUE_1
      main_result = 100;
      break;
    case 20:
      // code block for case VALUE_2
      main_result = 200;
      break;
    // additional cases as needed
    default:
      // default case code block
      main_result = -1;
      break;
  }

  return main_result; // return the result
}
```
