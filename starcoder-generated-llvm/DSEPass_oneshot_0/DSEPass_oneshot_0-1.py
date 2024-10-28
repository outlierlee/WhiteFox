
```cpp
static int func(int x) {
  int result = x;
  if (x > 10) {
    result = 0;
  } else {
    result = 100;
  }
  return result;
}

int main() {
  int* p = new int; // allocate memory
  *p = 10; // store a value
  int a = func(*p);
  *p = 20; // overwrite the value
  int b = func(*p);
  delete p; // deallocate memory
  return a + b;
}
```

