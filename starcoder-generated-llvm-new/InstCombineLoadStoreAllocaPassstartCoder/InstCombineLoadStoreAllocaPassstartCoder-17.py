
```c
#include <string.h>

int main() {
  int result = 0;
 const int codes[] = {1, 2, 3, 4, 5, 6, 7 , 8 , 9 , 10};
  int copy[10];

  memcpy(copy, codes, sizeof(codes));
  for(int i=0;i<10;i++){
    result = result + copy[i];
  }

  return result;
}
```

# C++ Code endes