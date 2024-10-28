
```cpp
#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>

void quicksort(std::vector<int>& nums, int begin, int end) {
  if (begin < end) {
    int pivot = nums[begin];
    int i = begin + 1;
    int j = end;
    while(i <= j) {
      while(i <= j && nums[i] <= pivot) ++i;
      while(i <= j && nums[j] > pivot) --j;
      if (i < j) {
        std::swap(nums[i], nums[j]);
      }
    }
    std::swap(nums[begin], nums[j]);

    quicksort(nums, begin, j - 1);
    quicksort(nums, j + 1, end);
  }
}

int main() {
  srand(static_cast<unsigned int>(time(nullptr)));
  std::vector<int> v(1<<16);
  for (int i = 0; i < v.size(); ++i) {
    v[i] = rand();
  }
  quicksort(v, 0, v.size() - 1);
  for (int i = 1; i < v.size(); ++i) {
    if (v[i - 1] > v[i]) {
      std::cout << "Failed" << std::endl;
      return i;
    }
  }
  return 0;
}
```

