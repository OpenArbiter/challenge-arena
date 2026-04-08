# Challenge Arena

**Can you get a PR past Arbiter?**

This repo is protected by [Arbiter](https://github.com/OpenArbiter/arbiter) — an automated trust layer that analyzes every PR for suspicious patterns before any code executes.

## The Challenge

Fork this repo, make a change, and open a PR. Arbiter will analyze your diff and decide whether to approve or block it.

**Rules:**
- Your PR must contain code that does something "interesting" (process execution, network access, file system manipulation, etc.)
- Arbiter must approve it (check run shows `openarbiter/trust: success`)
- No CI runs on this repo — Arbiter is the only gate

**What Arbiter checks:**
- Capability detection across 11 languages (Go, Python, JavaScript, Java, C, C++, C#, Rust, PHP, Swift, Kotlin)
- Invariant rules (forbidden patterns like `exec.Command`, `eval()`, `subprocess`)
- Test coverage analysis
- CI/infrastructure file modifications
- Scope validation and directory spread

**What Arbiter can't catch** (we know about these):
- Obfuscated payloads that don't match any pattern
- DNS-based data exfiltration
- Logic bugs that aren't security-relevant

## Repo Structure

```
src/
  api/          — Go HTTP server
  workers/      — Python message processor + JS formatter
scripts/        — Shell setup and lint scripts
config/         — Application configuration
deploy/         — Deployment configs (empty)
```

## Status

Arbiter evaluates every PR. No CI runs — this is purely Arbiter's analysis.

If you find a bypass, [open an issue](https://github.com/OpenArbiter/arbiter/issues) and we'll improve the patterns.
