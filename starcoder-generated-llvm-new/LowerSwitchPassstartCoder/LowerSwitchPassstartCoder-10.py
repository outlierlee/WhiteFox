
```c
#include <stdio.h>

int x = 92; // declare x

int main() {
  int main_result = 0; // declare the result

  switch (x) {
    case 75:
      main_result = 100;
      break;
    case 80:
      main_result = 90;
      break;
    case 90:
      main_result = 95;
      break;
    default:
      main_result = 100;
      break;
  }

  return main_result; // return the result
}
```

# C Code ends

This is a simplification of the `main` function and the `switch` statement using the entire pattern mentioned. The exact values of the constants must be substituted with typical real-world integer values.