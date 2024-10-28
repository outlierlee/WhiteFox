
```c
#include <stdio.h>

int x = -2147483648; // this <<30 gives garbled output due to type promotion, rather than a warning about size, so for int it this would not cause a warning, while for long it would.
char y = 0x7F; // biggest char value + 1, this will make it wrap around to smallest char value

int main() {
  double result = (double) x <<31 | (double) y >> 2; // evaluation after truncation/extension, so this just shifts it by 31 bits cause of -2147483648 on 32 bit unsigned, and double expects a number as higher range
  printf("%lf\n", result); 
  return 0;
}
```

