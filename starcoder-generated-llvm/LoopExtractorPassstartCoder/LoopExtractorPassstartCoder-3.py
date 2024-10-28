
```c
#include <stdio.h>

void loop_function() {
  int i = 0;
  int a = 0, b = 1;
  int sum = 0;
  for (i = 0; i < 10; i++) {
    sum += i; 
    if (b % 2) {
      a = b + 3;
    } else {
      a = b - 2;
    }
    b = b * 2;
  }
  printf("Sum: %d\n", sum);
}

int main() {
  loop_function();
  return 0;
}
```
