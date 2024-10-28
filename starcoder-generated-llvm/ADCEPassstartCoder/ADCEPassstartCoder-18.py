
```cpp
#include<iostream>

int a = 10;
double b = 20.5;

int compute(int x, int y) {
  int result = x + y;
  return result;
}

void compute1(int x, int y) {
  int result = x + y;
}

int main() {
  int main_result = 0;
  
  double c = a + b;
  
  main_result = compute(a, b);
  
  std::cout << "Result: " << main_result << "\n";
  
  return 0;
}
```

The significant change in this version is that c is a double type, even though a + b (the dead computation) results in an integer value.

