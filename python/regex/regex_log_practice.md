Regex Practice Logs (Intermediate to Master)
Use the following logs to practice extracting log severity/levels with regex.
Do NOT write code here. Just focus on the patterns.

Intermediate Logs

2026-02-12 10:15:03 INFO User logged in
2026-02-12 10:15:07 WARNING Disk usage at 85%
2026-02-12 10:15:09 ERROR Failed to connect to DB
[auth-service] DEBUG Token validated
NOTICE Config file reloaded
[worker] CRITICAL Job queue overflow

Advanced Logs

2026-02-12T10:15:03Z [backend] ERROR: Connection timeout
nginx[2213]: WARN client closed connection prematurely
systemd: ALERT Service restarted too frequently
kubelet[3321]: info Node pressure resolved
panic: runtime error: invalid memory address
[cache] FATAL worker crashed unexpectedly

Master Logs

{"time":"2026-02-12T10:15:03Z","level":"error","service":"payments","msg":"db connection failed"}
{"level":"CRITICAL","component":"gateway","code":502,"message":"bad upstream"}
time=2026-02-12 level=warn service=api msg="rate limit exceeded"
lvl=ERROR component=auth msg="invalid token"
<sev=HIGH> Payment service unavailable
[!!!] SEVERE - Kernel panic detected
2026/02/12 10:15:03 | lvl=panic | system crash
ERROR could not bind to port 443

Expected Results (What your regex should extract)

INFO
WARNING
ERROR
DEBUG
NOTICE
CRITICAL

ERROR
WARN
ALERT
info
panic
FATAL

error
CRITICAL
warn
ERROR
HIGH
SEVERE
panic
ERROR
