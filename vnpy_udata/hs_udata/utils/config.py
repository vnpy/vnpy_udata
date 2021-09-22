import os
import yaml

from hs_udata.utils.decorators import lru_cache


def load_yml(path):
    with open(path, encoding='utf-8') as pf:
        return yaml.safe_load(pf)


def save_yml(full_path, _yml):
    with open(full_path, encoding='utf-8', mode='w') as pf:
        return yaml.safe_dump(_yml, pf)


@lru_cache(128)
def read_config():
    path = os.path.join(os.path.dirname(__file__), ".", "config.yml")
    return load_yml(path)


def write_config(_config):
    conf = read_config()['system']
    import operator
    if operator.ne(_config, conf):
        path = os.path.join(os.path.dirname(__file__), ".", "config.yml")
        return save_yml(path, _config)
