Runtime Memory

目的：
過去の障害・判断・調査結果を保存する。

再調査禁止。

問題発生時は
まず Runtime Memory を検索する。

---

運用ルール

以後、以下が発生した場合は
GitHub Runtime Memory へ登録する。

- 重大障害
- 重要判断
- 設計変更

正本：
/docs/runtime-memory

Obsidian は GitHub 同期で閲覧・検索する。

---

分類

Issues
Decisions
Knowledge
Investigations
Recovery Playbooks

---

ID 命名（最低登録条件）

Issue:
MAP-xxx
SEN-xxx
FED-xxx

Decision:
DEC-xxx

Knowledge:
KNW-xxx

Recovery:
RCV-xxx

Investigations:
YYYY-MM-DD-{Topic}.md

---

Issue 必須項目

新しい Issue 作成時、以下を必ず記載する。

Symptoms
Normal Version
Breaking Commit
Root Cause
Recovery Target
Do Not Touch
Confidence

---

ファイル配置

Issues/
Decisions/
Knowledge/
Investigations/
RecoveryPlaybooks/
