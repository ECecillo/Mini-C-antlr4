#include "printlib.h"

int main()
{
  bool shouldTurnTrue;
  shouldTurnTrue = false;

  println_bool(!shouldTurnTrue);
  return 0;
}

// EXPECTED
// 1
