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

Then take on Level 2 and Level 3 if you have time.

**Hint:** never trust the browser. Anything a user can see or change can be
manipulated — check permissions on the server, every time.
