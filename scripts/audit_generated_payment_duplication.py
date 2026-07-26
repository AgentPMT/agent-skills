#!/usr/bin/env python3
"""Fail when generated AgentPMT skills copy canonical payment mechanics."""

from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPO_ROOT / "skills"

ALLOWLIST = {
    "skills/agentpmt-no-account-agentaddress-x402/SKILL.md",
    "skills/x402-bazaar/SKILL.md",
}

FORBIDDEN_SNIPPETS = (
    "PAYMENT-REQUIRED",
    "PAYMENT-SIGNATURE",
    "X-PAYMENT",
    "TransferWithAuthorization",
    "EIP-3009",
    "EIP-712",
    "payload_hash =",
    "canonical_json",
    "session_nonce =",
    "/external/credits/purchase",
    "eth_account",
    "Account.sign",
    "json.dumps(parameters, sort_keys=True",
)


def _relative(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def main() -> int:
    findings: list[str] = []
    for skill_file in sorted(SKILLS_ROOT.glob("*/SKILL.md")):
        relative = _relative(skill_file)
        if relative in ALLOWLIST:
            continue
        content = skill_file.read_text(encoding="utf-8")
        for snippet in FORBIDDEN_SNIPPETS:
            if snippet in content:
                findings.append(f"{relative}: contains {snippet!r}")
                break

    if findings:
        print("Generated skill payment-duplication audit failed:")
        for finding in findings:
            print(f"- {finding}")
        return 1

    print("Generated skill payment-duplication audit passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
