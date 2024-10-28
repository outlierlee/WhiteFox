
```c
int main() {
  int x = 1000;
  int y = 2500;
  int z = 4000;

  int func_with_unused_params(int a, int b, int c) {
    int result = 0;
    return 1500;
  }
  
  int main_result = func_with_unused_params(x, y, z);
  return main_result;
}
```

