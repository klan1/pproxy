from setuptools import setup
import os, re

def read(*names, **kwargs):
    with open(os.path.join(os.path.dirname(__file__), *names), encoding='utf8') as fp:
        return fp.read()

def find_value(name):
    data_file = read('pproxy', '__doc__.py')
    data_match = re.search(r"^__%s__ += ['\"]([^'\"]*)['\"]" % name, data_file, re.M)
    if data_match:
        return data_match.group(1)
    raise RuntimeError(f"Unable to find '{name}' string.")

def resolve_version():
    """Return the package version.

    Order of preference:
      1. env var PPROXY_VERSION (used by CI/release scripts)
      2. the most recent git tag (via setuptools_scm) when run from a git checkout
      3. the explicit __version__ string in pproxy/__doc__.py (which we
         hardcode below as a deliberate last-resort fallback)
    """
    env_v = os.environ.get("PPROXY_VERSION")
    if env_v:
        return env_v
    try:
        from setuptools_scm import get_version
        return get_version()
    except Exception:
        return find_value('version')

setup(
    name                = "klan1-pproxy",
    version             = resolve_version(),
    description         = "klan1/pproxy fork: HTTP/SOCKS4/SOCKS5/Shadowsocks tunnel proxy, Python 3.9+ compatible.",
    long_description    = read('README.rst'),
    long_description_content_type = "text/x-rst",
    url                 = "https://github.com/klan1/pproxy",
    author              = "Alejandro Trujillo J.",
    author_email        = "alejo@klan1.com",
    license             = find_value('license'),
    python_requires     = '>=3.9',
    keywords            = find_value('keywords'),
    packages            = ['pproxy'],
    classifiers         = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
    extras_require      = {
        'accelerated': [
            'pycryptodome >= 3.7.2',
            'uvloop >= 0.13.0'
        ],
        'sshtunnel': [
            'asyncssh >= 2.5.0',
        ],
        'quic': [
            'aioquic >= 0.9.7',
        ],
        'daemon': [
            'python-daemon >= 2.2.3',
        ],
    },
    install_requires    = [],
    entry_points        = {
        'console_scripts': [
            'pproxy = pproxy.server:main',
        ],
    },
)
