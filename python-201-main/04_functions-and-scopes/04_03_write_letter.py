# Define a function called `write_letter()` that takes as input a `name`
# and a `text` argument. In the body of the function, create a greeting
# message with the `name` input, as well as a goodbye message that uses
# the `name` again. Combine that with the input `text` to return a
# complete `letter`.


def write_letter(name, text):
    greeting = f"Hello {name}, '\n' {text} Stay well and we hope to see you there {name}."
    return greeting 

print(write_letter(
            'Karel', 'We are pleased to announce that you have been nominated for the Pulitzer price."\n"'))

