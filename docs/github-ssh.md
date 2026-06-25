# Emma's Site — GitHub SSH Configuration (Zeabur & Desktop)

## Key Location Matters (Critical — Updated for v0.16+)

**Zeabur Hermes** and **Desktop Hermes** have DIFFERENT key paths. Do not confuse them.

---

## On Zeabur (Cloud / Server Instance)

The `/root/.ssh/` directory gets wiped during Hermes version updates (git reset --hard on `/opt/hermes` destroys it). Use the permanent deploy key:

- **Private key:** `/opt/data/.ssh/id_ed25519_emma` (permanent — outside Hermes code)
- **SSH config:** `/opt/data/.ssh/config` (Host github.com with IdentityFile pointing to the key above)
- **Git command:** `GIT_SSH_COMMAND="ssh -i /opt/data/.ssh/id_ed25519_emma -o StrictHostKeyChecking=no" git push origin main`
- **Per-repo persistent config:** `git config core.sshCommand "ssh -i /opt/data/.ssh/id_ed25519_emma -o StrictHostKeyChecking=no"`
- **Git remote (SSH):** `git@github.com:reereegrata/Emmas-sleep-advice-site.git`
- **Clone (no auth needed):** `git clone https://github.com/reereegrata/Emmas-sleep-advice-site.git /tmp/Emmas-sleep-advice-site`

### First-Time Setup on Zeabur (after fresh clone)
```bash
cd /tmp/Emmas-sleep-advice-site
git remote set-url origin git@github.com:reereegrata/Emmas-sleep-advice-site.git
git config core.sshCommand "ssh -i /opt/data/.ssh/id_ed25519_emma -o StrictHostKeyChecking=no"
```

### Deploy Key (Add to GitHub if re-adding)
Public key:
```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJd0VAy2Q9qpmDvtxhq4dgV8l1aC+e+tMdyMBbLcIEnb zeabur-deploy@emmassleepadvice.com
```
Go to: Repo → Settings → Deploy keys → Add deploy key → paste → check "Allow write access"

---

## On Desktop (Local Machine)

- **Private key:** `/root/.ssh/id_ed25519_emma`
- **Git command:** `GIT_SSH_COMMAND="ssh -i /root/.ssh/id_ed25519_emma" git push`
- **Site files:** `/opt/Emmas-sleep-advice-site/`

---

## Wrong Key (Do NOT Use)

The key at `/opt/data/profiles/agentnyroh/home/.ssh/id_ed25519` is the Hermes agent's own key — NOT the Emma site key. It will fail with "Permission denied (publickey)."
