```
int main() {
  // Declare and initialize a constant array
  const int const_array[] = {1, 2, 3, 4, 5};

  // Declare a local array with automatic storage duration
  int local_array[5];

  // Use memcpy to copy data from the constant array to the local array
  int size_of_array = sizeof(const_array) / sizeof(int);
  for(int i = 0; i < size_of_array; i++) {
      local_array[i] = const_array[i];
  }

  // Use the local array in some way to ensure it is not optimized away
  int result = local_array[1] + local_array[2];

  return result;
}
```
