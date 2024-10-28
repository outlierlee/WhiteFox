
```cpp
int main() {
  int main_result = 0; // declare the result
  if(false){
    main_result = unused_function(); // call unused_function(), will be removed
  }
  if(true){
    int a = 1234;
    int b = a * 2345;
    main_result = b * 3456;
  }
  return main_result;
}
```
