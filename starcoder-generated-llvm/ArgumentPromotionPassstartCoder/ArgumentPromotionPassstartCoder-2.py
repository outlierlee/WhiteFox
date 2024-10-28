
```c
#include <arpa/inet.h>

static void no_stdlib_func(int *a, double *b) {
    if(a && b && a != NULL && b != NULL) {
        (*a)++;
        (*b) /= 2.0f;
    }
    if(a && a != NULL) (*a)++;
    if(b && b != NULL) (*b) *= 2.0f;
}

static void attr_const_func(const char *c) {
    printf("%s", c);
}

int main() {
    int a = 56;
    double b = 7.0;

    no_stdlib_func(&a, &b);

    int network_order = htonl(a);
    int host_order = ntohl((a > 99 ? 1 : 0));

    char text[50] = "no musttail attributed functions as well";
    attr_const_func(text);

    return network_order + host_order;
}
```

