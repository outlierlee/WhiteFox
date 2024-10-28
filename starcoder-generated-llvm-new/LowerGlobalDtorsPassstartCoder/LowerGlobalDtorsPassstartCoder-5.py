
```c
#include <stdio.h>

void __attribute__((destructor)) my_destructor() {
  if (1) {
    printf("Destructor#1 called\n");
  }
}

void __attribute__((destructor(101))) another_destructor() {
  if (0) {
    printf("Another destructor called\n");
  }
}

int main() {
  print("Hello, World!\n");
  return 0;
}
```

