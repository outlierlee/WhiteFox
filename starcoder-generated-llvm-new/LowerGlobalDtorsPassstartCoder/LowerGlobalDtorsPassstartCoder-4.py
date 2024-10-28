
```cpp
#include <stdio.h>

void __attribute__((destructor)) my_destructor() {
  printf("Destructor called during exit\n");
}

void __attribute__((destructor(101))) another_destructor() {
  printf("Another Destructor called with higher priority\n");
}

static int my_static_variable = 1024;

int main() {
  printf("Main function calling exit()\n");
  exit(0);
}
```

