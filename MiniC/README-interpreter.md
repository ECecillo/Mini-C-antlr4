# MiniC interpreter and typer

LAB3, MIF08 / CAP / CS444 2022-23

# Authors

CECILLON Enzo | p1805901

# Contents

- [X] Set default value given variable type.
  - Check if variable already defined in `_memory` array, if so throw an error.

- [X] Handle division errors
  - throwMiniCRuntime Error when dividing by 0.0 (float):
    > Division by 0
    - But don't stop on `raise MiniCRuntimeError`.
    - Check that we don't divide 2 variable with different types.

- [X] Handle Modulo operation:
  - throw MiniCRuntimeError when modulo is 0 or 0.0:
    > Modulo by 0
    use SKIP TEST ESPECTED to ignore gcc evaluation.
  - Compute operation.

- [X] Handle `if` and `else` block
  - Recursively if we have nested blocks

- [X] Handle `while` operation

# Howto

`make test-interpret TEST_FILES='TP03/tests/provided/examples/test_print_int.c'` for a single run

`make test` to test all the files in `*/tests/*` according to `EXPECTED` results.

You can select the files you want to test by using `make test TEST_FILES='TP03/**/*bad*.c'` (`**` means
"any number of possibly nested directories").

# Test design

Every test are sorted by their feature and tests that begin with `bad` should throw some runtime error with a message.

# Design choices


# Known bugs
