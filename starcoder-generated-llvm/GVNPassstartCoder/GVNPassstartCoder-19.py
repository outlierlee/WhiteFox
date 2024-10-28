```c
#include <stdio.h>

void example_function() {
  int x = 50, y = 100;
  int a = x + 10;
  if(a < y) {
    printf("%d\n", a);
  } else {
    printf("%d\n", a );
  }

  if(y < x) {
    printf("%d\n", y);
  } else {
    printf("%d\n", y);
  }
}

int main() {
  example_function();
  return 0;
}
```
