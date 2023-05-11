#include "printlib.h"

int main()
{
  int i, compteur;
  for (i = 0; ; i++)
  {
    if (compteur == 1000)
    {
      println_int(1/0);
    }
    compteur++;
  }
  return 0;
}
// EXECCODE 1
// SKIP TEST EXPECTED
// EXPECTED
// Division by 0
