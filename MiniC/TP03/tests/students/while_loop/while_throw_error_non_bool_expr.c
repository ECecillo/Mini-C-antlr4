#include "printlib.h"

int main()
{
  int i;
  i = 0;

  while (i)
  {
    println_int(i);
    i = i + 1;
  }

  return 0;
}

// EXPECTED
// In function main: Line 8 col 2: invalid type for while condition: integer
// EXITCODE 2
