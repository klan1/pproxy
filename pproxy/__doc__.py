__title__       = "pproxy"
__license__     = "MIT"
__version__     = "3.0.1"
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
    try:
        from importlib.metadata import PackageNotFoundError, version as _pkg_version
        __version__ = _pkg_version('pproxy')
    except PackageNotFoundError:
        try:
            from importlib_metadata import PackageNotFoundError, version as _pkg_version
            __version__ = _pkg_version('pproxy')
        except Exception:
            __version__ = 'unknown'
    except Exception:
        __version__ = 'unknown'

__all__ = ['__version__', '__description__', '__url__']
