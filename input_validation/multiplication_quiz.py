
import pyinputplus as pyip
import random, time

number_of_questions = 10
correct_answers = 0

for question_number in range(number_of_questions):
    # pick random numbers
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    prompt = '#%s: %s x %s = ' % (question_number, num1, num2)

    try:
        pyip.inputStr(
            prompt, 
            allowRegexes=['^%s$' % (num1 * num2)],  # right ans
            blockRegexes=[('.*', 'Incorrect!')],    # wrong ans
            timeout=8 ,
            limit=3                       # time and tries
            )
    except:
        # runs if no exceptions were raised in try
        print('Correct!')
        correct_answers += 1

time.sleep(1) # pause to read result
print('Score: %s / %s' % (correct_answers, number_of_questions))