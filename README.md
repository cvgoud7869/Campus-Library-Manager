Question: Why is LibraryItem abstract, and what happens if DVD forgets to write late_fee()?
Answer: LibraryItem is abstract, because it inherits from ABC class, and declares late_fee() using  the @abstract method decorator, and abstract classes are 
        intended to provide the template(structure and functionality) for its child classes. Abstract classes can contain attributes, constructors, concrete methods and abstract methods, which need to be implemented in the child classes. These methods are defined in the abstract class because this a common requirement among all the child classes, and each might implement differently. If DVD class forgets or does not implement late_fee() method, no error will be raised, but DVD class cannot be instantiated, which will raise a TypeError, because all the abstract methods of LibraryItem class should be implemented in the child class. If it is just defined without implementation, then even DVD class becomes an abstract class.

Question: What happens when you read item.__available from outside the class, and why do we use is_available() instead?
Answer: It will raise an AttributeError, because it is a private variable. If we still want to access it, we can access it using the mangled name, 
        objectname._classname__variablename. Though, Python does not impose strict access restrictions unlike Java. But, it is not recommended to access a private variable directly. Instead we should use a method(getter method) like is_available(), to access that private variable.

Question: What is the difference between LibraryItem.total_items and self.title?
Answer: LibraryItem.total_items, is used to access the Class variable(total_items), whereas self.title, is used to access the instance variable(title). 
        Class variables like total_items, belong to a class and not an individual object. All objects share the same variable total_items.
        Instance variales like title, belongs to an object, each object has its own title.