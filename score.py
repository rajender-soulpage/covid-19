import random
#different answer importants score dict.
gender_sy_answer = {"Male":0.60,"Female":0.30,"Others":0.10}

common_sy_answer = {"None":0,"Fever": 0.30, "Dry cough": 0.40,"Tiredness": 0.30}

less_common_sym_answer = {"None":0 ,"Aches & Pain": 0.10 ,"Sore Throat": 0.30 ,"Diarrhoea": 0.10,"Conjunctivitis": 0.10,"Headache": 0.05 ,"Loss of taste or smell": 0.30,"A rash on skin, or discolouration of fingers or toes": 0.05}

Serious_sym_answer = {"None":0,"Difficulty breathing or shortness of breath": 0.20,"Chest pain or pressure": 0.20,"Loss of speech or movement": 0.60}

pre_existing_health_answer = {"None":0,"Hypertension": 0.20,"High blood pressure":0.30,"Diabetes":0.05,"Lung disease": 0.30,"Dementia": 0.02,"Heart attacks": 0.30,"Other heart disease": 0.30,"Active cancer": 0.50,"Chronic kidney disease": 0.08} 

#importance score of each type of question
age_factor_answer = 0.20
gender_sy_answer_imp = 0.02
common_sy_answer_imp = 0.10
less_common_sym_answer_imp = 0.50
Serious_sym_answer_imp = 0.90
pre_existing_health_answer_imp = 0.75

answer_score_variables = [gender_sy_answer,common_sy_answer,less_common_sym_answer,Serious_sym_answer,pre_existing_health_answer]
importance_question_variable = [gender_sy_answer_imp,common_sy_answer_imp,less_common_sym_answer_imp,Serious_sym_answer_imp,pre_existing_health_answer_imp]

# user given input
user_input = []
def get_score():
    lis = []
    age_value = 0
    #user input
    for answer in user_input:
        if(type(answer) == list):
            #checking multiple user input
            for ans in answer:
                #getting the type of the question
                for type_question_index in range(0,len(answer_score_variables)):
                    if(ans in answer_score_variables[type_question_index].keys()):
                        lis.append(answer_score_variables[type_question_index][ans]*importance_question_variable[type_question_index])
        else:
            #getting the type of the question.
            for type_question_index in range(0,len(answer_score_variables)):
                if(answer in answer_score_variables[type_question_index].keys()):
                    lis.append(answer_score_variables[type_question_index][answer]*importance_question_variable[type_question_index])
    print(user_input[0],"______________-")
    #giving the age value by range.
    if(int(user_input[0])> 0 and int(user_input[0]) <= 17):
        age_value = 0.10
    elif(int(user_input[0]) > 17 and int(user_input[0]) <= 29):
        age_value = 0.15
    elif(int(user_input[0]) > 29 and int(user_input[0]) <= 40):
        age_value = 0.30
    elif(int(user_input[0]) > 40 and int(user_input[0]) <= 59):
        age_value = 0.55
    elif(int(user_input[0]) >=60):
        age_value = 0.80
    else:
        pass
    lis.append(age_value*age_factor_answer)
    if(round(sum(lis)*100) >= 100):
        return random.sample(range(90, 99), 1)[0]
    else:
        return round(sum(lis)*100)