import os
import requests


class Youdao(object):
    def __init__(self, en_us=0, word='status'):
        word = word.lower()
        self.en_or_us = en_us
        self.word = word

        self.root = os.path.dirname(os.path.abspath(__file__))
        self.file_dir = os.path.join(self.root, 'pronounce', 'en' if self.en_or_us == 0 else 'us')

        if not os.path.exists(self.file_dir):
            os.makedirs(self.file_dir)

    def down(self, word=None):
        if word:
            self.word = word

        tmp = self._get_file_path()
        if not os.path.exists(tmp):
            self._get_url()
            res = requests.get(self._url)
            if len(res.content) == 0:
                raise Exception('Download Failed.')
            with open(tmp, 'wb') as f:
                f.write(res.content)
        return tmp

    def _get_url(self):
        self._url = f'http://dict.youdao.com/dictvoice?type={1 - self.en_or_us}&audio=' + self.word

    def _get_file_path(self):
        filename = self.word + '.mp3'
        filepath = os.path.join(self.file_dir, filename)
        return filepath


if __name__ == "__main__":
    yd = Youdao(word='consumer')
    yd.down()
