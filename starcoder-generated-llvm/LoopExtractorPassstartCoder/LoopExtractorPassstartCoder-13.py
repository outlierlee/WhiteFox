
```c
#include <stdio.h>

// A function with a loop that isn't being extracted
void uselessLoopFunction() {
  int i;
  int sum = 0;

  for (i = 0; i < 2000; i++) {
    sum += i;
  }

  printf("Useless sum: %d\n", sum);
}

// A function with a loop that is being extracted
void myLoopFunction() {
  int i;
  int sum = 0;

  for (i = 0; i < 10; i++) {
    sum += i;
  }
}

int main() {
  uselessLoopFunction();
  myLoopFunction();

  return 0;
}
```

