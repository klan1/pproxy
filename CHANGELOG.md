# Changelog

## [3.0.2] — 2026-06-24 — README-only release (tag v3.0.2)

No code change versus 3.0.1. Re-publishes the package with an
expanded `README.rst` that covers the "fresh box" install path on
Debian / Ubuntu / Fedora / Arch / Alpine / macOS / Windows, plus an
"Older Linux" block for systems that still ship Python 3.7 or 3.8
(deadsnakes PPA on Debian/Ubuntu, IUS on RHEL/CentOS 7). The
QuickStart section above stayed minimal (`pip3 install klan1-pproxy`)
on purpose; the new "Installing Python 3 and pip" section picks up
the slack for users on a fresh Chromebook, server, or container.

## [3.0.1] — 2026-06-24 — README rebuild (tag v3.0.1)

No code change versus 3.0.0. Re-publishes the package with the full
762-line upstream `README.rst` (the 3.0.0 release shipped a 2.4 KB
abbreviated version that explained nothing). Edits to the upstream
README are limited to:

  - Title: `python-proxy` -> `klan1-pproxy`.
  - Badge URLs: `pproxy.svg` -> `klan1-pproxy` etc., with the
    `:target:` URLs pointing at the klan1 fork.
  - Install commands: `pip3 install pproxy` ->
    `pip3 install klan1-pproxy`.
  - Added a "Projects" trailer renamed to "Related projects (from
    upstream pproxy ecosystem)" with a disclaimer that those
    projects (python-vpn, shadowproxy) are NOT part of klan1-pproxy
    and are still on the legacy 2.x line.

## [3.0.0] — 2026-06-24 — py3.12-compat branch (tag v3.0.0)

### BREAKING CHANGES

- **Dropped support for Python 3.6 and 3.7.** `setup.py` now declares
  `python_requires='>=3.9'`. Both 3.6 (EOL Dec 2021) and 3.7 (EOL Jun
  2023) have been unsupported by the Python maintainers for years.
  Per SemVer 2.0, dropping interpreter support is a major version bump.

### Fixed

- **Python 3.12+ compatibility.** `asyncio.get_event_loop()` raises
  `RuntimeError` on Python 3.12 when called from the main thread without
  a running event loop. uvloop 0.21+ inherits this stricter behavior,
  so `pproxy -l http://...` would fail with:

  ```
  RuntimeError: There is no current event loop in thread 'MainThread'.
  ```

  Replaced all 12 occurrences of `asyncio.get_event_loop()` across
  `pproxy/server.py` and `pproxy/proto.py` with a new
  `proto._get_loop()` helper that prefers `asyncio.get_running_loop()`
  (works inside coroutines since Python 3.7) and falls back to a
  default loop if none is set. `main()` now creates the loop explicitly
  via `new_event_loop()` + `set_event_loop()` and the `--test` path
  uses `asyncio.run()`.

- **`pkg_resources` deprecation warning** emitted by setuptools >= 81
  when `pproxy` is imported. `pproxy/__doc__.py` now uses
  `importlib.metadata` (Python 3.8+) to look up the installed version,
  with a fallback to the `importlib_metadata` backport.

### Changed

- `setup.py`:
  - `python_requires` from `>=3.6` to `>=3.9`.
  - trove classifiers now declare Python 3.9 through 3.13.
  - Replaced `use_scm_version=True` with an explicit `resolve_version()`
    helper that prefers the `PPROXY_VERSION` env var, falls back to
    `setuptools_scm` when run from a git checkout, and finally to the
    hardcoded `__version__` string in `pproxy/__doc__.py`.
- `pproxy/__doc__.py`: hardcoded `__version__ = "3.0.0"` as the
  last-resort fallback for `resolve_version()`.

### Tested

| Python  | HTTP listener | SOCKS5 listener |
|---------|---------------|-----------------|
| 3.9.25  | ok            | ok              |
| 3.10.14 | ok            | ok              |
| 3.11.9  | ok            | ok              |
| 3.12.4  | ok (was broken in 2.7.9) | ok    |

End-to-end verified by installing the freshly built
`pproxy-3.0.0.tar.gz` sdist into a clean Python 3.12.4 venv:

```
$ python3 -m venv /tmp/pproxy-test-venv
$ /tmp/pproxy-test-venv/bin/pip install ./pproxy-3.0.0.tar.gz
$ /tmp/pproxy-test-venv/bin/python3 -c \
    "from pproxy.__doc__ import __version__; print(__version__)"
3.0.0
$ /tmp/pproxy-test-venv/bin/python3 -m pproxy -l http://127.0.0.1:29998 &
$ curl -x http://127.0.0.1:29998 http://ifconfig.me
181.129.245.170
```

### Installing this fork

```bash
# from git+https (anonymous read)
python3 -m pip install \
  "pproxy @ git+https://github.com/klan1/pproxy.git@py3.12-compat"

# from git+ssh (uses your SSH key; requires write access on the repo)
python3 -m pip install \
  "pproxy @ git+ssh://git@github.com/klan1/pproxy.git@py3.12-compat"

# pin the released tag
python3 -m pip install \
  "pproxy @ git+https://github.com/klan1/pproxy.git@v3.0.0"
```

### Branch

This release lives on the `py3.12-compat` branch with the `v3.0.0`
tag. Once reviewed it should be merged into `master` and the upstream
maintainers notified (PR against `moreati/pproxy` if they want it).

---

## [2.7.9] — last upstream release (qwj/python-proxy)

Forked at `c3a8446` from `moreati/pproxy`. No changes from upstream
other than the fork metadata. The `v2.7.9` tag was not created
because we inherited the upstream version string directly.
