#include "printlib.h"

int main()
{
  bool False, True;
  False = false;
  True = true;

  println_bool(False);
  println_bool(True);

  return 0;
}

// EXPECTED
// 0
// 1
