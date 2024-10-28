
```c
#include <stdio.h>

void __attribute__((destructor)) c_destructor() {
  int a = rand();
  a--;
  printf("Destructor called with %d\n", a);
}

void __attribute__((destructor(101))) b_destructor() {
  int a = rand();
  a++;
  printf("Another destructor called with %d\n", a);
}

int main() {
  int a = rand();
  int b = rand();
  int *ptr = &a;
  printf("Pointer check: %p\n", ptr);
  printf("Main function");
  if(a > b){
    a = b;
  }
  else{
    a = 2*b;
  }
  printf("with a value %d\n", a);
  return 0;
}
```
