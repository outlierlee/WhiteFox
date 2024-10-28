
```cpp
#include <vector>
#include <string>
#include <cmath>

static inline double sqrtFunc(double x) {
  return sqrt(x);
}

int main() {
  double x = 16.0;
  double y = sqrtFunc(x);
  return static_cast<int>(y);
}
```

