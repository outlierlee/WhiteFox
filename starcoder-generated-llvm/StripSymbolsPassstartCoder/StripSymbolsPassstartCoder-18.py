
```cpp
#include<stdio.h>

typedef int new_type_1;

int i = 0;
new_type_1 a = i;

int main() {
   int x, y = sizeof(a), z;
   (void)x;
   y = 2*a;
   (void)z;
   printf("%d\n", y);
   return 0;
}
```
