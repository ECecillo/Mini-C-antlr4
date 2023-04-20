#include "printlib.h"

int main()
{
  if (42 > 30)
  {
    println_int(42);
  }
  else
  {
    println_int(30);
  }

  return 0;
}

// EXPECTED
// 42
