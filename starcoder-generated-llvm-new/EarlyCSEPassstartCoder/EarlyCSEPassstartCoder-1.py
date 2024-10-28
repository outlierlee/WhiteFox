
```cpp
#include <iostream>

struct Test {
  int value;
  Test(int v) : value(v) {}
};

int main() {
  int a = 5;
  int b = 10;
  int c = 5; 

  int result1 = a + b; 

  Test t1(a + b);
  Test t2(c + b); 

  printf("Result1: %d\n", result1);
  printf("Object t1's value: %d\n", t1.value);
  printf("Object t2's value: %d\n", t2.value);

  return 0;
}
```

