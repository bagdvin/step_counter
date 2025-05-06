print("🏃‍♀️‍➡️ STEP COUNTER 🏃‍♀️ ")
step_count = int(input("Please enter the steps walked today "))
diff_step = 10000 - step_count

if step_count > 10000 :
    print(f"Keep it up !!!! You have walked {-diff_step} steps more than your goal")
else :
    print(f"Please walk {diff_step} steps to acheive your goal  ")

