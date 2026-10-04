"""公開套件的JSON、內部連結、技能引用與敏感資料檢查。

不連網、不修改檔案；檢查不能取代人工發布審閱或網站實測。
"""
from pathlib import Path
from urllib.parse import unquote
import json
import re
import sys

root = Path(__file__).resolve().parents[1]
errors = []
files = [p for p in root.rglob('*') if p.is_file() and '.git' not in p.parts and '__pycache__' not in p.parts]
text_extensions = {'.md', '.json', '.ps1', '.py', '.srt'}
for path in files:
    rel = path.relative_to(root)
    if path.suffix.lower() in {'.pdf', '.mp4', '.wav', '.mp3'}:
        errors.append(f'公開包不應包含原教材／影音附件：{rel}')
    if path.suffix not in text_extensions:
        continue
    content = path.read_text(encoding='utf-8')
    if path.suffix == '.json':
        try:
            json.loads(content)
        except ValueError as exc:
            errors.append(f'JSON錯誤 {rel}: {exc}')
    # 文件可提及token一詞；只擋憑證型字串或原帳號專用路徑。
    patterns = [r'gh[pousr]_[A-Za-z0-9]{20,}', r'github_pat_[A-Za-z0-9_]{30,}',
                r'sk-[A-Za-z0-9_-]{25,}', r'https://app\.edcafe\.ai/(?:preview|join)/[A-Za-z0-9]',
                r'https://app\.edcafe\.ai/me/file\?', r'C:[/\\]Users[/\\]User[/\\]',
                r'https://(?:www\.)?youtube\.com/watch\?v=', r'https://studio\.youtube\.com/channel/[A-Za-z0-9_-]+']
    # 本檢查程式的規則本身不是洩漏；不檢查規則字面值。
    if path.name != 'validate_package.py':
        for pattern in patterns:
            if re.search(pattern, content):
                errors.append(f'需人工檢查公開資料：{rel}，規則 {pattern}')
    if path.suffix == '.md':
        # 移除程式碼示例；只驗證真正Markdown連結。
        prose = re.sub(r'```.*?```', '', content, flags=re.S)
        for match in re.finditer(r'\[[^\]]*\]\(([^)]+)\)', prose):
            target = match.group(1).strip().strip('<>')
            if re.match(r'(?:https?://|mailto:|#)', target):
                continue
            target = unquote(target.split('#', 1)[0])
            if target and not (path.parent / target).exists():
                errors.append(f'內部連結不存在：{rel} -> {target}')

skill = root / 'skills/edcafe-operations/SKILL.md'
body = skill.read_text(encoding='utf-8')
if not re.match(r'---\nname: edcafe-operations\ndescription: .+\n---\n', body):
    errors.append('SKILL frontmatter不完整')
index = json.loads((skill.parent / 'references/操作資料.json').read_text(encoding='utf-8'))
ids = [item['id'] for item in index['operations']]
if len(ids) != len(set(ids)):
    errors.append('操作索引id重複')
for item in index['operations']:
    if not all(item.get(k) for k in ('id', 'title', 'route', 'status')):
        errors.append('操作索引必要欄位缺漏')

if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f'通過：{len(files)}個檔案，{len(ids)}項操作；JSON、內部連結、技能入口及公開資料規則。')
print('此檢查不表示外部網站連結、平台操作或教材內容全部通過。')
