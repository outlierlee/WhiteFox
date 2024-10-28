
```c
int x = 1;
char y = 'a';
double z = 1.23;

int func_with_unused_params(int a, int b, int c) {
  int result = 0;
  result = x * 2;
  return result;
}

int main() {
  int main_result = 0;
  main_result = func_with_unused_params(x, y, z);
  return main_result;
}
```

