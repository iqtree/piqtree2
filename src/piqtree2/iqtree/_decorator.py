"""Decorators for IQ-TREE functions."""

import os
import pathlib
import sys
import tempfile
from functools import wraps
from typing import Callable, Optional, TypeVar

from typing_extensions import ParamSpec

from piqtree2.exceptions import IqTreeError

Param = ParamSpec("Param")
RetType = TypeVar("RetType")


def iqtree_func(
    func: Callable[Param, RetType],
    *,
    hide_files: Optional[bool] = False,
) -> Callable[Param, RetType]:
    """IQ-TREE function wrapper.

    Hides stdout and stderr, as well as any output files.

    Parameters
    ----------
    func : Callable[Param, RetType]
        The IQ-TREE library function.
    hide_files : Optional[bool], optional
        Whether hiding output files is necessary, by default False.

    Returns
    -------
    Callable[Param, RetType]
        The wrappe IQ-TREE function.

    Raises
    ------
    IqTreeError
        An error from the IQ-TREE library.

    """

    @wraps(func)
    def wrapper_iqtree_func(*args: Param.args, **kwargs: Param.kwargs) -> RetType:
        # Flush stdout and stderr
        sys.stdout.flush()
        sys.stderr.flush()

        old_out = sys.stdout
        old_err = sys.stderr

        # Open /dev/null (or NUL on Windows) as destination for stdout and stderr
        devnull = open(os.devnull, "w")

        if hide_files:
            original_dir = pathlib.Path.cwd()
            tempdir = tempfile.TemporaryDirectory(prefix=f"piqtree_{func.__name__}")
            os.chdir(tempdir.name)

        try:
            # Replace stdout and stderr with /dev/null
            sys.stdout = devnull
            sys.stderr = devnull

            # Call the wrapped function
            return func(*args, **kwargs)
        except RuntimeError as e:
            raise IqTreeError(e) from None
        finally:
            # Flush stdout and stderr
            sys.stdout.flush()
            sys.stderr.flush()

            # Restore stdout and stderr
            sys.stdout = old_out
            sys.stderr = old_err

            # Close devnull
            devnull.close()

            if hide_files:
                tempdir.cleanup()
                os.chdir(original_dir)

    return wrapper_iqtree_func
