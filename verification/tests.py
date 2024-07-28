"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        
    {
        "input": [150.0, 10.0],
        "answer": [15.00, "Sem Necessidade de Revisão"]
    },
    {
        "input": [50.0, 5.0],
        "answer": [10.00, "Sem Necessidade de Revisão"]
    },
    {
        "input": [50.0, 10.0],
        "answer": [5.00, "Revisão Recomendada"]
    },
    {
        "input": [200.0, 30.0],
        "answer": [6.67, "Revisão Recomendada"]
    }

    ]
}
