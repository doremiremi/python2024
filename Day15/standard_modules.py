
#기본적으로 깔려있는 함수들
#random:랜덤 역할을 하는 도구모음
#math:수학 관련된 도구모음
#datetime:날짜와 시간을 다루는 도구모음
#os:파일 또는 운영체제접근

from random import *

from math import *
# import math
# math.sqrt()
from datetime import *

import os

p = os.path.join(os.environ['USERPROFILE'],'DESKTOP')
forder_name ="집보내줘"
new_p = os.path.join(p,forder_name)
os.makedirs(new_p)


# now = datetime.now()
#
# print(now)