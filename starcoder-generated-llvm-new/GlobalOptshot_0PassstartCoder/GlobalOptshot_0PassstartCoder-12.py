
```c
static __attribute__((fastcall)) int my_function(int a, int b) {
  return a + b;
}

int main() {
  int result = 0;
  result = my_function(5, 10);
  return result;
}
```
