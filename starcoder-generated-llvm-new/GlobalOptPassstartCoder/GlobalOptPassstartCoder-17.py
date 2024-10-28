
```c
#include <string.h>

static int my_function(int a, int b) {
  int result = 0;

  if (a % 2) {
    result = a * 32 + 15;
  } else {
    result = a / b;
  }

  if (a > b) {
    result = result * 2;
  } else {
    result = -result;
  }

  return result;
}

int main() {
  int i, j, a = (1 << 31), b = sizeof(__int64_t);
  char str[10] = "hello";
  int main_result = 0;

  for (i = 0; i < 5; i++) {
    for (j = 1; j <= i; j++) {
      main_result += my_function(i, j);
    }
  }

  memset(str, 'A', sizeof(str));

  return main_result;
}
```

