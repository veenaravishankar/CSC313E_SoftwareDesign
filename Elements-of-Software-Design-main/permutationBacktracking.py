def permutation(permuteList,start, end):
    if start == end:
        print(permuteList)
    else:
        for i in range(start,end+1):
            #swap
            permuteList[start],permuteList[i] = permuteList[i],permuteList[start]
            permutation(permuteList,start+1,end)
            #backtrack or swap back
            permuteList[start],permuteList[i] = permuteList[i],permuteList[start]


permutation(['B','E','V'],0,2)