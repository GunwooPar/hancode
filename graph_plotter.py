import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

def plot_cpm_history(time_data, cpm_data, parent_geometry=None):
    """
    시간(x축)과 타수(y축) 리스트를 받아 그래프를 생성하고 화면에 표시합니다.
    parent_geometry 정보를 받아 그래프 창의 위치를 조정합니다.
    """
    try:
        # 한글 폰트 설정
        font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
        rc('font', family=font_name)
    except FileNotFoundError:
        print("맑은 고딕 폰트를 찾을 수 없습니다. 기본 폰트로 그래프를 그립니다.")
        # Mac이나 Linux 사용자를 위한 예외 처리도 추가할 수 있습니다.
        pass

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(time_data, cpm_data, marker='o', linestyle='-', color='#88C0D0')
    
    ax.set_title('타속 변화 그래프 (CPM)', fontsize=16)
    ax.set_xlabel('시간 (초)', fontsize=12)
    ax.set_ylabel('타수 (CPM)', fontsize=12)
    
    # 그래프 스타일링
    ax.set_facecolor('#2E3440') # 배경색
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#D8DEE9')
    ax.spines['bottom'].set_color('#D8DEE9')
    ax.tick_params(axis='x', colors='#D8DEE9')
    ax.tick_params(axis='y', colors='#D8DEE9')
    ax.title.set_color('#ECEFF4')
    ax.xaxis.label.set_color('#ECEFF4')
    ax.yaxis.label.set_color('#ECEFF4')

    ax.grid(True, color='#4C566A', linestyle='--', linewidth=0.5)
    plt.tight_layout()
    
    if parent_geometry:
        # [수정] 화면에 잘리지 않도록 그래프 창의 크기와 위치를 조정합니다.
        manager = plt.get_current_fig_manager()
        parent_x, parent_y, parent_width, _ = parent_geometry
        
        MARGIN = 20  # gui_app.py와 동일한 간격
        graph_width, graph_height = 700, 500 # 수정한 그래프 창 크기

        # 부모 창 오른쪽에 간격을 두고 위치
        graph_x = parent_x + parent_width + MARGIN
        
        # 두 창의 상단 y좌표를 맞춤
        graph_y = parent_y
        
        try:
            manager.window.setGeometry(graph_x, graph_y, graph_width, graph_height)
        except Exception as e:
            print(f"그래프 창 위치 조정 중 오류 발생: {e}")
            pass

    plt.show()

if __name__ == '__main__':
    # 테스트용 데이터
    test_time = [i * 0.1 for i in range(10)]
    test_cpm = [120, 150, 180, 220, 210, 250, 230, 280, 260, 300]
    plot_cpm_history(test_time, test_cpm) 