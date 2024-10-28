
```c++
#include <cstring>
#include <random>
#include <vector>

int main() {
  int a = 10;
  int b = 12;
  const int const_array[] = {10, 20, 30, 40, 50};
  int local_array[5];
  std::memcpy(local_array, const_array, sizeof(const_array));
  std::vector<int> vec(5, local_array[0]);
  std::random_device rd;
  std::default_random_engine gen(rd());
  std::uniform_int_distribution<int> dis(-5, 5);
  int result = local_array[dis(gen) + 2];
  result *= 2;
  return result;
}
```

