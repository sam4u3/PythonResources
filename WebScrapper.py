import requests


class WebScrapper:
    def __init__(self, report_file_path: str):
        self.session = requests.Session()
        self.proxies = {'http': 'http://10.11.4.254:3128',
                        'https': 'http://10.11.4.254:3128'}
        self.final_data = []
        self.excel_report = report_file_path

    def get_request(self, url) -> str:
        try:
            request_res = self.session.get(url)
            if request_res.status_code == 200:
                return request_res.text
            return ''
        except requests.RequestException as ex:
            print(f'Exception : \n {str(ex)}')

    def find_total_pages(self):
        pass

    def get_total_products(self):
        pass

    def fetch_product_details(self):
        pass

    def dump_data_to_excel(self):
        pass


if __name__ == '__main__':
    pass
