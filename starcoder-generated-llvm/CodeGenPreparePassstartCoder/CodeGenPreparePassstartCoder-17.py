
```c
#include <stdio.h>

int switch_func(int x) {
  const int codes[] = {
    0x434d5017, 0, 1, -0x4816cc, 0x13cdcdcd, 0
  };
  int index = x & (sizeof(codes)/sizeof(codes[0]) - 1);
  int secret = codes[index];
  int result = secret * 100;
  return result;
}

int main() {
  int main_result = 0;
  int x = 1;
  int y = 2;
  int z = 3;
  if((x && y) || z) {
    switch_func(x);
  } else {
    main_result = 1;
  }
  printf("%d\n", main_result);
  return main_result;
}
```

