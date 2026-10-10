
# BMI（身体质量指数）= 体重（kg） ÷ 身高（m）²，或英制单位下为 BMI = 体重（lb） ÷ 身高（in）² × 703。

wei=float(input("请输入您的体重：（kg）"))
tall = float(input("请输入您的身高：(m)"))

bmi = wei/(tall*tall)
print(f"您的BMI指数为：{bmi:.2f}")
if bmi < 18.5:
    print("您的体重过轻")
elif bmi < 24:
    print("您的体重正常")
elif bmi < 28:
    print("您的体重过重")
else:
    print("您的体重肥胖")
