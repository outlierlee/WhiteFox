
```cpp
#include <iostream>
#include <vector>
#include <array>
#include <bitset>
#include <limits>
#include <cfloat>
#include <algorithm>
#include <string>

void example_function() {
  int a = (1 << 31);
  float b = 25.5;
  char c = 'c';
  unsigned int d = 10;
  long i_val = 100000;
  long double ld_val = 10.5;
  std::string mystr = "ACGAT";
  std::vector<int> vec1 = {0, 1, 2, 3, 4, 5};
  std::vector<int> vec2 = {5, 4, 3, 2, 1, 0};
  std::bitset<8> bit_val = 0x3F;
  std::array<int, 4> arr = {1, 2, 3, 4};

  a += 5;
  b *= 2.0;
  c = 'd';
  d = (d << 1);
  i_val = (i_val << 2);
  ld_val = (ld_val * 1.4);
  mystr = "ATCG";
  vec1.assign(6, 42);
  vec2.push_back(50);
  bit_val = mystr[3];
  arr.fill(0);

  std::cout << "a: " << a << ", b: " << b << ", c: " << c << ", d: " << d << ", long: " << i_val << ", ld: " << ld_val << ", str: " << mystr << ", vec: ";
  for (int i : vec1) {
      std::cout << i << " ";
  }
  std::cout << ", bit_val: " << bit_val << std::endl;
}

int main() {

  std::cout << "Calling function...\n";
  example_function();

  return 0;
}
```

# C++ Code Ends