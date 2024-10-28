
```c
#include <stdio.h>

void __attribute__((destructor)) my_destructor() {
  printf("Destructor 1 called\n");
}

void __attribute__((destructor(101))) another_destructor() {
  static int count = 0;
  printf("Destructor 2 called %d times\n", ++count);
}

int main() {
  printf("Main function called\n");
  return 0;
}
```
