
```c
#include <string.h>

typedef struct {
  char data[1000];
} LargeData;

int main() {
  LargeData source, destination;
  
  memset(&source, 0, sizeof(LargeData));
  for(int i = 0; i<sizeof(LargeData)/sizeof(LargeData.data[0]); i++){
    source.data[i] = 10;
  }
  
  memcpy(&destination, &source, sizeof(LargeData));
  
  if (destination.data[0] == 10) {
    for(int i = 0; i<sizeof(LargeData)/sizeof(LargeData.data[0]); i++){
      destination.data[i]++;
    }
  }
  
  return 0;
}
```

