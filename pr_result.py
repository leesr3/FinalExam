# 사용자의 답변을 토대로 분석결과 출력

def pr_result(answer):
    if answer[1] == '1':
        print("무조건 광고입니다! 실제로 홍길동은 존재하지 않아요! "
              "아무리 교통이 발달되었다고 해도 홍길동처럼 말도안되는 동선으로 밥을 먹을 수는 없겠죠? \n"
              "대부분 업체에서 정보를 모두 제공받아 다녀온 척을 하는 광고글이랍니다! 가지마세요!\n"
              "특정지역에서 꾸준히 포스팅이 올라오는 블로그가 진짜 맛집을 리뷰할 확률이 더 높아요")
    elif answer.count('1') > 3:
        print("소문난 잔치에 먹을것 없다... 이곳은 그럴 확률이 매우 높은 곳입니다.\n"
              "바이럴 마케팅 수법으로 할 수있는건 모든 다 하는 곳이예요! 믿지마세요!\n")
    elif answer.count('1') > 2:
        print("흠...업체랑 제휴 맺은 광고글 보다는 검색 상위 랭킹을 꿈꾸는 포스팅일 수 있어요\n"
              "다른 블로그에서도 해당 맛집 포스팅을 SoroMon에게 분석 요청 해보시고 결정하세요!\n")
    else:
        print("담백한 느낌의 포스팅이네요! 이 포스팅에서는 광고성이 전혀 느껴지지 않아요 블로거의 진지한 견해가\n"
              "들어갔을 확률이 높아요 별다른 혹평이 없다면 방문해봐도 좋겠어요!^^ 맛집 찾기 화이팅!\n")
