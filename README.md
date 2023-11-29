# 5조 팜스토리 스마트팜 Node-red
# Smart_farm_plan5_Portfowarding_NoderedAndCamera
## 구성원: 오상우, 윤현호, 박세린, 이병현, 권용만

### 개요
<p>
<img src=https://github.com/farmstory5/Smart_farm_plan4_CDS_WaterLevel_Analog_signal_in-Dashboard/assets/130550405/1a455a58-8089-419f-a275-84c491b285a4
</p>
<br/>

#### 포트포워딩이란?
포트포워딩이란 IP주소를 통해 외부에서 원하는 IP주소를 접근하고자 할 때 접근가능한 포트를 열어주는 작업입니다.<br/>
라즈베리파이4에서는 ufw작업을 통해 방화벽옵션에서 사용하고 싶은 포트를 허용하고<br/>
본체PC로는 공유기설정창에서 라즈베리파이의 IP와 해당포트를 포트포워딩합니다.<br/>
공유기에 설정된 외부 IP를 통해 다른 네트워크환경에서 해당 포트를 HTTP주소창에서 접속할 수 있게 됩니다.<br/>

#### 포트포워딩의 한계<br/>
외부에서 한 프로세스당 하나의 포트와 접속이 가능합니다.<br/>
즉, 하나의 HTTP창에서 하나의 포트만 접속이 가능하다는 뜻입니다.<br/>
그래서 포트포워딩된 다른 네트워크환경에서 노드레드의 포트HTTP창에선 카메라의 포트창을 접속할 수 없습니다.<br/>
카메라문제는 카메라 포트를 노드레드 포트에서 구현하는 것이 아닌 다른 하나의 HTTP창으로 접속하거나<br/>
하나의 HTTP창에 두 포트를 같이 접속을 하려면 포트포워딩이 아닌 다른 해결방안을 모색해야 됩니다.<br/>

### 블록도
<p align="center">
<img src="https://github.com/farmstory5/Smart_farm_plan4_CDS_WaterLevel_Analog_signal_in-Dashboard/assets/130550405/56e30635-be63-4a65-8f53-fe635a03b062">
</p>

### 라즈베리파이IP dashboard
<p align="center">
<img src="https://github.com/farmstory5/Smart_farm_plan4_CDS_WaterLevel_Analog_signal_in-Dashboard/assets/130550405/0f5bafbe-986f-4e03-8959-3419f4cd42bd">
</p>
<p align="center">
<img src="https://github.com/farmstory5/Smart_farm_plan4_CDS_WaterLevel_Analog_signal_in-Dashboard/assets/130550405/b74d09b2-e709-4961-a1f3-ad43ca3e01e0">
</p>
<p align="center">
<img src="https://github.com/farmstory5/Smart_farm_plan4_CDS_WaterLevel_Analog_signal_in-Dashboard/assets/130550405/c5616711-24bf-46e1-868d-06942281d9a2">
</p>
