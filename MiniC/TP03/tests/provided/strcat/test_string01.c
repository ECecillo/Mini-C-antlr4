#include "printlib.h"

int main(){
  string x,y,z;
  x = "ENS";
  y = "De Lyon";
  z = x + " " + y;
  println_string(z);
  return 0;
}

// SKIP TEST EXPECTED
// EXPECTED
// ENS De Lyon

