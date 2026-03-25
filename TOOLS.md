# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

## Browser Lanes

### OpenClaw managed browser

- Default browser lane: `openclaw`
- Purpose: persistent agent-owned browser identity, saved sessions, safer automation
- Status: preferred default for browsing and site logins the agent should retain

### User browser attach

- Special-case lane: `user`
- Purpose: live-data access in the real Chrome profile when current human/session state matters
- Requirement: normal Chrome must be open with remote debugging enabled so `~/Library/Application Support/Google/Chrome/DevToolsActivePort` exists
- Constraint: existing-session attach is process-bound; if that Chrome instance closes, the attach dies
- Helper launcher: `~/.openclaw/workspace/scripts/open-user-chrome-debug.sh`

Operational rule:
- Default to `openclaw`
- Use `user` only when live human-browser state is specifically needed

---

Add whatever helps you do your job. This is your cheat sheet.
