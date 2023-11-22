# Unit test module will be used to cover test cases on inshorts API

from unittest.mock import Mock, patch
from inshorts import Inshorts
from test_json_data import category_news_json_response, json_response


@patch("inshorts.requests")
def test_all_news1(request_mock):
    """
    Test case to test the all_news function when
    fetching the all news details successfully from inshorts API.
    """
    json_mock = Mock()
    json_mock.json.return_value = json_response
    request_mock.get.return_value = json_mock
    inshort_news = Inshorts()
    inshort_news.all_news(1)
    request_mock.get.assert_called_once()
    json_mock.json.assert_called_once()


@patch("inshorts.requests")
def test_all_news2(request_mock):
    """
    Negative Test case to test the all_news function when
    fetching the all news details.
    """
    json_mock = Mock()
    json_mock.json.return_value = json_response
    request_mock.get.return_value = json_mock
    inshort_news = Inshorts()
    inshort_news.all_news(3)
    request_mock.get.assert_called_once()
    json_mock.json.assert_called_once()


@patch("inshorts.requests")
def test_category_news1(request_mock):
    """
    Test case to test the category_news function when
    fetching the category news details successfully from inshorts API
    """
    json_mock = Mock()
    json_mock.json.return_value = category_news_json_response
    request_mock.get.return_value = json_mock
    inshort_news = Inshorts()
    inshort_news.category_news("sports", 1)
    request_mock.get.assert_called_once()
    json_mock.json.assert_called_once()


@patch("inshorts.requests")
def test_category_news2(request_mock):
    """
    Negative Test case to test the category_news function when
    fetching the category news details.
    """
    json_mock = Mock()
    json_mock.json.return_value = category_news_json_response
    request_mock.get.return_value = json_mock
    inshort_news = Inshorts()
    inshort_news.category_news("sports", 3)
    request_mock.get.assert_called_once()
    json_mock.json.assert_called_once()
