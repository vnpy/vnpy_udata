import warnings
import importlib
import pkgutil

__version__ = '0.0.3'


def _init():
    for loader, module_name, is_pkg in pkgutil.walk_packages(__path__, "hs_udata."):
        if module_name.startswith("hs_udata.apis") and not is_pkg:
            try:
                api_module = importlib.import_module(module_name)
            except ImportError as ex:
                warnings.warn("import module[{}] error, msg={}".format(module_name, ex))

            for api_name in api_module.__all__:
                try:
                    api = getattr(api_module, api_name)
                    globals()[api_name] = api
                except AttributeError as ex:
                    warnings.warn("load api[{}] error, msg={}".format(api_name, ex))

_init()

del _init

def set_token(token=None):
    from hs_udata.utils.client import init
    init(username="license", password=token)