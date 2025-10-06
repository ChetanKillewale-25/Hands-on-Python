
done = -1

if done:
    print("yes!")
else:
    print('No!')

done1 = ""                  #           LISTS , TUPLES , SETS AND DICTIONARIES ARE FALSE UNTIL THRY ARE EMPTY.

if done1:
    print("Yes!")
else:
    print("No!")

        #       USING ANY AND ALL USING BOOLEAN

book_1_read=True
book_2_read=False

read_any_book = any([book_1_read,book_2_read])      #   ANY RETURNS TRUE IF ANY VALUE IS TRUE.
print(read_any_book)

ingredients_purchased = True
ingredients_cooked = False

ready_to_serve = all([ingredients_purchased,ingredients_cooked])
print(ready_to_serve)