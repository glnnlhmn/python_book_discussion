import pytest
from vector2d import Vector

def test_boolean_ness():
    falsy_vector = Vector(0,0)
    assert(not falsy_vector)
    truthy_vector = Vector(3,14)
    assert(truthy_vector)

# This is kind of interesting. Since we didn't implement equality:
# >>> Vector(3,5) == Vector(3,5)
# False
# However, if we convert to a float using abs, == works :)
def test_addition():
    assert(abs(Vector(1,2) + Vector(2,3)) == 5.830951894845301)

def test_scalar_mul():
    assert(abs(Vector(1,2) * 5) == 11.180339887498949)

def no_vector_vector_mul():
    with pytest.raises(TypeError):
        v1 = Vector(-1,-5)
        v2 = Vector(-0,-3)
        doom = v1 * v2

def test_repr():
    v1 = Vector(1,2)
    assert str(v1) == 'Vector(1, 2)'

def test_abs():
    assert(abs(Vector(1,2)) == 2.23606797749979)