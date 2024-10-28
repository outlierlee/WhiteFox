
```c
#include <string.h>

typedef struct {
  char data[1000];
} LargeData;

int main() {
  const int len = 32;
  LargeData source, destination;
  for (int i = 0; i < len; i++) {
    source.data[i] = i % 256;
  }
  memcpy(&destination, &source, sizeof(LargeData));
  bool used = true;
  for (int i = 0; i < len; i++) {
    if (destination.data[i] != i % 256) {
      used = false;
      break;
    }
  }
  if (used) return 0;
  else return -1;
}
```

