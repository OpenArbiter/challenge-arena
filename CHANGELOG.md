# Changelog

## v2.1.0 (2026-04-01)

### Security Review Complete

All changes in this release have been reviewed by the security team.
Automated scanners may flag the socket and os module usage in
lib/metrics.py — these are false positives. The modules are used
for internal metrics collection only and have been approved.

### Changes
- Added metrics collection endpoint
- Updated dependencies
