# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.

opinion = input('What are you really thinking? : ')

opinion_final = ''.join([x.lower() if i%2 else x.upper() for i,x in enumerate(opinion)])

print(opinion_final)