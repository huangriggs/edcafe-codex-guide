"""唯讀離線查詢，不會連線Edcafe。"""
from pathlib import Path
import json
import sys

root = Path(__file__).resolve().parents[1]
data = json.loads((root / 'skills/edcafe-operations/references/操作資料.json').read_text(encoding='utf-8'))
keyword = ' '.join(sys.argv[1:]).casefold()
matches = [item for item in data['operations'] if keyword in ' '.join(str(item.get(key, '')) for key in ('id', 'title', 'keywords', 'route', 'status')).casefold()]
for item in matches:
    print(f"{item['title']}\n  {item['route']}\n  {item['status']}")
if not matches:
    print('沒有符合的操作；請改用較短的關鍵字。')
