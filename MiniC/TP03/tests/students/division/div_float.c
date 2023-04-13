#include "printlib.h"

int main()
{
  float x;
  x = 2.0 / 10.0;

  println_float(x);

  return 0;
}

// EXPECTED
// 0.20
