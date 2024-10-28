
```c
void external_func1() {
  global_var1 += 5;
  global_var2 *= global_var2;
}

void external_func2() {
  if (global_var1 > 100) {
    global_var2 -= 1.5;
  } else {
    global_var2 += 1.5;
  }
}

int main() {
  global_var1 += 20;
  external_func1();
  external_func2();
  return global_var1;
}
```

The C++ code ends.

