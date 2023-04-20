#include "printlib.h"

int main()
{
  int a;
  a = 42 % 0;

  println_int(a);
  return 0;
}

// SKIP TEST EXPECTED
// EXECCODE 1
// EXPECTED
// Division by 0
