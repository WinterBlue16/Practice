# 코딩테스트 복기
# 잊어버릴까봐 미리 적어둔다

# 암호 형태에 따라 level 매기고 출력하기
# 조건은 다음과 같다 아래의 다섯 조건 중 해당되는 것만큼 level이 올라간다

# 영어 소문자 포함
# 영어 대문자 포함
# 특수문자 포함
# 숫자(0~9) 포함
# 자릿수 10개 이상

# 예를 들어보면, 13233의 경우 숫자로만 이루어져 있으므로 level 1이다.
# 반면 12#rPkdgdss;5의 경우 위의 다섯조건을 모두 충족하므로 level 5가 된다


# 암호 입력
user_input = input()

# 암호 리스트로 만들기
password_li = list(user_input)

# 암호를 검사할 리스트 만들기
import string

# 영어 대문자
upper = list(string.ascii_uppercase)
# 영어 소문자
lower = list(string.ascii_lowercase)
# 숫자 리스트
number = []
for i in range(10):
    number.append(i)


# 레벨 카운트
level_count = 0


# 가장 큰 조건부터 처리
# 자릿수가 10보다 작은 경우
if len(password_li) < 10: # level_count=0
    for p in password_li:
        if p not in upper and lower and number:
            level_count += 1 # level_count=1
            break


        else: # level_count=0
            if any(p in upper) or lower or number:
                level_count+=2 # level_count=3
            elif (p not in upper and lower) or (p not in upper and number) or (p not in number and lower):
                level_count+=1
            else:
                level_count+=3
            print('LEVEL{}'.format(level_count))
            
