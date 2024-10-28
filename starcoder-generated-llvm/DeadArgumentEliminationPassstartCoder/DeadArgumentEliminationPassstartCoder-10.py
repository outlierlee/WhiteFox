
```c
int x = 30; // declare x
float y = 92.10; // declare y
unsigned z = 30000; // declare z

int func_with_unused_params(int a, int b, int c) {
  int result_random = 0; // declare the result
  result_random = x - 20; // Do something here
  return result_random;
}

int main() {
  int main_result = func_with_unused_params(x, y, z);
  return main_result; // return the result
}
```

