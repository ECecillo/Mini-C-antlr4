#include "printlib.h"

int main()
{
  float x, should_not_throw_err;
  x = 2.0 / 0.0;

  should_not_throw_err = 1.0;
  println_float(should_not_throw_err);
  return 0;
}

// EXECCODE 1
// SKIP TEST EXPECTED
// EXPECTED
// Division by 0
