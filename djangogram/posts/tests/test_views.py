from audioop import reverse
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile # 

class TestPosts(TestCase):
    def setUp(self): # test code 동작 전에 필요로하는 data를 생성, 초기화 하는 코드 
        User = get_user_model() # user model을 가져옴
        self.user = User.objects.create_user(
            username = 'kyungsoo', email = 'wjdrudtn97@naver.com', password = 'top_secret'
        ) # user를 생성하는 code

    def test_get_posts_page(self):
        url = reverse('posts:post_create')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/post.create.html')

    def test_post_creating_posts(self): # test를 위한 code는 test로 시작
        login = self.client.login(username = 'kyungsoo', password = 'top_secret')
        self.assertTrue(login)

        url = reverse('posts:post_create')
        image = SimpleUploadedFile("test.jpg", b"wahtevercontents")
        respone = self.client.post(
            url,
            {"image" : image, "caption" : "test test"}
        )

        self.assertEqual(respone.status_code, 200)
        self.assertTemplateUsed(respone, 'posts/base.html')

    def test_post_posts_create_not_login(self): # test를 위한 code는 test로 시작
        
        url = reverse('posts:post_create')
        image = SimpleUploadedFile("test.jpg", b"wahtevercontents")
        respone = self.client.post(
            url,
            {"image" : image, "caption" : "test test"}
        )

        self.assertEqual(respone.status_code, 200)
        self.assertTemplateUsed(respone, 'users/main.html')