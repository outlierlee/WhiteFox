```cpp
#include <unistd.h>

void unused_func() {
  // do anything
}

int main() {
  if (fork() == 0) {
    int r;
    for(r = 0; r < 3; ++r) {
      write(1, "Hello\n", 6);
    }
  } else {
    int status;
    wait(&status);
  }
  return 342;
}
```
