# Detection as Code Lab

A small detection engineering project implementing security rules with automated CI testing.

## Detections

| Detection | ATT&CK Stage |
|-|-|
| SSH Brute Force | Credential Access |
| PowerShell Encoded Command | Execution |
| Web Shell Detection | Persistence |
| Suspicious Admin Account Creation | Privilege Escalation |

## Testing

Rules are tested using fixture logs.

GitHub Actions runs automatically on every push.

A failed detection test blocks CI.

CI Validation Evidence

The detection pipeline was validated through three GitHub Actions states:

1. Passing CI Run (Green)

The workflow:

".github/workflows/detection-tests.yml"

runs automatically on every push.

Pipeline steps:

1. Checkout repository
2. Install Python test dependencies
3. Run pytest detection tests
4. Fail the build if any detection stops matching

Result:
All detection tests passed successfully.

---

2. Intentionally Broken Rule Test (Red)

To prove the pipeline blocks incorrect detections, I intentionally modified one detection test.

Example:

The Web Shell detection expected:

"shell.php"

I changed the fixture so the expected malicious pattern no longer matched.

Expected behavior:

The CI pipeline failed because pytest returned:

"Process completed with exit code 1"

This demonstrated that broken detection logic cannot pass the pipeline.

After restoring the correct rule, CI returned to green.

---

Detection Example

Example rule:

Encoded PowerShell Detection

Stage:
Execution

Logic:

Detect PowerShell processes containing encoded command execution.

Example detection condition:

process_name = powershell.exe
AND command_line contains "-EncodedCommand"

Malicious fixture:

powershell.exe -EncodedCommand SQBmACgA

Expected result:

Detection fires.

Benign fixture:

powershell.exe Get-Service

Expected result:

No alert.

This prevents normal administrator PowerShell activity from creating false positives.

---

Test Harness Logic

The pytest harness loads detection fixtures and checks two conditions:

1. Malicious events must trigger detections.
2. Benign events must not trigger detections.

Example:

assert detect(malicious_event) == True

assert detect(benign_event) == False

This proves the rules detect attacker behavior while reducing unnecessary alerts.

---

Design Decisions

I used lightweight YAML-style rules with Python unit tests because they are easy to maintain, version control, and validate without requiring an expensive SIEM.

The project demonstrates a complete detection engineering cycle:

Write rule → Test against fixtures → Run CI → Block broken detections → Deploy trusted logic.
