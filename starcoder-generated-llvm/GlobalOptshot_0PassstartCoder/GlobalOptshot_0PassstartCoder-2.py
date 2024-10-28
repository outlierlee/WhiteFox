
```c
static int my_function(int a, int b) {
  int result = 0;
  int i;
  for (i = 0; i < 32; i++) {
    result *= 2;
    result += a ^ b;
  }
  return result;
}

int main() {
  int result = 0;
  int a = 5;
  int b = 10;
  result = my_function(a, b);
  return result;
}
```

