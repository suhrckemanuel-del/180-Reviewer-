# Build the lead-session release zips from the prototype folder: step 2 cut to one gate variant, the
# "not for upload" comment removed, the version stamp filled.  python build_zips.py <src> <out> <stamp>
import re, sys, zipfile, pathlib
src = pathlib.Path(sys.argv[1]); out = pathlib.Path(sys.argv[2]); out.mkdir(exist_ok=True)
skill = (src / 'SKILL.md').read_text(encoding='utf-8')
skill = re.sub(r'<!-- PROTOTYPE.*?-->\n\n', '', skill, flags=re.S)
head, rest = skill.split('**Step 2. The lead\'s own read.**', 1)
block, tail = rest.split('**Step 3.', 1)
ung = re.search(r'> \*\*UNGATED:\*\* (.*?)\n>\n', block, re.S).group(1).strip()
gat = re.search(r'> \*\*GATED:\*\* (.*?)\n\n', block + '\n\n', re.S).group(1)
gat = re.sub(r'\n> ?', '\n', gat).strip()
for variant, text, name in [('ungated', ung, '180dc-review-lead'), ('gated', gat, '180dc-review-lead-gated')]:
    md = head + "**Step 2. The lead's own read.** " + text + '\n\n**Step 3.' + tail
    md = md.replace('name: 180dc-review-lead\n', f'name: {name}\n', 1)
    md = md.replace('<version stamp>', sys.argv[3])
    zp = out / f'{name}.zip'
    with zipfile.ZipFile(zp, 'w', zipfile.ZIP_DEFLATED) as z:
        z.writestr(f'{name}/SKILL.md', md)
        for f in sorted(src.rglob('*')):
            if f.is_file() and f.name != 'SKILL.md' and '__pycache__' not in f.parts:
                z.write(f, f'{name}/{f.relative_to(src).as_posix()}')
    print(zp.name, len(md.split()), 'words in SKILL.md;', 'step 2:', text[:70].replace('\n', ' '), '...')
