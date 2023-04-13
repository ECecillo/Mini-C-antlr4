#include "printlib.h"

int main()
{
  int x;
  float y;
  float res; // In python int / float is float.

  x = 2;
  y = 4.0;

  res = x / y; // Should raise an error because type mismatch.
  return 0;
}

// EXITCODE 2
// EXPECTED
// In function main: Line 12 col 8: invalid type for multiplicative operands: integer and float
