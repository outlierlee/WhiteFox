
```c
int x = 10;
char y = 'a';
int z = 5;

int func_with_unused_params(int unused1, int unused2, int unused3) {
  int result = x - z;
  result *= y;
  return result;
}

int main() {
  int main_result = 0;
  main_result = func_with_unused_params(x, y, z);
  return main_result;
}
```

