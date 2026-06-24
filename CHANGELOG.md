# Changelog

## [Unreleased] — py3.12-compat branch

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

- `setup.py`: bumped `python_requires` from `>=3.6` to `>=3.9`.
  Updated trove classifiers to declare Python 3.9 through 3.13.
  Python 3.6 and 3.7 are end-of-life and no longer supported.

### Tested

| Python  | HTTP listener | SOCKS5 listener |
|---------|---------------|-----------------|
| 3.9.25  | ok            | ok              |
| 3.10.14 | ok            | ok              |
| 3.11.9  | ok            | ok              |
| 3.12.4  | ok (was broken before this commit) | ok |

### Branch

This change lives on the `py3.12-compat` branch. Once reviewed it
should be merged into `master` and a tag/release cut so `pip install
pproxy` picks it up.
