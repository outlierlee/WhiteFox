
```c
#include <stdio.h>

int x = -1; // initializing variable x

int main() {
  int main_result = 0; // declare the result

  // switch statement with multiple cases
  switch (x) {
    case -50:
      // code block for case -50
      main_result = -500;
      break;
    case 100:
      // code block for case 100
      main_result = 1000;
      break;
    // additional cases as needed
    default:
      // default case code block
      main_result = 0;
      break;
  }

  return main_result; // return the result
}
```
