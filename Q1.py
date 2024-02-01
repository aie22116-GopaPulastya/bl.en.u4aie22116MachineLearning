def count_vowels_and_consonants_in_word(word):
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in word if char in vowels)
    consonant_count = sum(1 for char in word if char.isalpha() and char not in vowels)
    vowels_in_word = [char for char in word if char in vowels]
    consonants_in_word = [char for char in word if char.isalpha() and char not in vowels]
    return vowel_count, consonant_count, vowels_in_word, consonants_in_word
# Get user input
user_word = input("Enter a word: ")
# Call the function to count and get vowels and consonants
vowel_count, consonant_count, vowels, consonants = count_vowels_and_consonants_in_word(user_word)
# Output the results
result_output = {
    "Word": user_word,
    "Vowel Count": vowel_count,
    "Consonant Count": consonant_count,
    "Vowels": vowels,
    "Consonants": consonants
}
print(result_output)

