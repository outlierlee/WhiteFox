
```cpp
#include <iostream>
#include <vector>

class BaseClass {
public:
    BaseClass(int x) { this->x = x; }
    int getX() { return this->x; }
private:
    int x;
};

class DerivedClass : public BaseClass {
public:
    DerivedClass(int x) : BaseClass(x) { this->x = x; this->y = x*x; }
    int getY() { return this->y; }
private:
    int x, y;
};

void reference_func(std::vector<BaseClass>& vec, std::vector<DerivedClass>& d_vec) {
    for (int i = 0; i < vec.size(); ++i) {
        vec[i].getX();
        d_vec[i].getY();
    }
}

int main() {
    std::vector<BaseClass> vec(10, BaseClass(10));
    std::vector<DerivedClass> d_vec(10, DerivedClass(10));
    reference_func(vec, d_vec);
    return 0;
}
```

