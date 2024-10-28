
```c
#include <stdio.h>

void __attribute__((destructor)) my_destructor() {
  char* ptr = NULL;
  if (!ptr) {
    printf("Null pointer detected\n");
  }
}

void __attribute__((destructor(102))) another_destructor() {
  int x = 10;
  printf("Another destructor called with value %d\n", x);
}

int main() {
  int y = 15;
  printf("Main function called with value %d\n", y);
  return 0;
}
```
