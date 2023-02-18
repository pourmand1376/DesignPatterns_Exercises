This pattern is used to implement **undo** mechanism in oop. 

To see the workflow, run `python main.py`. 

## My Thoughts

What History class does is too simple, we can remove it and just use a list.
I kept it as it is used in the classic UML of design patterns. 

DocumentState is necessary since we should be able to capture the full state of the class. 