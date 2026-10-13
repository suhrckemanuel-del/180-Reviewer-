# What Claude Free, ChatGPT and Gemini do with an uploaded skill

Resolves issue #9 (child of map #7). Researched and checked 2026-10-13. Every fact below was read on that date at the URL given. Three labels:

- **Confirmed in docs**: stated on a first-party page (support.claude.com, claude.com, platform.claude.com, help.openai.com, chatgpt.com, support.google.com).
- **Reported**: only from a secondary source, or first-party sources disagree with each other.
- **Not found**: looked for and not stated anywhere first-party.

## Short answer

Claude Free can take an uploaded skill, and its Python scripts should run, because Free has the same code-execution sandbox as paid plans, with network access to package sources. But each of ~20 people must upload the zip themselves: sharing and org-wide provisioning are Team/Enterprise only. Gemini (free, personal accounts) also takes a `SKILL.md` or zip. ChatGPT is contradictory: the pricing page says "Skills beta: Yes" on Free, but the help article lists only Business, Enterprise, Healthcare and Edu. Nobody documents a skill zip size limit for Claude. One first-party Anthropic page still says custom skills are Pro+ and live under "Settings > Features". The fastest way to settle both conflicts is one person on a Free account trying the upload before 27 Oct.

## Claude Free

| Fact | Status | Source |
|---|---|---|
| Skills are available on Free, Pro, Max, Team, Enterprise; they require code execution to be on | Confirmed | https://support.claude.com/en/articles/12512180-use-skills-in-claude |
| Upload path: Customize > Skills, then "+", then "+ Create skill", then "Upload a skill", then a ZIP containing the skill folder. The skill then shows up in the list with an on/off toggle | Confirmed | same |
| On Free/Pro/Max, enable via Settings > Capabilities, "Code execution and file creation" | Confirmed | same |
| Pricing table: Skills "Yes" on Free; "Organization wide skills deployment" "No" on all individual plans | Confirmed | https://claude.com/pricing |
| Code execution and file creation is available to all users including Free, on web, Desktop and Mobile. Free/Pro/Max: network access enabled, limited to approved package sources (npm, PyPI, GitHub, etc.) | Confirmed | https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude |
| The sandbox runs Python ("Claude can create Python scripts for data analysis") | Confirmed | same |
| Claude on claude.ai can install packages from PyPI/npm when it loads a skill. API skills cannot install packages | Confirmed | https://support.claude.com/en/articles/12512198-how-to-create-custom-skills |
| **A skill's bundled `scripts/*.py` actually execute on a Free account** | **Not found as an explicit statement.** Inferred from the three rows above (skills on Free + code execution on Free + skills use the VM). No page says "scripts run on Free" | combination of the above, plus https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview ("Skills use Claude's VM environment") |
| ZIP layout: the skill folder sits at the ZIP root (no loose files at the root), and the folder name matches the skill name. Example: `my-skill.zip` > `my-skill/` > `skill.md` + `resources/` | Confirmed | https://support.claude.com/en/articles/12512198-how-to-create-custom-skills |
| File name casing: the help article writes `skill.md`; the org-provisioning article and claude.com docs write `SKILL.md` | Reported (sources differ). Use `SKILL.md`, the Agent Skills standard | https://support.claude.com/en/articles/13119606 ; https://claude.com/docs/skills/how-to |
| Frontmatter: `name` (max 64 chars) and `description` required. Help article says description max **200** chars; platform docs say max **1024** | Confirmed, but the two disagree. Stay under 200 to be safe | 12512198 (above); https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview |
| Upload fails if: the ZIP is over the size limit, the folder name doesn't match the skill name, `skill.md` is missing, or the name/description has invalid characters | Confirmed (failure list) | https://support.claude.com/en/articles/12512180-use-skills-in-claude |
| **Numeric ZIP / skill size limit** | **Not found.** A limit exists (it is listed as a failure cause) but no number is published | — |
| Uploaded skills are private to the uploader until shared; sharing is Team/Enterprise only | Confirmed | https://support.claude.com/en/articles/12512180-use-skills-in-claude |
| **Conflict:** the platform docs' claude.ai section says custom skills upload "through Settings > Features" and are "available on Pro, Max, Team, and Enterprise plans", "individual to each user", "not shared organization-wide" | Reported. This contradicts the help center and pricing page, and is probably stale (the help center describes sharing and publishing that the platform doc says don't exist) | https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview |
| Free context window: pricing says "Up to 1M, varies by model" on every plan, including Free. The paid-plan article gives per-model figures (200K to 1M) for paid plans only | Confirmed for pricing; Free per-model figure **not found** | https://claude.com/pricing ; https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans |
| Free usage limits: no number is published. Paid plans have a 5-hour session limit plus a weekly limit | Free figure **not found** | https://support.claude.com/en/articles/11647753 |
| Free gets Projects "Up to 5"; project sharing "No" | Confirmed | https://claude.com/pricing |
| Chat uploads: 20 files per chat; PDFs up to 1000 pages (visual analysis up to 100 pages; text only from 101 to 1000). The per-file size is stated as **500MB** in the upload article but **30MB** in the code-execution article | Confirmed, but the two disagree on size | https://support.claude.com/en/articles/8241126-upload-files-to-claude ; 12111783 (above) |
| **PPTX upload for reading**: not in the upload article's supported list (PDF, DOCX, CSV, TXT, HTML, ODT, RTF, EPUB, JSON, XLSX, images). The code-execution article says you can upload "CSV, TSV, and other files" for analysis, and the built-in PowerPoint skill exists | PPTX **reading not confirmed**. Export the deck to PDF: that path is confirmed | 8241126 and 12111783 (above) |

**Effect on an ~11k-token reviewer:** nothing documented says it won't fit. Skills load the body only when triggered, and bundled files cost no context until read (platform overview, "no practical limit on bundled content"). The binding Free-plan risk is the undocumented usage cap, not the context window.

## Claude Pro / Team (what changes)

| Fact | Status | Source |
|---|---|---|
| Pro and Max: the same per-person upload as Free. No sharing (sharing is Team/Enterprise) | Confirmed | https://support.claude.com/en/articles/12512180-use-skills-in-claude |
| Team: skills are on by default at org level; members can share with specific people (shared skills are view-only and auto-update) and "Publish to org" (with optional review and scanning) | Confirmed | same |
| Team/Enterprise owners can provision a skill for everyone via Organization settings > Plugins & skills > Add > Upload (a .zip that includes SKILL.md); it is on by default for all users and syncs to Claude Code | Confirmed | https://support.claude.com/en/articles/13119606 |
| Group targeting via plugins is Enterprise only | Confirmed | same |
| Team network egress default: the article contradicts itself (package managers only vs off) | Reported | https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude |
| `npx skills add` (Vercel Labs CLI) installs skills into filesystem agents (Claude Code, Codex, Cursor, OpenCode and 75 more). It does not install into claude.ai chat | Confirmed for what it supports; claude.ai **not listed** | https://github.com/vercel-labs/skills (README) |
| Claude Code (Pro and up) reads skills from `~/.claude/skills/` or `.claude/skills/`, and skills can ship as plugins. claude.ai, API and Claude Code skill stores are separate | Confirmed | https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview |

## ChatGPT

| Fact | Status | Source |
|---|---|---|
| Help article: skills are "available to eligible ChatGPT Business, Enterprise, Healthcare, and Edu users". Path: sidebar Plugins > Skills tab > Create > "Upload from your computer". Uploads are scanned and can be marked Needs Review or Blocked; skills can include "reusable steps and scripts"; sharing works within a workspace. Updated "last month" | Confirmed | https://help.openai.com/en/articles/20001066-skills-in-chatgpt |
| Pricing page: a "Skills beta" row reads "Yes" for Free, Go, Plus and Pro | Confirmed on the page, but **conflicts** with the help article | https://chatgpt.com/pricing |
| Upload format (zip vs SKILL.md), size limits, whether scripts run on Free | **Not found** | — |
| Free context window: GPT Instant 27K total; GPT Reasoning "Varies" (Go/Plus 54K/256K, Pro 128K/400K). The portion available for user input is smaller | Confirmed | https://chatgpt.com/pricing |
| Free file uploads: 3 per day; PPTX is supported; 512MB per file; 2M tokens per document. Projects: up to 5 files on Free | Confirmed | https://help.openai.com/en/articles/8555545-file-uploads-faq |

**Effect:** an 11k-token reviewer plus a deck plus the reply is tight inside Free's 27K Instant window. With 3 uploads a day, one review per person per day is realistic on Free. **Fallback if skills don't show up:** paste the SKILL.md body as the first message, or into a Project's instructions, then attach the deck. This is the "paste" path the reviewer already uses.

## Gemini

| Fact | Status | Source |
|---|---|---|
| Skills are "available without a Google AI subscription". Requirements: age 18+, a personal Google Account (not work or school), Keep Activity on. Works on web, mobile and Mac. Rolling out gradually, personal accounts first | Confirmed | https://support.google.com/gemini/answer/17094296?hl=en |
| Upload a `SKILL.md`, or a folder or `.zip` with `SKILL.md` at its root. The name must be lowercase with hyphens. Total upload is at most 100 MB. Text-based files (.md, .py, .sh, .json, .yaml, .csv, .html), plus .pdf and images, are accepted; .docx and .xlsx are not. Remove .DS_Store and .pyc files | Confirmed (English page). The German version of the page reportedly excludes .pdf and images | same |
| Scripts may be included, but scripts that need internet access aren't supported. How scripts execute is not described | Confirmed / partly not found | same |
| Sharing skills with others | **Not found** | same |
| Gems are being migrated into skills | Confirmed (page); the dates are reported, from gemini.google overview pages | same |
| Free chat uploads: up to 10 files per prompt, 100 MB per file (2 GB for video), with rolling usage caps | Confirmed | https://support.google.com/gemini/answer/14903178?hl=en |
| Free context window in the Gemini app | **Not found** | — |

**Effect:** consultants who use a 180DC/university Google account are excluded: work and school accounts are not eligible.

## What to verify by hand before 27 Oct (one person, ~15 minutes)

1. On a **Free** Claude account, upload the reviewer zip through Customize > Skills. Confirm it appears, triggers, and (if it has `scripts/`) that a script runs. This settles the platform-docs conflict.
2. Note any size error the upload gives. That is the only way to learn the undocumented limit.
3. On a **Free** ChatGPT account, check whether Plugins > Skills exists at all.
4. Upload a `.pptx` to Claude Free and see whether it is read. If not, tell people to export the deck to PDF.
