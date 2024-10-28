
```c
#include <stdio.h>

int main() {

    int seed = 1;
    int result = seed;
    MyStruct s;

    for(int i = 0; i< 1e5; i++)
      result += i;
  
    printf("result: %d\n", result);
  
    return result;
}
```
