<p align="center">
	<h1 align="center">Routing of telephone excercise</h1>
	<p align="center"> A solution for the coding challenge alaTest/ValueChecker (ICSS) 2024
</p>

## About The Repository

- With the [coding challenge](https://docs.google.com/document/d/1t8BSicFnJellmzg2tBNoAL4hoes3hkyBljowWbBeVrg),
  I've come up with the solution using Trie data structure to solve it.
- This repository contains data from [here](https://gist.github.com/anubhavshrimal/75f6183458db8c453306f93521e93d37).
- The unit test covers 7 test cases which I will explain later on.

## Data Preparation

- With the data from [anubhavshrimal](https://gist.github.com/anubhavshrimal/75f6183458db8c453306f93521e93d37),
  I've saved it into `/data/sample.json`. From that, I used some functions in `/src/utils.py` to create 2 .json files
  name
  ` operator_a.json` and `operator_b.json`.
- You can use the function `create_new_data` to create the data that we will use for Trie from the `sample.json` file.
- To make 2 .json to be different from each other, you can use the function `remove_random_data` to random remove an
  amount of
  elements from the data.

## To Run The Algorithm

- You can simply run the command `python main.py`. It will require you to input a phone number,
and then it will return the cheapest price and its operator. Data will come from both operators that I've created in `/data` folder.

## Why Trie?

- At the beginning, I've just merged data from 2 operators and check if the key from them is matched with the prefix.
Although at the worst case, this solution is just have the complexity equals `O(l)` with `l` is the length of the phone number.
However, the data was saved is having too many duplicated. For example, we have to save these prefix: `12`, `13`, `14` and `15`,
and then it will have `121`, `122`, `123`, ... For the worst case, the data will be so huge.
- I've tried to find a better data structure to store the data, and Trie(also call prefix tree) is the one I think will fit for our problem.
- ![Demo](https://static.javatpoint.com/ds/images/trie-data-structure.png)
- Above image is an example of a Trie, we will do exactly the same with our problem. We can save our prefixes with Trie, 
and also save the price + its operator, so we can return it when searching.
- I've written a function to print out the Trie for better debugging, this is an example of how our Trie will look like.
-         4---None---Empty
            3---0.05---B$
                4---None---Empty
                    5---0.7---A$
            7---0.1---A$
                1---0.2---B$

## Test cases

- To run the tests, simple use command `pytest` in the root folder.
- I've created 7 test cases to cover some cases for the code. The tests will have input of 2 dictionaries for 2 operators,
a phone number, and we will expect it returns the exact price + its operator. 
Moreover, I've covered some case when number not found or invalid number, the `create_trie` function also has been covered.

## What now?

- Feel free to read my solution and comment if you have any question.
- If there's something wrong, it would be a pleasure if you point it out for me. Thank you!


<p align="center">
	<h1 align="center">Thanks for reading this!</h1>
