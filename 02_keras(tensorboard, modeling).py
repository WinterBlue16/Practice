
#  DNN Modeling practice(2 dimension)
#  0. dataset 분리 함수
import numpy as np
from numpy import array
                        # dataset, 4
def split_sequence(sequence, n_steps):
    X,y = list(), list()
    for i in range(len(sequence)): # 10 # i는 0부터 시작된다!!
        end_ix = i + n_steps       # 0 + 4 = 4
        if end_ix > len(sequence)-1: # 4 > 9
            break
        seq_x, seq_y = sequence[i:end_ix], sequence[end_ix] # [0:4], [4] => 0, 1, 2, 3 / 4
        X.append(seq_x) # X 리스트에 추가 # 0, 1, 2, 3
        y.append(seq_y) # y 리스트에 추가 # 4
    return array(X), array(y) # numpy 배열로 만들기


dataset = array(range(100)) # 벡터로 넣어야 함!
n_steps = 5
'''
for n_steps in range(1, 10):
    x, y = split_sequence(dataset, n_steps)
    print('n_steps :', n_steps)
    print(x)
    print(y)
    print()
'''

x, y = split_sequence(dataset, n_steps)
print(x)
print(y)
print(x.shape)
print(y.shape)


# 2. dataset split(train, test, val)
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.6)
x_val, x_test, y_val, y_test = train_test_split(x_test, y_test, test_size=0.6)


# 3. 모델 생성
from keras.models import Model, Sequential
from keras.layers import Dense, LSTM, Input

model = Sequential()

model.add(Dense(256, input_shape=(5,)))
model.add(Dense(256))
model.add(Dense(256))
model.add(Dense(256))
model.add(Dense(1))


# 4. 모델 훈련
model.compile(loss='mse', optimizer='adam', 
              metrics=['mae'])

from keras.callbacks import EarlyStopping, TensorBoard

tb = TensorBoard(log_dir='./graph',
                      histogram_freq=0,
                      write_graph=True,
                      write_images=True)
# early_stoppping = EarlyStopping(monitor='loss', patience=10, mode='auto')# patience=N, 원하는 값이 나온 후(ex> min, max), 다른 값이 나오지 않은 상태로 N번 지날 경우 멈춤 
model.fit(x, y, epochs=200, batch_size=1, callbacks=[tb])# early_stopping은 리스트 형식으로 넣어야 함 => [early_stopping] 

# verbose=0 => 훈련과정을 보여주지 않음 
# verbose=2 => 훈련 과정에서 막대 제거 
# verbose=3 => epoch만 보여줌 


# 5. 모델 평가예측
loss, mse = model.evaluate(x, y, batch_size=1) # loss는 자동적으로 출력
print(loss, mse)


# 6. 실제 예측값 뽑아내기
model.summary()

# 새로운 데이터 넣어보기
x_prd = array([[973, 974, 975, 976, 976], [435, 436, 437, 438, 439], [373, 374, 375, 376, 377]])
g = model.predict(x_prd, batch_size=1)
print(g)

y_predict = model.predict(x_test, batch_size=1)

# RMSE 구하기
from sklearn.metrics import mean_squared_error

def RMSE(y_test, y_predict): # 실제 정답값, 모델을 통한 예측값 
    return np.sqrt(mean_squared_error(y_test, y_predict))
print('RMSE :', RMSE(y_test, y_predict))


# R2 구하기
# R2 정의 및 참고 : https://newsight.tistory.com/259
from sklearn.metrics import r2_score

r2_y_predict = r2_score(y_test, y_predict)
print("R2 :", r2_y_predict)

