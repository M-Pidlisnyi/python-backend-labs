from django.test import TestCase
from django.urls import reverse, resolve

from .views import ArticleCategoryList, ArticleDetail, ArticleList, HomePageView
#Create your tests here.

class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEqual(view.func.view_class, HomePageView)

class CategoryTest(TestCase):
    def test_category_list_view_status_code(self):
        url = reverse('articles-category-list', args=['name'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_category_list_url_resolves_view(self):
        view = resolve(r'/articles/category/[a-z]*')
        self.assertEqual(view.func.view_class, ArticleCategoryList)
        


class AtriclesTest(TestCase):
    def test_articles_list_view_status_code(self):
        url = reverse('articles-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_articles_list_url_resolves_view(self):
        view = resolve('/articles')
        self.assertEqual(view.func.view_class, ArticleList)

    def test_articles_detail_url_resolves_view(self):
        view = resolve(r'/articles/[0-9][0-9][0-9][0-9]/[0-9][0-9]/[0-9][0-9]/[a-z]*')
        self.assertEqual(view.func.view_class, ArticleDetail)

