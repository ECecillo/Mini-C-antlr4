#include "printlib.h"

int main()
{
  int a;
  a = 1;
  println_int(-(-(-a)));
  println_int(-(-(-(-a))));
  return 0;
}

// EXPECTED
// -1
// 1
