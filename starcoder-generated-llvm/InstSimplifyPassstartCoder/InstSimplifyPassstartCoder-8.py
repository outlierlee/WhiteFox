
```cpp
int main() {
  int result = 0; // declare the result

  // sum array
  int array[100];
  for (int i = 0; i < 100; i++) {
    array[i] = i;
  }

  int sums[100];
  sums[0] = array[0];
  for (int i = 1; i < 100; i++) {
    sums[i] = sums[i - 1] + array[i];
  }

  if (sums[99] > 5000) {
    result = 5000; // avoid extra checks
  } else {
    result = sums[sums[99]]; // redundant access to sums[99]
  }

  printf("Result: %d\n", result);

  return result;
}
```
