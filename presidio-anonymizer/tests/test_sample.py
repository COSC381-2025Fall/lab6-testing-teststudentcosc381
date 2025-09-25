import pytest
from presidio_anonymizer.sample import sample_run_anonymizer

# Part 3: Unit Tests for the Refactored Code
def test_sample_run_anonymizer():
    # replace the following line with your test
    # Grading 1: the input should be exactly: "My name is Bond.", 11, 15
    result = sample_run_anonymizer("My name is Bond.", 11, 15)
    # Grading 2: assert the result.text, which should be "My name is BIP."
    assert result.text == "My name is BIP."
    # Grading 3: assert the length of the result.items should be 1
    assert len(result.items) == 1
    # Grading 4: assert the start should be 11
    assert result.items[0].start == 11
    # Grading 5: assert the end should be 14
    assert result.items[0].end == 14
