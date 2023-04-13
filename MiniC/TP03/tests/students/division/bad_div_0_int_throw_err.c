#include "printlib.h"

int main()
{
  int x, should_not_be_print;
  should_not_be_print = 5;
  x = 10 / 0;

  should_not_be_print = 1;
  println_int(should_not_be_print);
  return 0;
}

// EXECCODE 1
// SKIP TEST EXPECTED
// EXPECTED
// Division by 0
