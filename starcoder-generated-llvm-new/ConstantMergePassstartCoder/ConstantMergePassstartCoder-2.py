```
#include <bitset>
#include <cstdio>

const int global_const1 = 42;
const int global_const2 = 42;

int use_globals() { return global_const1 + global_const2; }

int add(int x, int y) { return x + y; }

int bitwise_and(int x, int y) {
  return x & y;
}

int main() {
  int result = add(100, -42);
  result = bitwise_and(result, use_globals());
  printf("Result: %d\n", result);
  return 0;
}
```

