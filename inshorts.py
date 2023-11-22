# inshorts module contains Inshorts class.
# inshorts class will be used to fetch the news from inshorts.com as API response for it's instance.

# standard library's
import requests


class Inshorts:
    """
    Inshorts module is the main module which will get data from Inshorts API
    Inshorts class helps in providing 2 varities of News(all_news & Category_news).
    """

    url = "https://inshorts.com/api/en"

    # def __init__(self,ob_name):
    #     """Initialize Objects with it's name"""
    #     self.ob_name = ob_name

    def all_news(self, max_limits=5):
        """Provides the all news via Inshorts API

        Args:
            max_limit: maximum limit of the selected news.
        """

        try:
            url = f"{self.url}/news"
            params = (
                ("category", "all_news"),
                ("max_limit", f"{max_limits}"),
                ("include_card_data", "true"),
            )
            response = requests.get(url, params=params)
            json_response = response.json()
            print(json_response)

            # The below code can be used to Print only some selected key's and value's
            # Any required key can be added inside var_list to print it's specific value.
            var_list = [
                "author_name",
                "content",
                "source_url",
                "source_name",
                "title",
                "category_names",
                "image_url",
            ]
            for j in range(max_limits):
                print("-" * 30)
                for i in var_list:
                    print(
                        f'{i} = {json_response["data"]["news_list"][j]["news_obj"][i]}'
                    )
        except Exception as e:
            print(f"Exception occured due to {e.args}")

    def category_news(self, category_name, max_limits=5):
        """Provides the all news via Inshorts API

        Args:
            category_name: contains the category of news to fetch.
            max_limit: maximum limit of the selected news.
        """

        try:
            url = f"{self.url}/search/trending_topics/{category_name}"
            params = (
                ("category", "top_stories"),
                ("max_limit", f"{max_limits}"),
                ("include_card_data", "true"),
            )
            response = requests.get(url, params=params)
            json_response = response.json()
            print(json_response)

            # The below code can be used to Print only some selected key's and value's
            # Any required key can be added inside var_list to print it's specific value.
            var_list = [
                "author_name",
                "content",
                "source_url",
                "source_name",
                "title",
                "category_names",
                "image_url",
            ]
            for j in range(max_limits):
                print("-" * 30)
                for i in var_list:
                    print(
                        f'{i} = {json_response["data"]["suggested_news"][j]["news_obj"][i]}'
                    )
        except Exception as e:
            print(f"Exception occured due to {e.args}")
