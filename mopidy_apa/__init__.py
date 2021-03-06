import logging
import pathlib

import pkg_resources
from mopidy import config, ext

__version__ = pkg_resources.get_distribution("Mopidy-VFD").version

# TODO: If you need to log, use loggers named after the current Python module
logger = logging.getLogger(__name__)


class Extension(ext.Extension):

    dist_name = "Mopidy-APA"
    ext_name = "apa"
    version = __version__

    def get_default_config(self):
        return config.read(pathlib.Path(__file__).parent / "ext.conf")

    def get_config_schema(self):
        schema = super().get_config_schema()
        schema["amp_delay"] = config.Integer(minimum=10, maximum=1000)
        schema["psu_delay"] = config.Integer(minimum=10, maximum=1000)
        return schema

    def setup(self, registry):
        from .mopidy_client import MopidyClient

        registry.add("frontend", MopidyClient)
