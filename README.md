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
