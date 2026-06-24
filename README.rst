klan1-pproxy
============

A maintained fork of `pproxy <https://github.com/qwj/python-proxy>`_
(HTTP/SOCKS4/SOCKS5/Shadowsocks/ShadowsocksR/Redirect/PF/QUIC async
tunnel proxy) with two changes:

1. **Python 3.12+ compatibility.** Replaces ``asyncio.get_event_loop()``
   (which raises ``RuntimeError`` on Python 3.12+ when no loop is
   running) with ``asyncio.get_running_loop()`` plus a small fallback
   helper. Works on Python 3.9, 3.10, 3.11, 3.12 and 3.13.
2. **Dropped Python 3.6/3.7 support.** Both are end-of-life.

The original library was last released as ``pproxy 2.7.9`` two years
ago. This fork keeps the same protocol surface and CLI; it only fixes
the runtime crash on modern Python. See ``CHANGELOG.md`` for the
detailed change list and the upstream commit history for everything
else.

QuickStart
----------

.. code:: bash

   $ pip3 install klan1-pproxy
   $ pproxy
   Serving on :8080 by http,socks4,socks5
   ^C

Or pin to a specific version:

.. code:: bash

   $ pip3 install 'klan1-pproxy==3.0.0'

Supported protocols
-------------------

* HTTP, HTTP2, HTTP3
* SOCKS4, SOCKS4a, SOCKS5
* Shadowsocks, ShadowsocksR
* SSH tunnel (with the ``sshtunnel`` extra)
* PF (port-forwarding)
* QUIC (with the ``quic`` extra)
* TCP and UDP

CLI options
-----------

::

   usage: __main__.py [-h] [-l LISTEN] [-r RSERVER] [-ul ULISTEN] [-ur URSERVER]
                      [-b BLOCK] [-a ALIVED] [-s {fa,rr,rc,lc}] [-d] [-v]
                      [--ssl SSLFILE] [--pac PAC] [--get GETS] [--auth AUTHTIME]
                      [--sys] [--reuse] [--daemon] [--test TEST] [--version]

Differences from upstream ``pproxy``
------------------------------------

* ``pproxy.__version__`` reports ``"3.0.0"`` (was ``"2.7.9"``).
* ``setup.py`` declares ``python_requires=">=3.9"``. The wheel
  uploaded to PyPI under the name ``klan1-pproxy`` will refuse to
  install on Python 3.6 or 3.7.
* ``pproxy/__doc__.py`` uses ``importlib.metadata`` instead of the
  deprecated ``pkg_resources`` API to look up its own version.

Differences from upstream are tracked in
`CHANGELOG.md <https://github.com/klan1/pproxy/blob/py3.12-compat/CHANGELOG.md>`_.

Repository
----------

* Upstream: https://github.com/qwj/python-proxy (and its mirror
  https://github.com/moreati/pproxy)
* Fork: https://github.com/klan1/pproxy
* Branch: ``py3.12-compat``
* Tag: ``v3.0.0``

License
-------

MIT. Same as the upstream project.
