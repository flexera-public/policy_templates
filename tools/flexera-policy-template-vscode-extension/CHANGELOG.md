# Changelog

## v0.2.0

- Expanded syntax highlighting: new `builtin-variables`, `dsl-variables`, and `dsl-functions` grammar rules
- Added inline JavaScript (`code '...'`) syntax highlighting
- Added `info()` field name highlighting
- Expanded block/subblock/flow control keyword coverage
- Improved operator matching (`=~`, `!~`, `<<`, `=`)
- Added `indentationRules` and `onEnterRules` for smart `do`/`end` indentation
- Added `wordPattern` for better word selection with `$` prefix
- Updated folding rules to use `do`/`end` markers
- Added 23 code snippets covering all major policy template patterns

## v0.1.1

- Fixed syntax highlighting bug where `detail_template <<-'EOS'` heredocs were not recognized, causing all code below them to appear as a single flat color
- Added `dsl-string-heredoc` grammar rule to properly handle non-JavaScript heredocs (`detail_template`, `summary_template`, and other DSL string blocks)
- Added word boundary guards to `javascript-embedded` pattern to prevent false matches

## v0.1.0

- Initial release
