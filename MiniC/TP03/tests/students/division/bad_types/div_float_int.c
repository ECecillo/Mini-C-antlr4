#include "printlib.h"

int main()
{
  float x;
  int y;
  float res; // In python int / float is float.

  x = 2.0;
  y = 4;

  res = x / y; // Should raise an error because type mismatch.
  return 0;
}

// EXITCODE 2
// EXPECTED
// In function main: Line 12 col 8: invalid type for multiplicative operands: float and integer
