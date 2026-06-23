Issue:
MAP-001

Title:
Map Display Failure

Status:
Open

Symptoms:
地図データ準備中...
PrimaryMapRenderer非表示

Normal Version:
17477ae1

Breaking Commits:
a41f29e5
714baaeb
63be95c1
229e897d

Root Cause:
displayData gate

cache未生成

PrimaryMapRenderer未mount

Investigation Date:
2026-06-07

Recovery Target:
await loadGoogleMaps

Map retry effect

displayData gate除去

Do Not Touch:
CommandRuntime
TopBar
UnifiedPageShell

Confidence:
High
