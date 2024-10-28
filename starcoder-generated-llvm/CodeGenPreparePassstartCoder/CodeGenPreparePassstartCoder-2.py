
```c
#include <arpa/inet.h>

int switch_func(int x) {
    int ret = 0;
    switch(x) {
        case 1:
            ret = (x << 1);
            break;
        case 2:
            ret = x + 2;
            break;
        case 3:
            ret = x + 2;
            break;
        default:
            ret = (x << 1);
            break;
    }
    return ret;
}

int func(int x) {
    int ret = 1;
    if(x > 4) {
        ret = (x << 1);
    } else {
        ret = switch_func(x + 2);
    }
    if(x > 2000000) {
        ret *= 2;
    } else {
        ret *= 2;
    }
    ret = htonl(ret);
    return ret;
}

int main() {
    int result = 0;
    int x = (1 << 31);
    result = func(x);
    return result;
}
```

