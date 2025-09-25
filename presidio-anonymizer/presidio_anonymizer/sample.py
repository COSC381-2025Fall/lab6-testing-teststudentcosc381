from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig

# Part 2: Refactor for Testability
def sample_run_anonymizer(text:str, start: int, end: int): 
    # Grading 1: have three parameters, and the parameters should include:
    # 1) text with a str type,
    # 2) start with an int type,
    # 3) end with an int type

    # Initialize the engine
    engine = AnonymizerEngine()

    # Invoke the anonymize function with the text, 
    # analyzer results (potentially coming from presidio-analyzer) and
    # Operators to get the anonymization output:
    result = engine.anonymize(
        text=text, # Grading 2: change the input method to the parameter
        analyzer_results=[RecognizerResult(entity_type="PERSON", start=start, end=end, score=0.8)], # Grading 3: change the input methods to the parameters
        operators={"PERSON": OperatorConfig("replace", {"new_value": "BIP"})}
    )

    print(result)
    return result # Grading 3: have a return

    # input should be:
    # text: My name is Bond.
    # start: 11
    # end: 15
    # 
    # output should be:
    # text: My name is BIP.
    # items:
    # [
    #     {'start': 11, 'end': 14, 'entity_type': 'PERSON', 'text': 'BIP', 'operator': 'replace'}
    # ]

if __name__ == "__main__": 
    result = sample_run_anonymizer("My name is Bond.", 11, 15); # Grading 4: should modify the main method to get the result

# Grading 5: The whole program should be syntactically correct