### Running Multiple Claude Code Instances

Open two separate terminal windows.

Terminal 1 - Update Hook Card Component

claude

Prompt:
Change all Hook Card titles to pink font.
Modify only:
templates/index.html
Do not modify other files.

Terminal 2 - Update html port

claude

Prompt:
Change url port from 8000 to 8002
Modify only:
main.py
Do not modify other files

### Capturing Proof This Ran in Parallel

Do these while the two terminals are running, and right after, so the
evidence isn't lost once the sessions exit.

1. **Snapshot running processes** - in a third terminal, while both agents
   are working:
   ```
   ps aux | grep -i "claude" | grep -v grep
   ```
   Save the output. Two distinct PIDs listed at the same time is direct
   proof of concurrency (a git log can't show this after the fact).

2. **Commit separately per terminal.** When each agent finishes, commit
   from that terminal immediately, scoped to only its files:
   ```
   git add app/server.py static/app.js templates/index.html
   git commit -m "Improve HookCard visual design"
   ```
   ```
   git add main.py
   git commit -m "Change port 8000 -> 8001"
   ```
   Two separate commits (not one squashed commit) let you check
   overlapping author timestamps afterward:
   ```
   git log --format=fuller
   ```

3. **Check file isolation after both finish:**
   ```
   git diff --stat HEAD~2 HEAD
   ```
   Confirm each commit only touches the files it was scoped to - no
   cross-contamination between the two prompts.

4. **Check timestamp clustering:**
   ```
   stat -f "%Sm %N" -t "%Y-%m-%d %H:%M:%S" main.py app/server.py static/app.js templates/index.html
   ```
   Files from both terminals should fall in the same tight window (e.g.
   under a minute apart) rather than one set finishing long before the
   other starts.
