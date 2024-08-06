
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
