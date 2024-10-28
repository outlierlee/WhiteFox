
```cpp
#include <iostream>

void example_function() {
  int integer = 10;
  float myFloat = 10.0f;
  char myChar = 'c';

  integer += 1;
  myFloat += 1.0;
  myChar = 'd';
  
  std::cout << "Integer: " << integer << ", Float: " << myFloat << ", Char: " << myChar << std::endl;
}

int main() {
  example_function();
  return 0;
}
```
