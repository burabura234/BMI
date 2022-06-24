#    BMI換算器
height = input('請輸入身高(公尺): ')
weight = input('請輸入體重(公斤): ')
height = float(height)
weight = float(weight)
BMI = weight / (height * height)
print('你的BMI為', BMI)
if BMI < 18.5:
	print('你的體重太輕')
	print('需要多加注意')
elif BMI >= 18.5 and BMI < 24:
	print('你的體重剛剛好')
elif BMI >= 24 and BMI < 27:
	print('你的體重過重')
	print('需要多加注意')
elif BMI >= 27 and BMI < 30:
	print('你的體重為輕度肥胖')
	print('需要多加注意')
elif BMI >= 30 and BMI < 35:
	print('你的體重為中度肥胖')
	print('需要多加注意')
else:
    print('你的體重為重度肥胖')
    print('請立刻改善或就醫!')