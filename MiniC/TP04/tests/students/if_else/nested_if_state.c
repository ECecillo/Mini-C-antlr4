#include "printlib.h"

int main()
{
  bool shouldTurnTrue;
  int block_true_value, block_false_value, nested_block_true_value, nested_block_false_value;
  block_true_value = 42;
  block_false_value = 0;
  nested_block_false_value = 10;
  nested_block_true_value = 20;
  shouldTurnTrue = false;

  if (shouldTurnTrue)
  {
    println_int(block_true_value);
  }
  else
  {
    println_int(block_false_value);
  }

  if (!shouldTurnTrue)
  {
    if (!shouldTurnTrue)
    {
      println_int(nested_block_true_value);
    }
    else
    {
      println_int(nested_block_false_value);
    }
  }

  return 0;
}

// EXPECTED
// 0
// 20
