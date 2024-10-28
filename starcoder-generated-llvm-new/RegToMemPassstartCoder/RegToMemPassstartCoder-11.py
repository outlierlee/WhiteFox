
```c
#include <stdio.h>

#define N 5

char buff[N];
char* ptr;
int i;

void example_function() {
  for (i = 0; i < N; ++i) {
    buff[i] = 'A' + i;
  }

  ptr = buff;

  printf("Buffer content: %s\n", buff);
}

int main() {
  example_function();

  return 0;
}
```

