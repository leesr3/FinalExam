"""

File: main.py
----------------
과제 final : SoroMon
이름: 이소리
학번: 2017052951
무분별한 맛집 소개글이 광고인지 아닌지 구분해주는 프로그램.

"""
from crawling import save_tags
from pr_result import pr_result


def main():

    answer = []  # 사용자 답변을 받기 위한 list

    print("★★더 이상 광고 글에 속지 마세요. 'SoroMon'이 광고로부터 해방되도록 도와드릴게요.★★")
    print("★★감별하고 싶은 블로그 주소의 'blog' 부분부터 복사하여 입력해주세요.★★")
    url = "https://" + input("=> https:// ")
    # https://부터 복사 붙여넣기 시 새창이 열리므로, 이를 방지.

    # 맛집 소개글에서 광고글을 구분하는 주요 확인 사항
    print("★아래의 질문에 따라 블로그 내용을 확인한 후, (예/아니요)로 대답해주세요.")

    print("★문의하신 게시글에서 반복적으로 사용된 키워드 50개를 빈도순으로 나열하는 중이예요.")

    save_tags(url)  # url의 본문중 자주 사용한 단어와 그 빈도수를(tags) 파일에 저장(save).

    f = open('cnouns_list.txt', 'r', encoding='utf-8')
    lines = f.read()
    print(lines)
    f.close()

    print("★1번: 가게 이름이 상위에 속해있나요?")
    answer += [input("1.예 / 2. 아니요 =>")]

    print("★2번: 블로그 목록을 확인해보세요. 며칠사이에 블로그지기가 동에번쩍! 서에번쩍! 홍길동처럼 이동하고 있지 않나요?")
    answer += [input("1.예 / 2. 아니요 =>")]

    print("★3번: 주소, 오픈마감시간, 정기 휴무일, 전화번호등의 정보가 마치 주인이 작성한 것처럼 너무 상세하지 않나요?")
    answer += [input("1.예 / 2. 아니요 =>")]

    print("★4번: 사진이 너무 자세하거나 해상도가 높은가요?")
    answer += [input("1.예 / 2. 아니요 =>")]

    print("★5번: 존맛탱!등의 비속어 표현은 눈씻고도 찾아볼 수 없나요?")
    answer += [input("1.예 / 2. 아니요 =>")]

    pr_result(answer)  # 결과 분석 출력


if __name__ == '__main__':
    main()



