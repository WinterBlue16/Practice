# 코딩테스트 복기
# x개의 스포츠 팀이 각각 두 번씩 경기를 한다. input으로 팀의 갯수 x와 경기한 팀, 각 팀의 점수를 x*(x-1)만큼 준다.
# 출력 시가장 이긴 횟수가 많은 팀부터 순서대로 나열되게 하고, 형식은 '팀 이름', '이긴 횟수', '이긴 횟수에서 패한 횟수를 뺀 숫자'로 한다.
# 이긴 횟수가 같을 때는 이긴횟수에서 패한 횟수를 뺀 숫자로 비교한다.


# input으로 팁 갯수 넣기
team_num = int(input())

# 경기 횟수
n = team_num*(team_num-1)

# 이긴 팀이 모이는 리스트와 패배한 팀이 모이는 리스트 생성
winner_team = []
loser_team = []

# 경기 횟수만큼 input을 주고 이긴 팀의 이름을 리스트에 append 한다
for i in range(n):
    team1, score1, team2, score2 = input().split()

    # team 1이 이겼을 때
    if score1 > score2:
        winner_team.append(team1)
        loser_team.append(team2)

    # team 2가 이겼을 때
    if score1 < score2:
        winner_team.append(team2)
        loser_team.append(team1)

# 가장 많이 이긴 팀 찾기
from collections import Counter

count_winner = Counter(winner_team)
count_loser = Counter(loser_team)


# 가장 많이 이긴 팀부터 팀 이름, 이긴 횟수, 이긴 횟수에서 패한 횟수 뺀 숫자 출력
for key, value in count_winner.items():
    win_minus_lose = value - count_loser[key]
    print(key, value, win_minus_lose)
