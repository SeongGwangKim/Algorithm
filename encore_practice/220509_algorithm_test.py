# 네이버 웹툰 알고리즘 문제
'''
# - 웹툰의 제목, 작가, 장르 정보를 가지는 테이블(A)과
#  유저의 웹툰 작품별 별점 정보를 가지는 테이블(B)이 있습니다.
#  평균 별점이 가장 높은 작품 3개를 조회하는 쿼리를 작성해 주세요.

select A.제목, A.작가, A.장르, B.별점, Count(*)
from table_A A
left join table_B B
On A.제목 = B.제목
group by B.별점
having count(*) <= 3
Order by B.별점 Desc;

# - 단어에 나오는 모음의 순서를 바꾸는 함수를 만들어보세요.
# ex) naver webtoon => novor webtean

S = 'naver webtoon'
S_list = list(S)
print(len(S_list))
temp1 = S[1:2]
temp2 = S[3:4]
temp3 = S[10:11]
S_list[1] = temp3
S_list[3] = temp3
S_list[10] = temp2
S_list[11] = temp1

'''








'''
q) 다음 3개 DB 테이블에 관계성을 부여해주세요 

artist 
ㄴ artist_id(PK)
ㄴ artist_name `조석`

title 
ㄴ title_id(FK)
ㄴ title_name `마음의소리`

realation_table
ㄴ artist_id
ㄴ title_id

episode `1화`
ㄴ epiosde_id 



select C.title_name
from relation_table C
rigt join title B
on B.title_id = C.title_id
join artist A
on A.artist_id = C.artist_id

'''



# Q> a = b + 1과 같이 assign은 허용이 되지만, 한번 a에 값이 assign 되면
#  a는 다른 값으로 바꿀 수 없는 언어가 있습니다.
#  임의의 정수 N부터 M까지 더하는 프로그램을 작성해주세요.

'''
def su_add(N, M):
    N += 1
    if N == M:
        break
    else:
        N += 1
        su_add(N, M)
    return N
'''

# Q) 웹툰 테이블 (웹툰 ID, 작가ID) , 구매 테이블 (구매번호, 웹툰 ID, 구매자ID, 구매날짜)이 있다.
# 작가별로 가장 많이 판매된 TOP10 작품을 뽑는 쿼리 작성부탁드립니다.

'''
select A.작가ID, count(*)
from 웹툰_테이블 A
rigt join 구매_table B
on A.웹툰ID = B.웹툰ID
group by 작가ID
having count(*) <= 10
order by count(*) desc;
'''