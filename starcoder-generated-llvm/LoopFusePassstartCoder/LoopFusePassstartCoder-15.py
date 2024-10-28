
```cpp
#include <cstdio>
#include <vector>
#include <string>

int main() {
  int i, j;
  std::vector<int> array1(10, 0), array2(10, 0), result(10, 0);

  for (i = 0; i < 10; i++) {
    array1[i] = i;
    array2[i] = i * 2;
  }

  for (i = 0; i < 10; i++) {
    array1[i] += 1;
    array2[i] += 2;
  }

  for (i = 0; i < 10; i++) {
    result[i] = array1[i] + array2[i];
  }

  for (i = 0; i < 10; i++) {
    std::printf("%d ", result[i]);
  }

  return 0;
}
```