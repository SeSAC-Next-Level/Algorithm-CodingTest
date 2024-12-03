from datetime import datetime
import sys

# 입력을 빠르게 받기 위해 sys.stdin.readline 사용
input = sys.stdin.readline

# 검색 조건 입력
start_time_str, end_time_str, keyword = input().strip().split()

# 시간 파싱
start_time = datetime.strptime(start_time_str, "%H:%M:%S").time()
end_time = datetime.strptime(end_time_str, "%H:%M:%S").time()

# 로그 개수 입력
N = int(input())

# 변수 초기화
logs_by_category = {'INFO': [], 'WARN': [], 'ERROR': []}

prev_log = None  # 이전 로그를 추적하기 위한 변수
prev_filtered = False  # 이전 로그가 필터링되었는지 여부

for _ in range(N):
    # 각 로그 읽기 및 파싱
    log_line = input().strip()
    if not log_line:
        continue  # 빈 줄은 스킵
    try:
        time_str, category_with_bracket, content = log_line.split(' ', 2)
    except ValueError:
        continue  # 잘못된 형식의 로그 라인은 스킵
    log_time = datetime.strptime(time_str, "%H:%M:%S").time()
    category = category_with_bracket.strip('[]')
    content_str = content.strip()

    # 시간 필터링 적용
    if log_time < start_time or log_time > end_time:
        prev_filtered = False
        continue

    # 키워드 필터링 적용 (대소문자 구분 없음, 부분 일치)
    if keyword.lower() not in content_str.lower():
        prev_filtered = False
        continue

    # 필터링 조건에 부합하는 로그 처리

    # 이전 로그와 비교하여 압축 가능 여부 확인
    if prev_filtered and prev_log and prev_log['category'] == category and prev_log['content'] == content_str:
        # 이전 로그의 카운트 증가
        prev_log['count'] += 1
    else:
        # 새로운 로그 항목 추가
        log_entry = {
            'time': log_time,
            'time_str': time_str,
            'category': category,  # 'category' 키 추가
            'content': content_str,
            'count': 1
        }
        logs_by_category[category].append(log_entry)
        prev_log = log_entry
    prev_filtered = True  # 현재 로그는 필터링되었음

# 출력 준비
output_lines = []

# 로그분류 순서 정의
category_order = ['INFO', 'WARN', 'ERROR']

logs_found = False  # 필터링된 로그가 있는지 확인

for category in category_order:
    if logs_by_category[category]:
        logs_found = True
        output_lines.append(f'[{category}]:')
        for log in logs_by_category[category]:
            # 로그 라인 준비
            count_str = f" (x{log['count']})" if log['count'] > 1 else ''
            output_lines.append(f"- {log['time_str']}: {log['content']}{count_str}")
        output_lines.append('')  # 각 카테고리 후 빈 줄 추가

if not logs_found:
    print("No logs found.")
else:
    # 출력
    print('\n'.join(output_lines).strip())
