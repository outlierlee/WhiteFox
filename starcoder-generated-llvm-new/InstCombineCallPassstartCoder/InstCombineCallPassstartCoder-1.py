
```c
#include <stdio.h>
#include <string.h>

const int len = 10;
const char hello[] = "hello,world!";
int pair[2];

// A function that will be transformed by the optimizer to end up calling `pair_split`
void example_func() {
  memcpy(pair, "aaa", sizeof(int)*2);
  // Would normally call `pair_split` function here e.g. pair_split(pair);
}

int main() {
  pair[0] = 1;
  pair[1] = 2;
  hello[5] = 'a';
  printf("%s\n", "Hello, World!");
  example_func();
  printf("%d\n", pair[1]);
  return 0;
}
```

