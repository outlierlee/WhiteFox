
```c
__attribute__((noinline)) 
static int my_function(int a, int b) {
  int result = (a * 2) + (b * 3);
  if (a > b) {
    result += a + b;
  } else {
    result -= a - b;
  }
  if (a > b) {
    result *= 2;
  } else {
    result /= 2;
  }
  return result;
}

extern int printf(const char *, ...);

int main() {
  int result = 0;
  printf("%d\n", my_function(10, 5));
  return result;
}
```

