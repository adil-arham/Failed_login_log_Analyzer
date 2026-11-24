Failed Login Log Analyzer

A small Python script that reads an authentication log, finds failed login attempts, and flags users with suspicious activity (3 or more failures). Uses only the Python standard library.

Files
auth.log - sample log with exactly 50 entries (7 users)
log_analyzer.py - the analyzer
test_log_analyzer.py - unit tests (unittest)
Log format

One entry per line: YYYY-MM-DD HH:MM:SS username SUCCESS|FAILED

How to run
python log_analyzer.py            # analyzes auth.log
python log_analyzer.py other.log  # analyzes another file
python -m unittest -v             # run the tests
Example output
Entries analyzed: 50 (skipped 0 bad lines)
Total failed attempts: 10
Failures per user:
  bob: 4
  carol: 1
  dave: 2
  eve: 3
Flagged users (>= 3 failures): ['bob', 'eve']
How the threshold works

THRESHOLD = 3 is a constant at the top of log_analyzer.py. The script counts FAILED entries per username in a dictionary. A user is flagged when their count is >= THRESHOLD. So 3 failures is flagged and 2 is not (dave has 2 and is not flagged). Change the constant to make it stricter or looser.

Error handling
Missing file: prints a clear error message instead of crashing.
Blank or malformed lines are skipped and the number skipped is reported.
Limitations
Counts failures per username only, so it can't tell one attacker from a user who simply forgot their password.
No time window: 3 failures spread over a year are treated the same as 3 failures in one minute.
No IP address tracking, so it can't spot one source trying many accounts.
