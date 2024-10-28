
```c
#include <stdio.h>

int x = 5;

int main() {
  int main_result = 0;

  switch (x) {
    case 1:
      printf("This is case 1\n");
      main_result = 100;
      break;
    case 2:
      printf("This is case 2\n");
      main_result = 200;
      break;
    case 3:
      printf("This is case 3\n");
      main_result = 300;
      break;
    case 4:
      printf("This is case 4\n");
      main_result = 400;
      break;
    case 5:
      printf("This is case 5\n");
      main_result = 500;
      break;
    default:
      printf("Default case\n");
      main_result = 600;
      break;
  }

  return main_result;
}
```

