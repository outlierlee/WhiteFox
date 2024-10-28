#include <stdatomic.h>

// declare variables
atomic_int atomic_var = ANY_VALUE; // declare an atomic integer variable
int non_atomic_var = ANY_VALUE; // declare a non-atomic integer variable

int main() {
  // perform an atomic read-modify-write operation
  int old_value = atomic_fetch_add(&atomic_var, non_atomic_var);

  // use the result of the atomic operation
  int result = old_value OPERATOR ANY_VALUE;

  return result; // return the result
}
