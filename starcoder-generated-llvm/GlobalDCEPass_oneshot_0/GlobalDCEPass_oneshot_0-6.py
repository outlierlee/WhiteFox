
```cpp
#include <iostream>
#include <vector>
#include <string>

void unused_func() {
  int j = 1;
  std::vector<int> vec;
  std::string str = "hello";
  
  for(int i=0; i<10; i++)
    vec.push_back(i+j);

  const int N = 10;
  int arr[N];

  for(int i = 0; i < N; ++i)
    arr[i] = vec[i % vec.size()];

  for(int i = 0; i < N; ++i) 
    std::cout << arr[i] << ' ';
  
  std::cout << '\n';
}

int main() {
  std::cout << "Test: unused function\n";
  unused_func(); // calling unused function
  return 0; 
}
```
