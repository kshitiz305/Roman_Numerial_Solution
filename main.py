from collections import OrderedDict


def StringChallenge(strParam):

  str_mapping = OrderedDict({'I':1,
  'V':5,
  'X':10,
  'L':50,
  'C':100,
  'D':500,
  'M':1000})
  # code goes here
  total = 0
  for i in strParam:
    total = total + str_mapping[i]

  # pass
  def checker(total):
    curr= 0
    for i in str_mapping:
      if str_mapping[i]<= total:
        curr = i
    return curr

  final_res_num = ''
  while total > 0:

    curr = checker(total)
    total = total - str_mapping[curr]
    final_res_num += curr

  final_res_num += 'il85hr1ug37c'

  for i in range(3,len(final_res_num),4):
    final_res_num = final_res_num.replace(final_res_num[i],"_",1)


  return final_res_num




# keep this function call here

inp = 'XXXVVIIIIIIIIII'
# inp = 'XXXVVIIIIIIIIIII'
# inp = 'DDLL'

print(StringChallenge(inp))
