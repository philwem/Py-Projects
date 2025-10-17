def cal_average_score():
    score_list = []
    for i in range(5):
        score = int(input(f"Enter score {i + 1}"))
        score_list.append(score)
    
    print(f"Scores : {score_list}") 

    ave_score = sum(score_list)/len(score_list)
    print(f"Average Score : {ave_score}")
    
    high_score = max(score_list)
    print(f"Highest Score : {high_score}")
cal_average_score()