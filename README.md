# SOOJLE 세종대학교 정보통합솔루션
보다 자세한 설명은 아래의 링크를 참고해주십시오.
https://soojle.gitbook.io

# Overview
## INTRO
![img](https://gblobscdn.gitbook.com/assets%2F-L_Wo7SRUvbKJuPojzzZ%2F-LuSgJyztPHSe7KN0lJs%2F-LuSgeUaBDVndgUf6uXm%2Fimage.png?alt=media&token=d2ad0cf6-8949-47ca-929d-79cb35ae0692)
세종대학교에서는 재학생의 편리한 학교생활을 위해 여러 커뮤니티 및 공지 등을 통해 유용한 정보를 게시하거나 공지한다. 
그 안에는 학교의 메인 홈페이지 외에도 학과 및 동아리에서 각각 개설되는 웹 사이트, 학생들이 자발 적으로 만든 커뮤니티,
플랫폼까지 포함하면 한 학교에서만 관련 사이트가 수백 개에 다다르게 되었다.
그러나 이러한 환경에 반해 실제 대학교 관련 정보를 탐색하는 상당히 불편하다는 평을 받고 있다. 서비스 자체의 접근성, 
알려지지 않아 가치 면에 비해 사용량이 저조한 서비스, 여러 곳에 흩어져 있고 중복으로 존재하는 정보 등을 통해 구글을 비롯한 
통합 검색 엔진으로도 찾을 수 없는 정보가 점점 증가하고 있다. 

본 프로젝트는 이러한 문제점을 해결하기 위해 해당 학교 관련된 웹상의 모든 정보를 수집하여 
통합한 접근성이 높은 서비스를 제공함으로 학생들의 정보 접근성을 높여 더 편리한 학교생활에 임할 수 있도록 하는 서비스 제공을 목표로 한다. 
흩어져 있던 정보들을 한 곳으로 통합시켜 필요한 정보의 탐색을 용이하게 하고, 
사용자의 액션을 수집하여 대학교 전체의 흐름을 파악하는 유의미한 가치의 정보를 수집할 수 있다. 본 프로젝트를 수행함으로써, 
학교 내의 모든 정보를 체계화하고 접근성을 높여 정보의 소비량을 증진시키고 학생들이 보다 편리하게 학교생활에 임하는 것이 가능할 것이라 기대한다.

## 프로젝트 추친 배경
사회 집단은 구성원이 많을수록 내부에서 생성되는 정보는 기하급수적으로 증가한다. 
대학교라는 공동체 또한 매우 많은 구성원과 내부 집단을 내포하고 있으며,
각자의 필요에 따라 무수히 많은 커뮤니티, 플랫폼 등이 탄생하게 되었다. 

현재 세종대학교에 관련하여 만들어진 모든 사이트 및 플랫폼은 약 200개 이상에 달한다.
그러나 이러한 환경에 반해 실제 학교의 대학생들은 학교 내의 원하는 정보를 찾기가 힘들다는 의견이 많이 나오고 있다. 
이런 상황에 대한 문제점은 각 커뮤니티나 사이트의 조회수만 알아보아도 명백한데, 대표적으로 아래와 같은 문제점이 있다.

## **사용자 인증을 통한 정보 공유 억제**

![img](https://gblobscdn.gitbook.com/assets%2F-L_Wo7SRUvbKJuPojzzZ%2F-Leokpfb2dHbweVnA0gz%2F-LeokrIup-uFuVDmy2tl%2F%EB%A1%9C%EA%B7%B8%EC%9D%B8.png?alt=media&token=4b4aab46-6681-41be-87ac-fd8516ea84fa)

로그인을 해야만 해당 정보에 접근 가능

- 학교 내 에브리타임, 페이스북를 비롯한 여러 활동적인 플랫폼이 존재함.
- 이들의 정보는 네이버나 구글의 검색에서 정보가 노출되지 않는 경우가 대부분임. 
- 구성원 외의 접근을 차단하여 검색엔진 크롤링 봇 조차도 접근할 수 없기 때문.
- 로그인을 해야만 해당 정보에 접근이 가능하며, 모든 플랫폼에 로그인을 해두었다고 해도 결국 각각의 사이트에서 직접 정보를 검색해야 함.

## **서비스 기능성 및 접근성 결여**

![img](https://gblobscdn.gitbook.com/assets%2F-L_Wo7SRUvbKJuPojzzZ%2F-Leokpfb2dHbweVnA0gz%2F-LeomEsuTi6aUbVNx_g3%2FKakaoTalk_20190514_141659246.jpg?alt=media&token=be3e34e5-342c-4439-95dd-5e4eb7bba1b7)

- 많은 웹 사이트가 개발 후, 마땅한 관리가 이루어지지 않음.
- 20대 이용률 통계에서 월등히 사용량이 높은 모바일 기기에 대한 접근성이 낮음.
- 실제로 학생들의 이용률을 낮추는 큰 문제이며, SNS가 그에 대한 반증이기도 함.

## **분야 등을 구별하지 않는 무분별한 정보와 중복된 정보의 혼재**

![img](https://gblobscdn.gitbook.com/assets%2F-L_Wo7SRUvbKJuPojzzZ%2F-LeoiGYloSb7SKj7dsmP%2F-Leok1P75R_NgZiz5IgZ%2F%EC%A0%9C%EB%AA%A9%20%EC%97%86%EC%9D%8C.png?alt=media&token=78604a15-b630-4b53-ae45-52e6ea38b99f)

- 여러 분야의 정보를 관리할 공간이 마땅하지 않아, 분류가 제대로 되지 않고 혼잡함.
- 자유게시판 등에도 여러 홍보 글이 난무하는 상황임.
- 무분별한 및 중복된 정보들로 인해 자신이 원하는 정보만을 얻기가 힘듦.

즉, 대학교를 위한 여러 플랫폼들이 존재함에도 이들은 완전히 흩어져 있기 때문에  
관련된 모든 정보를 수집하여 체계적으로 관리할 시스템이 필요하다. 
자신이 원하는 정보에 대한 빠르고 효율적인 탐색을 넘어, 사용자의 데이터를 분석하여 새로운 정보를 추천해줄 수 있어야 한다.
