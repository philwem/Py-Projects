def cal_average_score():
  score_list = []
  for i in range(5):
    score = int(input(f"Enter score {i + 1}"))
    score_list.append(score)
    print(f"Scores : {score_list}") 
