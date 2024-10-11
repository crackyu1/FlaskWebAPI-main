
import pytest
#测试myRequests.get函数
from app.myRequests import get
def test_get():
    
    dict=get(province="广东省",city="广州市1")
    #判断返回的字典中是否包含place和temperature
    assert "place" in dict
    assert "temperature" in dict

if __name__ == "__main__":
    pytest.main()