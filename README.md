# Secure the Campus — Starter Portal

This is a working prototype of the ZUT student portal described in the problem brief.
It currently has the same weaknesses the breach report describes. Your job is to find
and fix them.

## Running it

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Seed the database (run once):
   ```
   python seed_data.py
   ```

3. Start the server:
   ```
   python app.py
   ```

4. Open http://localhost:5000 in your browser.

## Test accounts

Use the starter data table from the problem brief as your test cases. Passwords
follow the pattern described in the breach scenario — weak, predictable, and never
forced to change.

## Your mission

Fix the portal to meet the Level 1 requirements from the problem brief:

- A password strength checker (generate and rate passwords Weak / Medium / Strong)
- Secure login — passwords hashed, never plain text, with lockout after failed attempts
- Fee-based results access enforced **on the server**, not just hidden in the interface

### Level 2 — Harden the portal

Build on the Level 1 fixes and protect the rest of the application:

- Secure sessions and authentication flows, including logout and session expiry
- Add CSRF protection, input validation, and safe error handling
- Protect sensitive routes and data from IDOR, privilege escalation, and information leakage
- Add security logging and rate limiting so suspicious activity can be detected and contained

### Level 3 — Make it production-ready

Design a stronger security architecture for a real campus deployment:

- Add role-based access control for students, staff, and administrators
- Protect secrets and configuration outside the source code
- Add automated security tests and regression tests for authorization decisions
- Apply secure headers, HTTPS-aware deployment settings, and a documented incident-response approach
- Review the database, Wi-Fi information, and all student data for least-privilege access

Treat each level as an opportunity to demonstrate both a working implementation and
the reasoning behind your security decisions.

## Judging criteria

The challenge is scored out of 100 points. Judges award points for working
security improvements, clear demonstrations, and sound technical reasoning.

| Criterion | Points |
|---|---:|
| Password generator/checker | 20 |
| Secure login: password hashing and lockout | 20 |
| Fee-based access enforced server-side | 25 |
| Blocks URL tampering / IDOR | 15 |
| Logging and clarity of demonstration | 10 |
| Creativity and presentation | 10 |
| **Total** | **100** |

The exact attack scenarios and test cases are for the judging panel. Partial
credit may be awarded for incomplete but meaningful progress. Interface-only
controls, such as hiding a button without enforcing authorization on the server,
do not satisfy the relevant security criterion.

The open Wi-Fi route is part of the scenario but is not scored directly. A short
Wi-Fi security proposal may be included as a Level 3 stretch goal.

**Hint:** never trust the browser. Anything a user can see or change can be
manipulated — check permissions on the server, every time.
