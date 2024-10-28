
```cpp
int main(){
    int *p = new int;
    int ans = 0;
    if(1) {
      *p = 10;
      ans = *p;
      *p = 20;
      ans = *p;
    }
    delete p;
    if(*p == 20)
        ans = *p;
    return ans;
}
```
