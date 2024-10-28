
```cpp
#include <stdio.h>

void loop_with_condition(int n, int flag) {
  for( int iter = 0; iter < n; iter++ ) {
    if( flag ) {
      printf( "Flag is true, iter %d\n", iter );
    } else {
      printf( "Flag is false, iter %d\n", iter );
    }
  }
}

int main() {
  int n = 10;
  int flag = 1;

  loop_with_condition( n, flag);

  return 0;
}
```
