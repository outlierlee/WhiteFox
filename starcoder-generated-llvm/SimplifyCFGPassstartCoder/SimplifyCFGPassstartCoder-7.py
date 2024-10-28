
```c
#include <stdio.h>
#define BLOCK_SIZE 100

int main() {
  int x = 0;
  int y = 1;

  if (y < x) {
    for (int ii = 0; ii < BLOCK_SIZE; ii++) {
      printf("Block #%d\n", ii);
    }
  } else {
    printf("Unreachable block\n");
  }

  return 0;
}
```
