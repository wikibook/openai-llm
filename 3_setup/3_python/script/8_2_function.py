lambda_radian = (lambda x:x / 180 * 3.1415)

for x in range(0, 360, 90):
    print('도: {}, 라디안: {:.2f}'.format(x, lambda_radian(x)))