
```cpp
static int my_function(int a, int b) {
  int result = 0;
  if(a % 2 == 0)
    if(b % 2 == 0)
      result = a + b;
    else
      result = a - b;
  else
    if(b % 2 == 0)
      result = a + b;
    else
      result = a * b;
  return result;
}

int main() {
  int x = 10;
  int y = 20;
  int main_result = 0;

  main_result = my_function(x, y);

  return main_result;
}
```

The C++ code ends.