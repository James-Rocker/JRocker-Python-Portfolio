# in most programming languages, dicts look like hash tables but
print(hash(1))  # hashes are stored as integers
print(hash(1.01), hash(1.01).bit_count())

"""
you might notice the huge difference. That's because the hash function returns the hash value of an object which
is an int and the standard 64 bit Python 3 interpreter represents it with 24 bytes

The cool thing about hashing decimal values is that 
"""

print(hash(1.01) == hash(23058430092136961))

"""
However, trying to get the original value based of a hash is impossible. This is a one way trip for the object
"""

# You might notice the hash object for strings changes on runs of this scrip, while ints and floats don't
print("tree hash this time is", hash("tree"))
print("Running a second time it's the same hash", hash("tree"))

"""
That's because since 3.3, string and byte objects are salted with a random object before the hashing process. 
This is a security process so the salting and hashing is not easy to reverse engineer. A hacker could steal the salted
passwords but that's not helpful if they can't reverse engineer the hash values

We can overwrite this behaviour by overwriting the PYTHONHASHSEED environment variable but this needs to
be done before the script is run with
export PYTHONHASHSEED=0
"""

# The only object types that are hashable are immutable types but mutable types result in type errors

try:
    hash(["a", "list", "of" "things"])
except TypeError as e:
    print(e, e.with_traceback)

# that's because mutable objects can change. However, it refers to object instance's, not types
d = dict()
d[(0, 0)] = 1  # perfectly fine
try:
    d[(0, [0])] = 1  # not fine
except TypeError as e:
    print(d, e, e.with_traceback)
