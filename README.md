# About The Project
이동 수단의 바퀴가 크랙 위를 지나가면 충격을 받을 수 있으며 주행자의 부상을 초례할 가능성이 생긴다. 이러한 문제점을 보안하기 위해 바퀴가 지나가는 부분의 크랙을 탐지 및  속도를 제어해 크랙 위에서의 충격량을 최소화, 주행자에게 안정감을 제공할 수 있다.


# Feature List
1. 터틀봇을 원격 혹은 유선으로 조종 가능하게 한다.
2. 실 시간성을 보장하기 위해 최적화 작업을 한다.
3. 라즈베리파이 카메라로 터틀봇 바퀴의 이동경로의 크랙을 탐지 할 경우 터틀봇 속도를 줄인다.


#  Feature List Details
1. 터틀봇의 자율 주행을 위한 컨트롤 보드 OpenCR1.0을 사용해 시리얼 케이블로 통신한다.
2. 이동 로봇 제어를 위한 안드로이드 애플리케이션을 사용, RPi4b 와 블루투스로 통신 가능.
3. Pi 카메라를 사용해 캡처 한 이미지 해상도를 900 by 600, 이를 Gray scale로 변환한 뒤, 150 by 150의 이미지로 분할한다.
4. 로봇의 주행에 영향을 주는 이미지만을 선택하여 크랙 여부를 판단한다. 
5. 고정된 카메라의 각도(θ)와 카메라가 설치된 높이(h)를 통해 크랙까지의 거리를 계산.
º 기체의 현재속도(v0)를 이용해 로봇이 크랙에 도착하는 시간(t0)을 계산한다. 
º  t0 = h tanθ/v0, t1 = t0 + w/v1
(v1=감속 속도, w=기체의 길이)
6. 이미지 캡처에 약 300ms 소요, 분할된 단일 이미지의 추론에 걸리는 시간은 약 30ms 로 걸리는 총 시간은 약 420ms 이다.

# Data
[Structural Defects Network (SDNET) 2018](https://www.kaggle.com/datasets/aniruddhsharma/structural-defects-network-concrete-crack-images)


# Model
* TensorFLow로 CNN 인공 신경망 모델을 개발
* RPi4b 의 제한된 성능에서 실시간 추론을 위해 TF-Lite 로 모델을 경량화
* 모델의 테스트 정확도 : 98.17% 

* 모델 구성도

![model](https://user-images.githubusercontent.com/76561461/190082773-675ba968-8244-40e9-a3c4-78213bbbe7a5.PNG)
<br/>

* 충격 센서 데이터

![sensor](https://user-images.githubusercontent.com/76561461/190082777-37deaec5-249d-4937-a73f-e201553d0a78.PNG)
<br/>

# Test

![2](https://user-images.githubusercontent.com/76561461/144840823-ba5dd336-a3ec-403a-a00e-ae0742975360.PNG)

* 학습 및 검증 그래프
 
![1](https://user-images.githubusercontent.com/76561461/144840333-f80b7aac-e39e-4eac-b0f2-6be3d88284ba.PNG)
<br/>

# Demo
https://www.youtube.com/watch?v=YbdRjEjghic
