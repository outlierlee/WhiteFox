
```cpp
#include <vector>
#include <string>

static int unused_function() {
  int result = 0;
  if (result) {
    result = result + 10;
  } else {
    result = result - 10;
  }
  return result;
}

int main() {
  int result = 0;
  int arr[10] = {0};
  std::vector<int> v(arr, arr + 10);
  std::string str = "hello";
  result = v[2] + v[3] + v[4] + str[1] + str[2] + str[3];
  return result;
}
```

