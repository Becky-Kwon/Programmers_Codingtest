def solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
    # 장르를 조회수 합산 값 순으로 sort 를 한번에 함.
    genreSort =sorted(set(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    print("genreSort : ",genreSort)
    for g in genreSort:
        # 튜플 형태일때 첫번째 요소를 기준으로 정렬하고 
        # 첫번째 요소가 같은 경우 두번째 요소를 기준으로 정렬하는 원리를 이용
        # -를 붙인것은 고유번호가 낮은 것을 크다고 보기에
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    return answer
  
  
def solution(genres, plays):
  genre_list = list(set(genres))
  genre_play = {}
  genre_table = {}
  genre_play_list_ = {}
  play_genre = {}
  result = []
  for genre in genre_list:
      genre_play[genre] = 0
      genre_play_list_[genre] = []
      genre_table[genre] = {}
  for i in range(len(plays)):
      genre_play[genres[i]] += plays[i]
      genre_play_list_[genres[i]].append(plays[i])
      genre_table[genres[i]][i] = plays[i]
  play_genre = {v:k for k,v in genre_play.items()}
  genre_top = [play_genre[x] for x in sorted(list(play_genre.keys()), reverse = True)]

  for gen in genre_top:
      if len(genre_play_list_[gen]) >=2:
          song_list_sort = sorted(genre_play_list_[gen], reverse = True)[:2]
          # 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
          if song_list_sort[0] == song_list_sort[1]:
              song_2 = sorted([k for k, v in genre_table[gen].items() if v == song_list_sort[0]])
              result.extend(song_2)
          else : 
              for song in song_list_sort:
                  result.extend([k for k, v in genre_table[gen].items() if v == song])
      else : result.extend(list(genre_table[gen].keys()))

  return result
