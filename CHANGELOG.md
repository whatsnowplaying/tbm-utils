# Change Log

Notable changes to this project based on the [Keep a Changelog](https://keepachangelog.com) format.
This project adheres to [Semantic Versioning](https://semver.org).


## [Unreleased](https://github.com/thebigmunch/tbm-utils/tree/master)

[Commits](https://github.com/thebigmunch/tbm-utils/compare/2.4.0...master)

### Added

* ``FILEPATH_CHARACTER_REPLACEMENTS``.


## [2.4.0](https://github.com/thebigmunch/tbm-utils/releases/tag/2.4.0) (2020-03-16)

[Commits](https://github.com/thebigmunch/tbm-utils/compare/2.3.0...2.4.0)

### Changed

* Make ``position`` parameter for ``cast_to_list`` an optional kwarg.
	It defaults to casting the first argument if not given.


## [2.3.0](https://github.com/thebigmunch/tbm-utils/releases/tag/2.3.0) (2020-03-01)

[Commits](https://github.com/thebigmunch/tbm-utils/compare/2.2.1...2.3.0)

### Added

* Support singular and plural item labels for ``LabelList``.
* Custom items, keys, and values methods and views for ``AttrMapping``.


## [2.2.1](https://github.com/thebigmunch/tbm-utils/releases/tag/2.2.1) (2020-02-25)

[Commits](https://github.com/thebigmunch/tbm-utils/compare/2.2.0...2.2.1)

### Fixed

* Add missing attributes in ``DataReader.__init__``.


## [2.2.0](https://github.com/thebigmunch/tbm-utils/releases/tag/2.2.0) (2020-02-25)

[Commits](https://github.com/thebigmunch/tbm-utils/compare/2.1.0...2.2.0)

### Added

* Ability for ``DataReader`` to read bits.


## [2.1.0](https://github.com/thebigmunch/tbm-utils/releases/tag/2.1.0) (2020-02-25)

[Commits](https://github.com/thebigmunch/tbm-utils/compare/2.0.2...2.1.0)

### Added

* ``DataReader`` class.
* ``datareader`` decorator.


## [2.0.2](https://github.com/thebigmunch/tbm-utils/releases/tag/2.0.2) (2020-02-23)

[Commits](https://github.com/thebigmunch/tbm-utils/compare/2.0.1...2.0.2)

## Fixed

* Add missing dependency.


## [2.0.1](https://github.com/thebigmunch/tbm-utils/releases/tag/2.0.1) (2020-02-23)

[Commits](https://github.com/thebigmunch/tbm-utils/compare/2.0.0...2.0.1)

### Removed

* ``cast_to_list`` decorator from ``filter_filepaths_by_dates``.


## [2.0.0](https://github.com/thebigmunch/tbm-utils/releases/tag/2.0.0) (2020-02-23)

[Commits](https://github.com/thebigmunch/tbm-utils/compare/1.1.1...2.0.0)

### Changed

* API for ``filter_filepaths_by_dates``.


## [1.1.1](https://github.com/thebigmunch/tbm-utils/releases/tag/1.1.1) (2020-02-01)

[Commits](https://github.com/thebigmunch/tbm-utils/compare/1.1.0...1.1.1)

### Fixed

* Old code in ``get_defaults`` missed in prior edit pass.


## [1.1.0](https://github.com/thebigmunch/tbm-utils/releases/tag/1.1.0) (2020-02-01)

[Commits](https://github.com/thebigmunch/tbm-utils/compare/1.0.0...1.1.0)

### Changed

* Init of ``AttrMapping`` to use ``__setitem__``.


## [1.0.0](https://github.com/thebigmunch/tbm-utils/releases/tag/1.0.0) (2019-10-10)

[Commits](https://github.com/thebigmunch/tbm-utils/commit/cf46bd09ee883e9e82d5b9f584c7f910675d18f6)

* Initial release.
