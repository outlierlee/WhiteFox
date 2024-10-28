
```cpp
#include<iostream>

static int unused_function() {
  int result = 0;
  result += 20;
  return result;
}

int main() {
  int a = (1 << 31) + 7;
  int b = (1 << 31) + 11;
  a = a - b;
  int main_result = 0;
  if(a){
    main_result = 100;
  } else {
    main_result = 200;
  }
  return main_result;
}
```

