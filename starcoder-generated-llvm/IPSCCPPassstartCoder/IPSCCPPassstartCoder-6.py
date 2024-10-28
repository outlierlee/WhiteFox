
```c
static int global_var = 1024;

static int use_global_var() {
  return global_var;
}

int main() {
  int result = use_global_var();
  return result;
}
```

