
```cpp
int main() {
  std::string str = "hello";
  str.push_back(' ');
  std::string name = "world";
  std::map<int, std::string> map;
  map[10] = name;
  map[20] = name;
  for (auto &pair : map) {
    str += pair.second;
  }
  int x = 10;
  return x & 4;
}
```
