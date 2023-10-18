
"https://www.techiedelight.com/ja/trie-implementation-python/"

# Trieノードを格納するクラス


class Trie:
    # コンストラクター
    def __init__(self):
        self.isLeaf = False
        self.children = {}

    # 文字列をTrieに挿入する反復関数

    def insert(self, key):

        # ルートノードから開始します
        curr = self

        # キーの各文字に対して行います
        for c in key:
            # 次のノードに移動し、パスが存在しない場合はノードを作成します
            curr = curr.children.setdefault(c, Trie())

        # 現在のノードをリーフとしてマークします
        curr.isLeaf = True

    # Trie内のキーを検索するための反復関数。 Trueを返します
    # キーがTrieで見つかった場合は#。それ以外の場合は、Falseを返します

    def search(self, key):

        curr = self

        # キーの各文字に対して行います
        for c in key:
            # 次のノードに移動します
            curr = curr.children.get(c)
            # 文字列が無効な場合は#(Trieのパスの終わりに到達)
            if curr is None:
                return False

        # 現在のノードがリーフノードであり、到達した場合にtrueを返します。
        # 文字列の終わり
        return curr.isLeaf


if __name__ == '__main__':

    # ノードを構築します
    head = Trie()

    head.insert('xyz')
    print(head.search('xyz'))
