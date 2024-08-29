
<a id='changelog-0.3.1'></a>
# Changes in release "0.3.1"

## ENH

- Add support for Lie Markov Models.
- Base frequencies default to None (specified by model).

## BUG

- `piqtree2` apps are now pickleable (they can now be run with `parallel=True` in the cogent3 app infrastructure)

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
