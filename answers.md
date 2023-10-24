## CS 520 In-class exercise 2

By Patrick Walsh, Matthew Lips

Due **October 26th, 11:59pm**

---

## Questions

### Question 1
> What are the 2 best practices satisfied by the triangle project that make it easier to write unit tests and run them?

The two best practices satisfied by the triangle project that make it easier to write unit tests is **Composite** and **white box testing**.
- Composite allows develpoers to plug and play with the function, rather than having to build an entire object for the triangle just to get the same outputs for testing
- white box testing allows developers to see inside the code and make testing like decision and statement testing better, but it makes the largest difference with mutation testing. Being able to see the source code like white box testing allows is required for mutation testing, and mutation testing allows for more rigorous tests of the software, ensuring no undefined behaviors sneak through.

### Question 2
> For the isTriangle class with the initial test suite, what is the statement (a.k.a. line) coverage percentage? The decision (a.k.a. branch) coverage percentage? The mutant detection rate?

### Question 3
> Did your approach to writing unit tests differ between developing a coverage-adequate test suite and developing a mutation-adequate test suite? Briefly explain why or why not.

### Question 4
> Consider your mutation-adequate test suite and the triangle program. For any given program, why are some mutants not detectable?

### Question 5
> What changes in the code coverage percentages and mutant detection rate did you observe when deleting (or commenting out) all assertions?

### Question 6
> Create a definition of “test case redundancy” based on code coverage or mutation analysis. Given your definition of test case redundancy, are some of the test cases in your test suites redundant? Given your definition of test case redundancy, would you remove redundant test cases? Briefly explain why or why not.

### Question 7
> How many decision points did you find for the Control flow graph for normative cases (scalene triangle, equilateral triangle, and isosceles triangle) and exception cases (invalid sides and triangle inequality)? Did these findings help you to create a better test suite?