#Exercise 4

def levenshtein_distance(source, target):
  distance = []
  for idx in range(len(source)+1):
    row = [0]*(len(target)+1)
    distance.append(row)

  for idx in range(len(source)+1):
    distance[idx][0] = idx
  for idx in range(len(target)+1):
    distance[0][idx] = idx


  for idx in range(1, len(source)+1):
    for jdx in range(1, len(target)+1):
      if source[idx-1] == target[jdx-1]:
        distance[idx][jdx] = distance[idx-1][jdx-1]
      else:
        del_cost = distance[idx-1][jdx] + 1
        ins_cost = distance[idx][jdx-1] + 1
        sub_cost = distance[idx-1][jdx-1] + 1

        if (del_cost <= ins_cost and del_cost <= sub_cost):
          distance[idx][jdx] = del_cost
        elif (ins_cost <= del_cost and ins_cost <= sub_cost):
          distance[idx][jdx] = ins_cost
        else:
          distance[idx][jdx] = sub_cost

  return distance[len(source)][len(target)]

assert levenshtein_distance('hi', 'hello') == 4
print (levenshtein_distance('yen', 'you'))
