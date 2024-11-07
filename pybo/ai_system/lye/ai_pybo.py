# ai_pybo.py start_ai가 있던 함수 페이지.

# from pybo.ai_system.lye.ai_system import setup_system
from pybo.ai_system.ai_system import setup_system
# from django.conf import settings     # 기존 Path 모듈을 대체한 settings. 장고에서 url 관련을 나타낼때는 path보다 이 모듈을 사용한다고 함.
#
# import logging # 개발자용 디버깅용 로깅 모듈
#
# import numpy as np
# import pickle
# ai_system.py ocode 제작 모듈
# : AI 시스템 설정을 위한 데코레이터 가져오기

"""
이름변동 사항

1 setup_django_system -> load_config
2 start_ai -> ai_view


setup_django_system 추가사항
1 config 함수화 : load_config
2 사용자 선택 detector 모델 불러오기 조건식 : help_load_detectors
3 사용자 선택 predictor모델 불러오기 조건식 : help_load_predictors
"""


@setup_system  # setup_django_system 데코레이터를 사용해, Django 환경설정에 이어서 ai_view 함수를 사용.
def start_ai(request, image_path, face_recognition_system, target_encodings,*args, **kwargs):
    """ func(request, image_path, ai_system, target_encodings, *args, **kwargs)
    AI 얼굴 인식 시스템을 사용하여 이미지를 처리하고 결과를 반환합니다.
    """
    # 얼굴 인식 시스템을 사용하여 이미지를 처리하고, 결과 이미지의 경로를 받음
    output_path = face_recognition_system.process_image(image_path, target_encodings)
    # 처리된 이미지의 경로를 반환
    print('------------------------------------------------------')
    print('This is output_path ==> ',output_path)
    print('------------------------------------------------------')
    return output_path



""" 하단의 코드는 디버깅을 위한 코드들임. 
    작성중이던 코드였음. 실제로 실행되려면 더 작업 또는 삭제해야하는 코드임. -이예은"""