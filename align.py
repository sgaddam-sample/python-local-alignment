import sys

#v and w are sequences
def LCSBacktrack( v, w ):
    sigma = 5
    s = make_mat(len(w) +1, len(v) + 1)
    backtrack = make_mat(len(w)+1, len(v) +1)

    for i in range(len(w) + 1):
        s[i][0]= 0
        backtrack[i][0] = 0

    for j in range(len(v)+1):
        s[0][j] = 0
	
    backtrack[0][j] = 1
    down = right = diagonal = 0
    for i in range(1, len(w)+1):
        for j in range(1, len(v)+1):
            
            down = s[i-1][j] - sigma
            right = s[i][j-1] - sigma
            mu = score[blosum[v[j-1]]][blosum[w[i-1]]]
            diagonal = s[i-1][j-1] + mu
            s[i][j] = max(down, right, diagonal)

            if s[i][j] == down:
                backtrack[i][j] = "down"
            elif s[i][j] == right:
                backtrack[i][j] = "right"
            else:
                backtrack[i][j] = "diagonal"
    
    max_score = 0
    for i in range(len(w)+1):
        for j in range(len(v)+1):
            if s[i][j] > max_score:
                i_max = i
                j_max = j
                max_score = s[i][j]
    
    print max_score
    return backtrack

def outputLCS( backtrack, v, j, i):
    s1 = s2 = ""
    while i*j != 0:
        if backtrack[i][j] == -1:
            break
        elif backtrack[i][j] == "down":
            s1 += '-'
            s2 += str(w[i-1])
            i = i - 1
        elif backtrack[i][j] == "right":
            s1 += str(v[j-1])
            s2 += '-'
            j = j-1
        else:
            s1 += str(v[j-1])
            s2 += str(w[i-1])
            i = i-1
            j = j-1
    
    print s1[::-1]
    print s2[::-1]

# process input 2 sequence file 
with open (sys.argv[1]) as filename:
    v = filename.readline().rstrip()
    w = filename.readline().rstrip()

# process blosum file
filename2 = open("blosum.txt")
f2 = filename2.readline().replace("  "," ").rstrip().replace("  ", "").split(" ")

i = 0
blosum = {}
for char in f2:
    blosum[char] = i
    i += 1

score = []
for line in filename2.readlines():
    score_i = line.rstrip().replace('  ',' ').split(' ')
    score.append([int(f2) for f2 in score_i[1:]])

backtrack = LCSBacktrack(v, w)
print outputLCS(backtrack, v, len(v), len(w))
