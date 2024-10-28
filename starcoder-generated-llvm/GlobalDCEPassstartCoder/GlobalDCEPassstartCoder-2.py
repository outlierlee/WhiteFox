
```c
#include <stdio.h>

static int unused_function() {
  return 0;
}

int main() {
  printf("Hello, world! %s\n", "message from main");
  using namespace std;
  int main_result;
  for(int i=0; i<1000; ++i) {
    main_result += i;
  }
  return main_result;
}
```

