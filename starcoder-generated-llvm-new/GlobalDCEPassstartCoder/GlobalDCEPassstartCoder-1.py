
```c
static int unused_function() {
  int result = 0;
  if (1 > (2 * 3)) {
    result = result * 2 + 1;
  } else {
    result = result * 3;
  }
  while (result < (150 / 2)) {
    result = result + 100;
  }
  if ((result += 2) > (100 - 5)) {
    result--;
  } else {
    result++;
  }
  return result;
}

int main() {
  int main_result = 0;
  int unused_var = 42;
  if (unused_var % 3) {
    main_result = unused_var * 2;
  }
  // main function does not call unused_function
  if (main_result > 0) {
    main_result--;
  } else {
    main_result++;
  }
  return main_result;
}
```

