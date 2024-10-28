
```c
#include <stdio.h>

int x = 100;

int main() {
  int main_result = 0;

  switch (x) {
    case 50:
      main_result = 10;
      break;
    case 100:
      main_result = 20;
      break;
    case 150:
      main_result = 30;
      break;
    default:
      main_result = 40;
      break;
  }

  return main_result;
}
```

The given program starts with the declaration of the variable `x` with the value `100`. Then in the `main` function, we use a `switch` statement on `x`, with 4 cases `50`, `100`, `150` and the `default` case. The program flow will enter the case where `x` is `100`, so the variable `main_result` will get the value `20` and `20` will be returned from the `main` function. This will trigger a specific version of the `main` function for specific C++ compilers that support light-weight switch case optmizations.