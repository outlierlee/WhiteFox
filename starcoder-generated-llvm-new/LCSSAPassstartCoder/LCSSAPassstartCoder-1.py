```cpp
#include <unordered_map>
#include <vector>
#include <iostream>

using namespace std;

int main() {
    int result = 0;

    int size = 10;
    unordered_map<int, vector<int>> map;
    vector<int> vec = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    vector<int> vecCopy(vec);

    for(int i = 0; i < vec.size(); i++){
        for(int j = i + 1; j < vec.size(); j++){
            map.insert(make_pair(vec[j], vecCopy));
        }
    }

    auto it = map.begin();
    for (; it != map.end(); ++it){
        if (it->second == vec){
            result += it->first;
        }
    }

    cout << "Result is: " << result << endl;

    return 0;
}
```

