
```cpp
#include <iostream>
#include <vector>

struct X {
    X(int val) :value(val) {}
    operator int() const { return value; }
    int value;
};

struct A {
    A(int val) :value(val) {}
    operator int() const {
        return value;
    }
    int value;

    // dummy function for getting non zero value
    int getNonZeroValue() const {return value;}
};

int main() {
    std::vector<X> xvec;
    std::vector<A> avec;
    int phi = 0;

    xvec.emplace_back(1);
    avec.emplace_back(xvec[0].getNonZeroValue());

    A a(1);

    for (int i = 0; i < 10; ++i) {
        if (i % 2 == 0) {
            phi = avec[0].getNonZeroValue();
        } else {
            phi = 0;
        }

        if (phi) {
            std::cout << "Phi is Non-Zero" << std::endl;
        } else {
            std::cout << "Phi is Zero" << std::endl;
        }
    }
    return 0;
}
```

