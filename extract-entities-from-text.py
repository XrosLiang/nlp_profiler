import time

from org.neomatrix369.better_nlp import BetterNLP

english_nlp_model = BetterNLP().load_nlp_model()

print("Started parsing...")
startTime = time.time()
# Can be any factual text or any text to experiment with
generic_text = """Denis Guedj (1940 – April 24, 2010) was a French novelist and 
a professor of the History of Science at Paris VIII University. He was born 
in Setif. He spent many years devising courses and games to teach adults 
and children math. He is the author of Numbers: The Universal Language and 
of the novel The Parrot's Theorem. He died in Paris. 
"""

parsed_generic_text = english_nlp_model(generic_text)

[print(f"{each_entity.text} ({each_entity.label_})") for each_entity in parsed_generic_text.ents if each_entity.text.strip() == each_entity.text]

print("\nToken types legend: ", BetterNLP.token_legend())
endTime = time.time()

print("\n")
print("...Finished parsing\n")
print("Time taken to process the generic text: {} seconds".format(endTime-startTime))