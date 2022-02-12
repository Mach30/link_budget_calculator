Current thoughts for the library:

Constructor may need to take a pint registry so that all units for the entire execution come from the same pint registry.

python property decorators should be used for getting and setting variables, this is the new and fancy pythonic way to control "property" variables. This way is preferred over using functions for each variable or one get/set function for all variables.

Documentation for the code other than the link budget documentation should use python docstrings. This way code users will have direct access to helpful tips as they use the library.

pint dBm units are "hacked" together for now until a clean way to implement them in pint is confirmed.

Flow of the library:
 - User instantiates a new link budget calculator object
 - Set input variables using "setter" functions
 - > If one of the inputs is invalid, throw errors so the user is aware
 - Call a "run" or "calculate" function that does the calculations
 - > If this is successful, an "isValid" function should return true until other changes in the values
 - > If a calculation is erroneous, an error will be thrown and "isValid" will be false
 - User can "get" output or intermediate variables as they please