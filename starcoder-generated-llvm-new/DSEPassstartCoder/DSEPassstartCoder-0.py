
```cpp
#include <vector>
#include <string>

int main() {
  std::vector<char> vec(100);
  std::vector<char> vec1(100);

  // Assign values to vec
  for (int i = 0; i < 100; i++) {
    vec[i] = (char)i;
  }

  // Assign values to vec1
  for (int i = 0; i < 100; i++) {
    vec1[i] = (char)(i + 100);
  }

  for (int i : vec){
    vec[i % 5] = vec1[i % 5];
  }
  int sum = vec[0];
  return sum;
}
```

