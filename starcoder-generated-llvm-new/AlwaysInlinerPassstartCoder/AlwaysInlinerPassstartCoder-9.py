
```c
inline int inline_func(int a, int b) {
  int sum = 0;
  for(int i = 0; i <= a; ++i){
    sum += i * b;
  }
  return sum;
}

int main() {
  int x = 10;
  int y = 5;
  int result = inline_func(x, y);
  return result;
}
```
