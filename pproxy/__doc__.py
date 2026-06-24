__title__       = "pproxy"
__license__     = "MIT"
__version__     = "3.0.3"
__description__ = "Proxy server that can tunnel among remote servers by regex rules."
__keywords__    = "proxy socks http shadowsocks shadowsocksr ssr redirect pf tunnel cipher ssl udp"
__author__      = "Qian Wenjie"
__email__       = "qianwenjie@gmail.com"
__url__         = "https://github.com/qwj/python-proxy"

try:
    from setuptools_scm import get_version
    __version__ = get_version()
except Exception:
    # Python 3.8+ has importlib.metadata as the standard way to look up an
    # installed distribution's version. This avoids the pkg_resources
    # deprecation warning emitted by setuptools>=81.
    #
    # We try both possible distribution names: 'klan1-pproxy' (this fork,
    # what gets installed via `pip install klan1-pproxy`) and 'pproxy'
    # (the upstream distribution, in case someone installed the original
    # package or our fork under its module name).
    def _lookup_version(dist_name):
        """Return the installed version of dist_name, or None."""
        # importlib.metadata is stdlib in 3.8+; importlib_metadata is the
        # backport for 3.7 and earlier (we still support it for the rare
        # 3.7 user who installed the fork before the py3.12-compat work).
        for importer in ('importlib.metadata', 'importlib_metadata'):
            try:
                mod = __import__(importer, fromlist=['version', 'PackageNotFoundError'])
                return mod.version(dist_name)
            except Exception:
                continue
        return None

    __version__ = 'unknown'
    for _dist_name in ('klan1-pproxy', 'pproxy'):
        _v = _lookup_version(_dist_name)
        if _v is not None:
            __version__ = _v
            break

__all__ = ['__version__', '__description__', '__url__']
