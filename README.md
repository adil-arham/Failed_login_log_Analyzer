Failed Login Log Analyzer

A small Python script that reads an authentication log, finds failed login attempts, and flags users with suspicious activity (3 or more failures). Uses only the Python standard library.

Files
auth.log - sample log with exactly 50 entries (7 users)
log_analyzer.py - the analyzer
test_log_analyzer.py - unit tests (unittest)
Log format

One entry per line: YYYY-MM-DD HH:MM:SS username SUCCESS|FAILED

Dealing with Error 
Missing file: prints a clear error message instead of crashing.
Blank or malformed lines are skipped and the number skipped is reported


Limitations
Counts failures per username only, so it can't tell one attacker from a user who simply forgot their password.
No time window: 3 failures spread over a year are treated the same as 3 failures in one minute.
No IP address tracking, so it can't spot one source trying many accounts.
