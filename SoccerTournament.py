import sys

def AverageConceded(N, W, D, X, scored, conceded, points):
  games = [N-1] * N
  results = []
  concededLoc = []
  for i in range(0,len(conceded)):
    concededLoc.append(conceded[i])
  for i in range(0,N-1):#lower number team
    for j in range(i+1,N):#higher number team
      score2 = int(concededLoc[i]/games[i])
      score1 = int(concededLoc[j]/games[j])
      concededLoc[i] -= score2
      concededLoc[j] -= score1
      games[i] -= 1
      games[j] -= 1
      results.append(str(score1)+" "+str(score2))
  return results

###############################################################################################

def CorrectResults(results,scored,conceded):
  N = len(scored)
  count = 0
  while True:
    count += 1
    scoredGuess = [0] * N
    concededGuess = [0] * N
    i = 0
    j = 0
    for k in range(0,len(results)):
      scoredGuess[i] += int(results[k][0])
      scoredGuess[j] += int(results[k][2])
      concededGuess[i] += int(results[k][2])
      concededGuess[j] += int(results[k][0])

      j += 1
      if j == N:
        i += 1
        j = i + 1
    if count == 100:
      return results
    #print(scoredGuess)
    #print(scored)
    for i in range(0,N-1):#lower number team
      for j in range(i+1,N):#higher number team
        if scoredGuess[i] > scored[i] and scoredGuess[j] > scored[j] and int(results[(i*(N-1))+j-1-int(i*(i+1)/2)][0]) > 0 and int(results[(i*(N-1))+j-1-int(i*(i+1)/2)][2]) > 0:
          results[(i*(N-1))+j-1-int(i*(i+1)/2)] = str(int(results[(i*(N-1))+j-1-int(i*(i+1)/2)][0])-1)+" "+str(int(results[(i*(N-1))+j-1-int(i*(i+1)/2)][2])-1)
        elif scoredGuess[i] > scored[i] and int(results[(i*(N-1))+j-1-int(i*(i+1)/2)][0]) > int(results[(i*(N-1))+j-1-int(i*(i+1)/2)][2]) + 1 and int(results[(i*(N-1))+j-1-int(i*(i+1)/2)][0]) > 1:
          results[(i*(N-1))+j-1-int(i*(i+1)/2)] = str(int(results[(i*(N-1))+j-1-int(i*(i+1)/2)][0])-1)+" "+results[(i*(N-1))+j-1-int(i*(i+1)/2)][2]
        elif scoredGuess[j] > scored[j] and int(results[(i*(N-1))+j-1-int(i*(i+1)/2)][0]) + 1 < int(results[(i*(N-1))+j-1-int(i*(i+1)/2)][2]) and int(results[(i*(N-1))+j-1-int(i*(i+1)/2)][2]) > 1:
          results[(i*(N-1))+j-1-int(i*(i+1)/2)] = results[(i*(N-1))+j-1-int(i*(i+1)/2)][0]+" "+str(int(results[(i*(N-1))+j-1-int(i*(i+1)/2)][2])-1)

        elif scoredGuess[i] < scored[i] and scoredGuess[j] < scored[j] and int(results[(i*(N-1))+j-1-int(i*(i+1)/2)][0]) < 3 and int(results[(i*(N-1))+j-1-int(i*(i+1)/2)][2]) < 3:
          results[(i*(N-1))+j-1-int(i*(i+1)/2)] = str(int(results[(i*(N-1))+j-1-int(i*(i+1)/2)][0])+1)+" "+str(int(results[(i*(N-1))+j-1-int(i*(i+1)/2)][2])+1)
        elif scoredGuess[i] < scored[i] and int(results[(i*(N-1))+j-1-int(i*(i+1)/2)][0]) > int(results[(i*(N-1))+j-1-int(i*(i+1)/2)][2]) + 1 and int(results[(i*(N-1))+j-1-int(i*(i+1)/2)][0]) < 2:
          results[(i*(N-1))+j-1-int(i*(i+1)/2)] = str(int(results[(i*(N-1))+j-1-int(i*(i+1)/2)][0])+1)+" "+results[(i*(N-1))+j-1-int(i*(i+1)/2)][2]
        elif scoredGuess[j] < scored[j] and int(results[(i*(N-1))+j-1-int(i*(i+1)/2)][0]) + 1 < int(results[(i*(N-1))+j-1-int(i*(i+1)/2)][2]) and int(results[(i*(N-1))+j-1-int(i*(i+1)/2)][2]) < 2:
          results[(i*(N-1))+j-1-int(i*(i+1)/2)] = results[(i*(N-1))+j-1-int(i*(i+1)/2)][0]+" "+str(int(results[(i*(N-1))+j-1-int(i*(i+1)/2)][2])+1)

def FindResults(options,results,N):
  notdone = 0
  for i in range (0,len(options)):
    if options[i][0] != -10:
      notdone += 1
  if notdone <= 1:
    return results
  biggest = 0
  bigi = 0
  bigj = 0
  for i in range(0,len(options)):
    for j in range(0,3):
      if options[i][j] > biggest:
        biggest = options[i][j]
        bigi = i
        bigj = j
  middest = 0
  midj = 0
  smallest = 9999
  for j in range(0,3):
    if j != bigj:
      if options[bigi][j] > middest:
        middest = options[bigi][j]
        midj = j
      if options[bigi][j] < smallest:
        smallest = options[bigi][j]
  if smallest > 0:
    return "" #can't be bothered to deal with situations of all 3
  else:
    for i in range(0,len(options)):
      if i < bigi:
        if options[i][2-bigj] > 0:
          options[i][2-bigj] -= 1
          biggest -= 1
          results[(i*(N-1))+bigi-1-int(i*(i+1)/2)] = str(bigj)+" "+str(2-bigj)
          #print((i*(N-1))+bigi-1-int(i*(i+1)/2),i,bigi,str(bigj)+" "+str(2-bigj))
        elif options[i][2-midj] > 0 and middest > 0:
          options[i][2-midj] -= 1
          middest -= 1
          results[(i*(N-1))+bigi-1-int(i*(i+1)/2)] = str(midj)+" "+str(2-midj)
          #print((i*(N-1))+bigi-1-int(i*(i+1)/2),i,bigi,str(midj)+" "+str(2-midj))
        elif options[i][0] != -10:
          return ""
      elif i > bigi:
        if options[i][2-bigj] > 0:
          options[i][2-bigj] -= 1
          biggest -= 1
          results[(bigi*(N-1))+i-1-int(bigi*(bigi+1)/2)] = str(2-bigj)+" "+str(bigj)
          #print((i*(N-1))+bigi-1-int(i*(i+1)/2),i,bigi,str(2-bigj)+" "+str(bigj))
        elif options[i][2-midj] > 0 and middest > 0:
          options[i][2-midj] -= 1
          middest -= 1
          results[(bigi*(N-1))+i-1-int(bigi*(bigi+1)/2)] = str(2-midj)+" "+str(midj)
          #print((i*(N-1))+bigi-1-int(i*(i+1)/2),i,bigi,str(2-midj)+" "+str(midj))
        elif options[i][0] != -10:
          return ""
    if biggest < 0:
      for i in range(0,len(options)):
        if i < bigi:
          if options[i][2-midj] > 0 and middest > 0 and results[(i*(N-1))+bigi-1-int(i*(i+1)/2)] != str(midj)+" "+str(2-midj):
            options[i][2-midj] -= 1
            middest -= 1
            results[(i*(N-1))+bigi-1-int(i*(i+1)/2)] = str(midj)+" "+str(2-midj)
            #print((i*(N-1))+bigi-1-int(i*(i+1)/2),i,bigi,str(midj)+" "+str(2-midj))
        elif i > bigi:
          if options[i][2-midj] > 0 and middest > 0 and results[(bigi*(N-1))+i-1-int(bigi*(bigi+1)/2)] != str(2-midj)+" "+str(midj):
            options[i][2-midj] -= 1
            middest -= 1
            results[(bigi*(N-1))+i-1-int(bigi*(bigi+1)/2)] = str(2-midj)+" "+str(midj)
            #print((i*(N-1))+bigi-1-int(i*(i+1)/2),i,bigi,str(2-midj)+" "+str(midj))
    if middest != 0:
      return ""
    options[bigi] = [-10,-10,-10]
    return FindResults(options,results,N)
  
def FindWinners(N, W, D, X, scored, conceded, points):
  results = []
  for i in range(0,N):
    results.append([])
    for w in range(0,int(points[i]/W)+1):
      d = int((points[i]-(w*W))/D)
      if (w * W) + (d * D) == points[i] and w + d < N:
        results[i].append([w,d,N-w-d-1])

##  combinations = 1
##  for i in range(0,N):
##    combinations *= len(results[i])
##  print(combinations)
##  sys.stdout.flush()
  
  pos = [0]*N
  options = []
  done = False
  while not done:
    wins = 0
    losses = 0
    for j in range(0,N):
      wins += results[j][pos[j]][0]
      losses += results[j][pos[j]][2]
    if wins == losses:
      options.append([])
      for j in range(0,N):
        options[-1].append(results[j][pos[j]])
    for j in range(N-1,-1,-1):
      if pos[j] != len(results[j]) - 1:
        pos[j] += 1
        break
      else:
        pos[j] = 0
        if j == 0:
          done = True
  #print(options)

  for i in range(0,len(options)):
    results = [""] * int(N*(N-1)/2)
    respot = FindResults(options[i],results,N)
    if respot != "":
      return respot
  return ""

#############################################################################################
   
def CorrectGuess(N, W, D, X, scored, conceded, points):
  baseline = AverageConceded(N, W, D, X, scored, conceded, points)
  count = 0

  while True:
    count += 1
    if count > 100:
      return baseline
    scoredGuess = [0] * N
    concededGuess = [0] * N
    pointsGuess = [0] * N
    i = 0
    j = 0
    for k in range(0,len(baseline)):
      scoredGuess[i] += int(baseline[k][0])
      scoredGuess[j] += int(baseline[k][2])
      concededGuess[i] += int(baseline[k][2])
      concededGuess[j] += int(baseline[k][0])
      if int(baseline[k][0]) > int(baseline[k][2]):
        pointsGuess[i] += W
      elif int(baseline[k][2]) > int(baseline[k][0]):
        pointsGuess[j] += W
      else:
        pointsGuess[i] += D
        pointsGuess[j] += D

      j += 1
      if j == N:
        i += 1
        j = i + 1

    for i in range(0,N-1):#lower number team
      for j in range(i+1,N):#higher number team
        if pointsGuess[i] > points[i] and scoredGuess[i] > scored[i] and concededGuess[j] > conceded[j] and pointsGuess[j] < points[j] and int(baseline[(i*(N-1))+j-1-int(i*(i+1)/2)][0]) > 0:
          baseline[(i*(N-1))+j-1-int(i*(i+1)/2)] = str(int(baseline[(i*(N-1))+j-1-int(i*(i+1)/2)][0])-1)+" "+baseline[(i*(N-1))+j-1-int(i*(i+1)/2)][2]#i-=1
        elif pointsGuess[i] > points[i] and scoredGuess[j] < scored[j] and concededGuess[i] < conceded[i] and pointsGuess[j] < points[j] and int(baseline[(i*(N-1))+j-1-int(i*(i+1)/2)][2]) < 3:
          baseline[(i*(N-1))+j-1-int(i*(i+1)/2)] = baseline[(i*(N-1))+j-1-int(i*(i+1)/2)][0]+" "+str(int(baseline[(i*(N-1))+j-1-int(i*(i+1)/2)][2])+1)#j+=1
        elif pointsGuess[i] < points[i] and scoredGuess[i] < scored[i] and concededGuess[j] < conceded[j] and pointsGuess[j] > points[j] and int(baseline[(i*(N-1))+j-1-int(i*(i+1)/2)][0]) < 3:
          baseline[(i*(N-1))+j-1-int(i*(i+1)/2)] = str(int(baseline[(i*(N-1))+j-1-int(i*(i+1)/2)][0])+1)+" "+baseline[(i*(N-1))+j-1-int(i*(i+1)/2)][2]#i+=1
        elif pointsGuess[i] < points[i] and scoredGuess[j] > scored[j] and concededGuess[i] > conceded[i] and pointsGuess[j] > points[j] and int(baseline[(i*(N-1))+j-1-int(i*(i+1)/2)][2]) > 0:
          baseline[(i*(N-1))+j-1-int(i*(i+1)/2)] = baseline[(i*(N-1))+j-1-int(i*(i+1)/2)][0]+" "+str(int(baseline[(i*(N-1))+j-1-int(i*(i+1)/2)][2])-1)#j-=1
       
def findSolution(N, W, D, X, scored, conceded, points):
  if N < 15:
    solWinners = FindWinners(N, W, D, X, scored, conceded, points)
    if solWinners != "":
      solWinners = CorrectResults(solWinners,scored,conceded)
      return solWinners
  return CorrectGuess(N, W, D, X, scored, conceded, points)

N = int(input())#number of teams 6 - 50
W = int(input())#points for winning 2 - 6
D = int(input())#points for draw 1 - W-1
X = int(input())#number of simulations per game 1 - 10
#attack strength 2 - 10, defense strength 1 - 10

scored = [0] * N
conceded = [0] * N
points = [0] * N
for i in range(N):
  temp = input().split()
  scored[i] = int(temp[0])
  conceded[i] = int(temp[1])
  points[i] = int(temp[2])

#ret = findSolution(6, 3, 1, 1, [5,4,6,9,4,11], [10,12,4,4,5,4], [2,1,10,9,5,13])
ret = findSolution(N, W, D, X, scored, conceded, points)

print(len(ret))
for st in ret:
  print(st)
sys.stdout.flush()

#cd Documents/TopCoder/121
#java -jar SoccerTournament.jar -exec "python SoccerTournament.py" -seed 1 -debug
"""
1: 7    21
2: 1003 1030
3: 108  239
4: 579  530
5: 1052 1156
6: 53   69
7: 532  360
8: 955  1210
9: 750  756
"""

#11,521,044,102,683,491,968,301,186,185,806,402,494,141,970,566,348,800,000,000 1x10^58
