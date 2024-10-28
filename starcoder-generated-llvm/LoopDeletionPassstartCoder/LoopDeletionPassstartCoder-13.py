
```c
#include <stdio.h>
int main() {
  int x = 300;
  int y = 0;
  while (x < 0) {
    y += (x - x - 1);
  }
  return y;
}
```

