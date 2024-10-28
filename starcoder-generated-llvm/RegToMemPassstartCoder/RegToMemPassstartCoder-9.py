
```c
void local_variable_func() {
  int x = 10;
  float y = 5.0;
  char z = 'z';

  for (int i = 0; i < 10; i++) {
    x += i;
  }

  y += x;
  z++;
  printf("%d %.2f %c\n", x, y, z);
}

int main() {
  local_variable_func();
  return 0;
}
```
