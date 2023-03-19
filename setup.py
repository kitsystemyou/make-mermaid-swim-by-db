from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# long_description(後述)に、GitHub用のREADME.mdを指定
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='DB2mermaid',  # パッケージ名(プロジェクト名)
    packages=['db2mermaid'],  # パッケージ内(プロジェクト内)のパッケージ名をリスト形式で指定

    version='1.0.2',  # バージョン

    license='MIT',  # ライセンス

    install_requires=['sqlalchemy', 'mysqlclient'],  # pip installする際に同時にインストールされるパッケージ名をリスト形式で指定

    author='singsignalyou',  # パッケージ作者の名前
    author_email='kitsystemyou@gmail.com',  # パッケージ作者の連絡先メールアドレス

    url='https://github.com/kitsystemyou/make-mermaid-swim-by-db',  # パッケージに関連するサイトのURL(GitHubなど)

    description='db -> mermaid ER code',  # パッケージの簡単な説明
    long_description=long_description,  # PyPIに'Project description'として表示されるパッケージの説明文
    long_description_content_type='text/markdown',  # long_descriptionの形式を'text/plain',  'text/x-rst',  'text/markdown'のいずれかから指定
    keywords='mermaid erDiagram',  # PyPIでの検索用キーワードをスペース区切りで指定

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
    ],  # パッケージ(プロジェクト)の分類。https://pypi.org/classifiers/に掲載されているものを指定可能。
)
