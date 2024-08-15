
<a id='changelog-0.3.0'></a>
# Changes in release "0.3.0"

## Contributors

- @rmcar17 Added new classes to enhance model specification when calling `build_tree` and `fit_tree`.
- @thomaskf fixed a bug in IQ-TREE resulting in segmentation faults on some invalid arguments.

## ENH

- `build_tree` and `fit_tree` now allow specifying base frequencies, invariable sites and rate heterogeneity options.

## BUG

- Fixed a segmentation fault on repetitive calls to IQ-TREE with particular arguments.

<a id='changelog-0.2.0'></a>
# Changes in release "0.2.0"

## Contributors

- Richard Morris
- Robert McArthur

## ENH

- `build_tree` and `fit_tree` now use enums for the substitution model.

## BUG

- Fixed an issue where calling `build_tree` or `fit_tree` twice, then another function with invalid input resulted in a segmentation fault.

## DOC

- Implement scriv as a tool to manage collection of changes, and automated collation into the changelog
