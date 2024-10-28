
```cpp
#include <vector>
#include <string>

void __attribute__((noinline)) func(int a, float b, std::vector<int> c, std::string str) {
    a += 15;
    b *= 2.31;
    for(auto& it : c){
        it -= 2;
    }
    str += "world";
}

int main(){
    int x = 100;
    float y = 15.67;
     std::vector<int> vec = {1, 2, 3};
     std::string str = "hello";
     func(x, y, vec, str);
     return 0;
}
```

