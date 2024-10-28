
```cpp
static int global_var = 1024;

static int modify_global_var(int val) {
  global_var = val;
  return global_var;
}

int main() {
  int result = 0;
  int value = (1 << 20);
  result = modify_global_var(value);
  return result;
}
```
