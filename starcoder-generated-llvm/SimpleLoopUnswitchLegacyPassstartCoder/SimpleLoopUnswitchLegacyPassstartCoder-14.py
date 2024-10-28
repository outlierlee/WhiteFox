
```c
#include <stdio.h>

static void loop_with_condition(int n, int flag) {
  if (!(n > 10)) {
    for (int i = 0; i < n; ++i) {
      if (!(i %2)) {
        printf("i is even, iteration %d\n", i);
      } else {
        printf("i is odd, iteration %d\n", i);
      }
    }
  } else {
    for (int i = 0; i < (n / 2); ++i) {
      printf("value is: %d\n", i);
    }
    for (int i = n / 2; i < n; ++i) {
      printf("value is: %d\n", i);
    }
  }
}

int main() {
  int n = 12;
  int flag = 1;

  loop_with_condition(n, flag);

  return 0;
}
```
