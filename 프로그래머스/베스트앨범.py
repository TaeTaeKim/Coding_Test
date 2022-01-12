def solution(genres, plays):
    answer = []
    # 각 장르별 플레이 횟수
    album = {}
    # 곡의 플레이 횟수 순으로 정렬
    for i,(g,p) in enumerate(zip(genres,plays)):
        if g in album.keys():
            album[g][0] +=p
            album[g][1].append((i,p))
        else:
            album[g] = [p,[(i,p)]]
    # 모든 곡을 플레이 횟수 순으로 정렬
    album = sorted(album.items(),key=lambda x:x[1][0],reverse=True)
    for i in album:
        songs = sorted(i[1][1],key=lambda x:x[1],reverse=True)[:2]
        for j in songs:
            answer.append(j[0])
    return answer

# 해쉬를 쓰는 dict의 함수와 정렬에서의 key를 lambda함수를 이용한 방법을 숙달.