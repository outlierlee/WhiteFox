#include <math.h>

int main() {
  // Declare and initialize floating-point variables
  float a = ANY_FLOAT_VALUE; // e.g., 1.5f
  float b = ANY_FLOAT_VALUE; // e.g., 2.5f
  float c = ANY_FLOAT_VALUE; // e.g., 3.5f

  // Perform a floating-point multiplication operation
  // that involves a constant and a variable
  float result = (a / b) * c; // This pattern can trigger the optimization

  // Return the result as an integer
  return (int)result;
}
