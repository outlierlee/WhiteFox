
```c
#include <stdio.h>
void loop_with_condition(int n, int flag) {
  for(int i=0,sum=0;i<n;i++) {
    if (flag%3) {
      sum += i*2;
    } else {
      sum -= i;
    }
  }
}

int main() {
  loop_with_condition(15, 10);
  return 0;
}
```

