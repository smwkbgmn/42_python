ft_list = ["Hello", "tata!"]  # mutable
ft_tuple = ("Hello", "toto!")  # immutable
ft_set = {"Hello", "tutu!"}  # unordered, no duplicates, cannot be indexed
ft_dict = {"Hello" : "titi!"}  # mutable, unordered

ft_list[1] = "World!"
ft_tuple = (ft_tuple[0], "Germany!")
ft_set.remove("tutu!")
ft_set.add("Wolfsburg!")
ft_dict["Hello"] = "42Wolfsburg!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

"""
All data in a Python program is represented by objects or by relations between objects.

Every object has an [identity, a type and a value].
An object's identity never changes once it has been created;
you may think of it as the object’s address in memory.
The is operator compares the identity of two ∑objects;
the id() function returns an integer representing its identity.

An object's type determines the operations that the object supports
(e.g., “does it have a length?”) and also defines the possible values for
objects of that type. The type() function returns an object’s type
(which is an object itself). Like its identity, an object’s type is also unchangeable.

The value of some objects can change.
Objects whose value can change are said to be mutable;
objects whose value is unchangeable once they are created are called immutable.
(The value of an immutable container object that contains a reference to
a mutable object can change when the latter’s value is changed;
however the container is still considered immutable,
because the collection of objects it contains cannot be changed.
So, immutability is not strictly the same as having an unchangeable value,
it is more subtle.) An object’s mutability is determined by its type;
for instance, numbers, strings and tuples are immutable,
while dictionaries and lists are mutable.
"""
