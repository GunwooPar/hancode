from rich.live import Live
from rich.table import Table
import time

# 표시할 테이블 객체 생성
table = Table()
table.add_column("항목")
table.add_column("값")

# Live 객체로 테이블을 감싸줍니다.
with Live(table, screen=True, refresh_per_second=10) as live:
    # 루프 안에서 테이블의 내용만 계속 바꿔주면...
    for i in range(1, 101):
        # 기존 행을 지우고
        table.rows.clear()
        
        # 새로운 행을 추가
        table.add_row("값 1", str(i * 10))
        table.add_row("값 2", str(i * 20))
        table.add_row("값 3", str(i * 30))
        
        # rich 라이브러리가 알아서 화면 깜빡임 없이 업데이트합니다.
        time.sleep(0.05)