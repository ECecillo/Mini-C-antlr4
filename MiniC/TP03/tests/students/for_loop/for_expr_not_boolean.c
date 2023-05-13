#include "printlib.h"

int main()
{
  int i;
  for (i = 0; "hello there"; i = i + 1)
  {
    println_int(i);
  }
  return 0;
}

// EXPECTED
// EXITCODE 2
// In function main: Line 6 col 2: invalid type for for condition: string
