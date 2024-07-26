"""Collections of envs.

Each collection is a list of envs.
"""

import importlib
from inspect import getmembers, isclass, isfunction


def _collection_from_file(fname):
    """Return list of envs from file."""
    lib = "neurogym.envs.collections." + fname
    if fname == "yang19":
        envs = [
            "go",
            "rtgo",
            "dlygo",
            "anti",
            "rtanti",
            "dlyanti",
            "dm1",
            "dm2",
            "ctxdm1",
            "ctxdm2",
            "multidm",
            "dlydm1",
            "dlydm2",
            "ctxdlydm1",
            "ctxdlydm2",
            "multidlydm",
            "dms",
            "dnms",
            "dmc",
            "dnmc",
        ]
    else:
        module = importlib.import_module(lib)
        envs = [name for name, val in getmembers(module) if isfunction(val)]
        envs = sorted(envs)
        envs = [env for env in envs if env[0] != "_"]

    return [fname + "." + env + "-v0" for env in envs]


def get_collection(collection):
    if collection == "":
        return []  # placeholder for named collections
    else:
        try:
            return _collection_from_file(collection)
        except ImportError:
            msg = f"Unknown collection of envs, {collection}"
            raise ValueError(msg)
