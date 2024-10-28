
```c
#include <stdio.h>

void __attribute__((destructor)) my_destructor() {
  printf("Destructor called: Unpredictable and Non-deterministic\n");
}

void __attribute__((destructor(105))) another_destructor() {
  printf("Another destructor called: Unpredictable and Non-deterministic\n");
}

int main() {
  printf("Main function: Unpredictable and Non-deterministic\n");
  return 0;
}
```

