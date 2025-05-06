print("🏃‍♀️‍➡️ STEP COUNTER 🏃‍♀️ ")
step_count = int(input("Please enter the steps walked today "))
diff_step = 10000 - step_count

if step_count > 10000 :
    print(f"Keep it up !!!! You have walked {-diff_step} steps more than your goal")
    print(f" 🥳 You have {-diff_step*0.04} extra calories today. ")
else :
    print(f"Please walk {diff_step} steps to acheive your goal  ")
    print(f"You need to burn {diff_step*0.04} calories to achieve your goal 🤗.")

