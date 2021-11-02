# [leo, kiki, eden]	[eden, kiki]	leo
# [marina, josipa, nikola, vinko, filipa]	[josipa, filipa, marina, nikola]	vinko
# [mislav, stanko, mislav, ana]	[stanko, ana, mislav]	mislav

participant = ['leo', 'kiki', 'eden']
completion = ['eden', 'kiki'   ]


def solution(participant, completion):
    answer = ''
    sorted_participant = sorted(participant)
    sorted_completion = sorted(completion)
    print(sorted_completion, sorted_participant)
    for i in range(len(sorted_participant)-1):
      if(sorted_participant[i] != sorted_completion[i]  ):
        answer = sorted_participant[i]
        print(answer)
    # return answer


solution(participant, completion)