
```cpp
static int unused_function() {
  int result = 0;
  result += 1;
  return result;
}

int main() {
  int main_result = 0;
  unused_function();
  main_result += 2;
  return main_result;
}
```
