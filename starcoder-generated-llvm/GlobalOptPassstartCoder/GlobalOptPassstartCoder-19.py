
```cpp
#include <vector>

static int my_function(int a, int b)
{
  int result = 0;
  if (a > b)
  {
    result = a - b;
  }
  else
  {
    result = a * b;
  }
  return result;
}

int main()
{
  int main_result = 0;
  int a = (1 << 31);
  std::vector<int> vec = {0, 1, 2, 3};
  for (int i = 0; i < vec.size(); i++)
  {
    main_result += my_function(vec[i], a);
  }
  return main_result;
}
```

