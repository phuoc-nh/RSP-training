from collections import Counter

def solution(letters):
    cnt = Counter(letters)
    sorted_cnt = cnt.most_common()
    print(sorted_cnt)
    
    res = 0

    for i in range(len(sorted_cnt)):
        if i >= 0 and i <= 8:
            res += sorted_cnt[i][1] * 1
        elif i >= 9 and i <= 17:
            res += sorted_cnt[i][1] * 2
		else:
			res += sorted_cnt[i][1] * 3
		
		
			
		
			
		


letters = "abcghdiefjoba"
solution(letters)