```
#include <stdio.h>

__attribute__((destructor(1000))) void my_first_destructor() {
  printf("First Destructor Called\n");
}

__attribute__((destructor(2000))) void my_second_destructor() {
  printf("Second Destructor Called\n");
}

__attribute__((destructor(3000))) void my_third_destructor() {
  printf("Third Destructor Called\n");
}

int main() {
  printf("This shuld be printed before destructors\n");
  return 0;
}
```
