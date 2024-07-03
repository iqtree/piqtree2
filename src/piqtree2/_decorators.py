import os
import sys
from functools import wraps
from typing import Callable, ParamSpec, TypeVar

from piqtree2.exceptions import IqTreeError

Param = ParamSpec("Param")
RetType = TypeVar("RetType")


def iqtree_func(func: Callable[Param, RetType]) -> Callable[Param, RetType]:
    @wraps(func)
    def wrapper_iqtree_func(*args: Param.args, **kwargs: Param.kwargs) -> RetType:
        # Flush stdout and stderr
        sys.stdout.flush()
        sys.stderr.flush()

        # Save original stdout and stderr file descriptors
        original_stdout_fd = os.dup(sys.stdout.fileno())
        original_stderr_fd = os.dup(sys.stderr.fileno())

        # Open /dev/null (or NUL on Windows) as destination for stdout and stderr
        devnull_fd = os.open(os.devnull, os.O_WRONLY)

        try:
            # Replace stdout and stderr with /dev/null
            os.dup2(devnull_fd, sys.stdout.fileno())
            os.dup2(devnull_fd, sys.stderr.fileno())

            # Call the wrapped function
            return func(*args, **kwargs)
        except RuntimeError as e:
            raise IqTreeError(e) from None
        finally:
            # Flush stdout and stderr
            sys.stdout.flush()
            sys.stderr.flush()

            # Restore stdout and stderr
            os.dup2(original_stdout_fd, sys.stdout.fileno())
            os.dup2(original_stderr_fd, sys.stderr.fileno())

            # Close the duplicate file descriptor
            os.close(devnull_fd)

    return wrapper_iqtree_func
