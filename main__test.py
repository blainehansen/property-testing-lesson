from hypothesis import given, example, strategies as st
from main import decode, encode


@given(st.text())
@example("")
def test__decode_inverts_encode(s):
	assert decode(encode(s)) == s

@st.composite
def strings_with_repeated_characters(draw):
	# TODO only doing one character, how to do multiple in a random way?
	c = draw(st.characters())
	n = draw(st.integers(min_value=2, max_value=10))
	return c * n

@given(strings_with_repeated_characters())
@example("")
def test__decode_inverts_encode_definitely_repeated(s):
	assert decode(encode(s)) == s


# @given(st.integers(), st.integers())
# def test__ints_are_commutative(x, y):
# 	assert x + y == y + x

# @given(...)
# def test__ints_are_commutative_inferred(x: int, y: int):
# 	assert x + y == y + x


# @given(x=st.integers(), y=st.integers())
# def test__ints_cancel(x, y):
# 	assert (x + y) - y == x


# @given(st.lists(st.integers()))
# def test__reversing_twice_gives_same_list(xs):
# 	# This will generate lists of arbitrary length (usually between 0 and
# 	# 100 elements) whose elements are integers.
# 	ys = list(xs)
# 	ys.reverse()
# 	ys.reverse()
# 	assert xs == ys


# @given(st.tuples(st.booleans(), st.text()))
# def test__look_tuples_work_too(t):
# 	# A tuple is generated as the one you provided, with the corresponding
# 	# types in those positions.
# 	assert len(t) == 2
# 	assert isinstance(t[0], bool)
# 	assert isinstance(t[1], str)



# https://fsharpforfunandprofit.com/posts/property-based-testing-2/
# hypothesis.assume
# adapting strategies
# composite strategies
# https://hypothesis.readthedocs.io/en/latest/data.html

# https://fast-check.dev/docs/advanced/model-based-testing/
# https://github.com/blainehansen/project-f/blob/main/lib/dom/manipulate.test.ts
