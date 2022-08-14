import sys
import itertools

# テスト入力用 readlineの上に配置する
import io
_INPUT = u"""\
3
2 6 2
"""
sys.stdin = io.StringIO(_INPUT)
lines = [s.strip() for s in sys.stdin.readlines()]
