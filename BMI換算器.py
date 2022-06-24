#    BMI換算器
height = input('請輸入身高(公尺): ')
weight = input('請輸入體重(公斤): ')
height = float(height)
weight = float(weight)
BMI = weight / (height * height)
print('您的BMI為', BMI)