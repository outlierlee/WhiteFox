
```cpp
int main() {
  int result = 0;
  int a = 10;
  int b = 20;
  int c = 30;

  for (int i = 0; i < 10; i++) {
    if (a < b) {
      result += a;
    } else {
      result += b;
    }
  }

  if (result > c) {
    printf("Result is greater than c\n");
  } else {
    printf("Result is less than or equal to c\n");
  }

  return result;
}
```

# C++ code ends