from django.test import TestCase
from django.contrib.auth.models import User
from sign.models import Event
from django.test import Client

class TestLogin(TestCase):
    '''测试登录功能'''
    def test_login_success(self):
        '''测试登录成功'''
        test_data = {'username':'putishuxia','password':'xygz1234hao'}
        #实例化浏览器并发送数据
        response = self.client.post('/login_action/',data=test_data)
        self.assertTemplateUsed(response,'index.html')

    def test_login_username_null(self):
        '''登陆失败--用户名为空'''
        test_data = {'username':'','password':'xygz1234hao'}
        #实例化浏览器并发送数据
        response = self.client.post('/login_action/',data=test_data)
        print(response)
        self.assertTemplateUsed(response,'index.html')
        self.assertIn(b'username or password null!',response.content)

    def test_login_password_null(self):
        '''登陆失败--密码为空'''
        test_data = {'username': 'putishuxia', 'password': ''}
        # 实例化浏览器并发送数据
        response = self.client.post('/login_action/', data=test_data)
        self.assertTemplateUsed(response, 'index.html')
        self.assertIn(b'username or password null!', response.content)

    def test_login_user_notexit(self):
        '''用户不存在--无该用户名'''
        test_data = {'username': 'yzc', 'password': 'xygz1234hao'}
        # 实例化浏览器并发送数据
        response = self.client.post('/login_action/', data=test_data)
        self.assertTemplateUsed(response, 'index.html')
        self.assertIn(b'username or password error!', response.content)

    def test_login_userpassword_notexit(self):
        '''用户不存在--无该密码'''
        test_data = {'username': 'putishuxia', 'password': 'xygz1234ha'}
        # 实例化浏览器并发送数据
        response = self.client.post('/login_action/', data=test_data)
        self.assertTemplateUsed(response, 'index.html')
        self.assertIn(b'username or password error!', response.content)


        '''
        测试登录也要考虑字符长度、空格、特殊字符（空格、！、？等），结合软件设计的约束找测试点。
        '''

class TestEventManage(TestCase):
    def setUp(self):
        #准备发布会数据
        Event.objects.create(name = 'xiaomi5',limit = 1000,status = 1,address = '北京市海淀区',start_time = '2019-11-11 13:00:00')
        self.login_user = {'username': 'putishuxia', 'password': 'xygz1234hao'}
    def test_eventmanage(self):
    #首先登陆，满足装饰器要求
        test_data = {'username': 'putishuxia', 'password': 'xygz1234hao'}
        # 实例化浏览器并发送数据
        response = self.client.post('/login_action/', data=test_data)
        print(response)
        #response = self.client.post('/event_manage/')
        self.assertEqual(response.status_code,200)
        #self.assertIn(b'Lenovo',response.content)

    def test_event_search(self):
        #test_data = {'username': 'putishuxia', 'password': 'xygz1234hao'}
        # 实例化浏览器并发送数据
        response = self.client.post('/login_action/', data=self.login_user)
        response = self.client.post('/search_name/', {'name':'xiaomi5'})
        #response = self.client.get('/search_name/?name=xiaomi5')
        print(response)
        #self.assertEqual(response.status_code,200)
        #self.assertIn(1, response.content)
        self.assertIn(b'xiaomi5', response.content)




