```
This step of setting the database to match the structure of the models is called migration. Remember, migrations are needed when we make changes to our models — and we’ve just made two new ones!

In Django, there are two steps necessary to make this migration happen:

Running python3 manage.py makemigrations to create a file with the instructions needed for our database to create the proper schemas.
Running python3 manage.py migrate to execute the instructions in our file to create the actual tables in our database.
We’ll first focus on makemigrations. Since we need to use manage.py to execute this step, we need to be in our root folder to execute:
```

In this lesson, we covered:

A schema is a structure we design for the data in our application.
A model is a Python class that contains characteristics and behavior using: attributes, metadata, and methods.
Model attributes are implemented using Django field names and different field types.
Django models can relate to other models. One way of showing this connection is to use a foreign key.
Django field types accept optional keyword arguments based on key-value pairs such as null, blank, choices, default, and primary_key.
Models can contain metadata using a nested Meta class and providing specific attributes.
Models can have methods that are functions specific to that model. Some methods are inherited from the parent Model class.
Django requires that we commit our models to the 
database
Preview: Docs Loading link description
 via a two-step migration procedure with makemigrations and migrate.
Django lets us undo one or more migrations by supplying the migrate command with a named migration.

In this exercise, we will use the Python shell to create instances of models. The Python shell is a command-line tool that starts up a Python interpreter which we will use to execute CRUD functionality.

We can run the Python shell by using the following command in the command-line tool.

python3 manage.py shell

Copy to Clipboard

In order to work with our models in the Python shell we need to import them the same way we would in a Python file:

>>> from app_name.models import ModelName

Copy to Clipboard

With our model imported, we can start creating instances (specific examples) of the model. Let’s say that we’re creating a website like Twitter that has a Post model with the fields title and description. To create an instance of our model we need to call our model and fill out the fields like so:

>>> post_instance=Post(title="New", description="My Post")

Copy to Clipboard

Here, we start with a variable called post_instance that will store our instance. Then we used the Post model and provided the necessary arguments and values for the title and description fields. Note that while variables are not necessary to create instances, it gives us a nice way to refer to our created instances later on.

We’ve created our instance but we still need to save it to our database by calling .save() on the post_instance variable:

>>> post_instance.save()

Copy to Clipboard

With our instance made, we should exit out of the shell. We can exit out of the Python shell by typing out the command exit(). In Windows we can press ctrl + Z. On Mac or Linux ctrl + D.

Reading Instances
10 min
Being able to read instances of a model can give us more information about what’s stored in the 
database
Preview: Docs Loading link description
 and the shape of our data. When we want to view all instances of a model, we can run the .all() method on the model like so:

>>> every_instance = ModelName.objects.all()

Copy to Clipboard

Here we created a variable called every_instance. In the variable, we called a model followed by .objects followed by the .all() query 
method
Preview: Docs Loading link description
. This will return every instance of the model, which should look something like this:

>>> every_instance
<QuerySet [<ModelName: object (1)>, <ModelName: object (2)>]>

Copy to Clipboard

Our code returns us a QuerySet, a collection of objects from our database. In this QuerySet two instances, each instance associated with a number which is the instance’s ID number. We should also know that a QuerySet is indexable, meaning we can grab an instance by their 
index
Preview: Docs Loading link description
.

>>> every_instance[0]
<ModelName: object (1)>

Copy to Clipboard

In the above code snippet, we referenced the variable every_instance and searched for the instance in the index position 0. In the next line, we get returned the first instance in the QuerySet (<ModelName: object (1)>).

There’s also another way that we can return the first instance of a model using a query method using the .first() query method:

>>> first_instance = ModelName.objects.first()
>>> first_instance
<ModelName: object (1)>

Copy to Clipboard

In our code snippet, we created a variable called first_instance where we called ModelName.objects.first(). Then, we referenced the variable first_instance and it returned us the very first instance created for that model.

The .first() and .all() method (or any other method) can be combined with other methods to make more complicated queries but we will get deeper into this as we progress throughout the lesson.

The get() and get_or_create() Method
12 min
Yay, we’ve finished with the basics of CRUD! Now let’s get introduced to some useful methods, starting with .get().

The .get() method returns an object that matches the arguments we give it. This 
method
Preview: Docs Loading link description
 should mainly be used to look up values that are unique to return a single instance. If our query returns multiple objects we will get a .MultipleObjectsReturned exception. And if nothing matches, we’ll get a .DoesNotExist exception. Here’s an example of the syntax:

>>> unique_instance = ModelName.objects.get(name="Ruqisa")
>>> unique_instance
<ModelName: ModelName object (10)>

Copy to Clipboard

In the example above, we called .get() with a name="Ruqisa" 
argument
Preview: Docs Loading link description
 and when we check the returned value, we get an instance. Even though we only used a single argument, we could’ve added as many arguments as there are fields.

Another method that gives even more functionality is the .get_or_create() method.

What .get_or_create() does is look through the 
database
Preview: Docs Loading link description
 for an object with the conditions that we provide. If an object fits our conditions it will return the object, otherwise, it will create the object hence its name .get_or_create().

Let’s look at an example:

>>> wanted_object = ModelName.objects.get_or_create(title="example", content="jango")
>>> wanted_object
(<ModelName: ModelName object (15)>, True)

Copy to Clipboard

The code above looks through our database for an object with the title of "example" and content of "jango". Notice that we get a 
tuple
Preview: Docs Loading link description
 back. The first element of the tuple is the object itself and the second element is a 
boolean
Preview: Docs Loading link description
 (True if the object was just created, or False if the object was not just created). In this case, there was no model that has a title="example" and content="jango". Hence we get back (<ModelName: ModelName object (15)>, True).

Let’s look at some other common querying methods, like .exclude().

The .exclude() method does the exact opposite of the .get() 
method
Preview: Docs Loading link description
. Instead of returning an object with matching arguments, it returns all objects that do not match the arguments.

>>> not_trucks = ModelName.objects.exclude(title="truck")
>>> not_trucks
<QuerySet [<ModelName: object (1)>, <ModelName: object (2)>]>

Copy to Clipboard

Another helpful method is the .order_by() method. It allows us to return a list of objects based on a specified order. We can return based on the date posted, by ID number, etc.

>>> ordered_by_id = modelName.objects.order_by("-pk")
>>> ordered_by_id
<QuerySet [<ModelName: object (2)>, <ModelName: object (1)>]>

Copy to Clipboard

Above, we created an ordered_by_id variable. In the variable we called a model and used the .order_by() method to sort by "pk", or primary key/ID. We returned our instances by ID in descending order by adding the negative "-" sign in front of "pk". Notice that we have object(2) appear before object(1).

We can even return the objects randomly:

>>> random_ordering = ModelName.objects.order_by("?")

Copy to Clipboard

This will return our objects ordered randomly every time.

There are many more useful query methods that we can look up in Django’s documentation.

Querying Two Tables
11 min
Oftentimes, we need to work with different models at the same time since apps generally have more than a single model and their models often relate to each other. To gain more insight into how these models work together and what information they share, we should learn how to query two tables at the same time.

Remember, foreign keys can connect two tables together through a one-to-many relationship. For example, imagine if we have an Answer model and a Question model. A single Question can have many Answer instances. So the Answer model stores a foreign key of the Question model to its own table.

Now let’s say we want to return every Answer to a Question. We can use the .filter() method to look for every Answer instance related to a question instance. The first thing we need to do is capture a Question instance in a variable. For now, let’s say we have a variable called question_instance that holds the question "Is blue a color?". Now in our .filter() 
method
Preview: Docs Loading link description
, we can provide the question_instance variable as an 
argument
Preview: Docs Loading link description
 and get back matching results.

>>> question_instance = Question.objects.get(question="Is blue a color?") 
>>> Answer.objects.filter(question=question_instance)
<QuerySet [<Answer: No>, <Answer: Yes>, <Answer: It is a number>]>

Copy to Clipboard

Above, we used the Answer model and called the .filter() method with the argument question=question_instance. When we run the above query it will return a QuerySet with every Answer instance that’s associated with the Question instance "Is blue a color?". We used a specific instance before to filter, but we can also use fields, like an ID. Django allows us to prepend _id to the name of the foreign key table to filter by ID, like so:

>>> Answer.objects.filter(question_id=3)
<QuerySet [<Answer: It is a number>]>

Copy to Clipboard

The above code will return every Answer instance related to the Question instance whose ID is 3.

Let’s get a little deeper into querying two tables. In our previous exercise, we were able to access every Answer related to a Question because our Answer model held a foreign key to our Question model. What if we wanted to explore the other side of the relationship and use the Question model to query for all related Answer instances? This query is called reverse relation, since that the relationship is now flipped, the table that’s doing the querying doesn’t contain a foreign key.

Suppose we have a variable called question_instance that stores an instance of our Question model. We can get the related Answer instances to that question instance by using _set like so.

>>> question_instance.answer_set.all()

Copy to Clipboard

Above, we access the .answer_set property of the question_instance. By convention, the _set property is preceded by the lowercase name of the model. Notice that we use .all() at the end to access every Answer instance related to question_instance.

Let’s go over a quick summary of what we’ve learned so far.

CRUD is the four basic functions of a 
database
Preview: Docs Loading link description
. CRUD stands for Create, Read, Update and Delete.
A new instance of a model can be created by calling the model then filling out the fields of the model. The instance can be saved to the database by using .save().
We can view all queries of a model by using the .all() 
method
Preview: Docs Loading link description
.
We can update an instance of a model by reassigning a field value and saving the instance.
We can delete an instance by using the .delete() method.
The .get() method returns an object that matches the argument(s)parameters we give it.
The .get_or_create() method looks through the database and looks for any object with the conditions that we provide. If it does find an object with our conditions it will return the object if not it will create the object.
The .exclude() method returns an object that does not match the 
argument
Preview: Docs Loading link description
 we give it.
We can use the .order_by() method to return objects in any order we like.
The .filter() method can be used to query two tables. The .filter() method can take in a foreign key and return an instance associated with that foreign key.
We can query using the reverse relation by appending _set to a model’s name to find related model instances.
Congrats! You’ve made it through and learned so much. Now you can use your knowledge to dig deeper into how to interact with the database!