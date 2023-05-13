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
// for condition must be a boolean expression
