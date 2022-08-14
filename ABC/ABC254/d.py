import sys

# テスト入力用 readlineの上に配置する
import io
_INPUT = u"""\

"""
sys.stdin = io.StringIO(_INPUT)


lines = [s.strip() for s in sys.stdin.readlines()]