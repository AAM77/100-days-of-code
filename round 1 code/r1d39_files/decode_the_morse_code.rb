# Name: Decode the Morse Code
# Difficulty: 6 kyu
#
# --- sources ---
# Website: CodeWars
# URL: https://www.codewars.com/kata/decode-the-morse-code/train/ruby
#
#
#
##################
#                #
#  Instructions  #
#                #
##################
#
#
# In this kata you have to write a simple Morse code decoder. While the Morse code is now mostly superceded by voice and digital data communication channels, it still has its use in some applications around the world.
# The Morse code encodes every character as a sequence of "dots" and "dashes". For example, the letter A is coded as ·−, letter Q is coded as −−·−, and digit 1 is coded as ·−−−−. The Morse code is case-insensitive, traditionally capital letters are used. When the message is written in Morse code, a single space is used to separate the character codes and 3 spaces are used to separate words. For example, the message HEY JUDE in Morse code is ···· · −·−−   ·−−− ··− −·· ·.
#
# NOTE: Extra spaces before or after the code have no meaning and should be ignored.
#
# In addition to letters, digits and some punctuation, there are some special service codes, the most notorious of those is the international distress signal SOS (that was first issued by Titanic), that is coded as ···−−−···. These special codes are treated as single special characters, and usually are transmitted as separate words.
#
# Your task is to implement a function that would take the morse code as input and return a decoded human-readable string.
#
# For example:
#
# decodeMorse('.... . -.--   .--- ..- -.. .')
# #should return "HEY JUDE"
# NOTE: For coding purposes you have to use ASCII characters . and -, not Unicode characters.
#
# The Morse code table is preloaded for you as a dictionary, feel free to use it:
#
# Coffeescript/C++/Go/JavaScript/PHP/Python/Ruby/TypeScript: MORSE_CODE['.--']
# C#: MorseCode.Get(".--") (returns string)
# Elixir: morse_codes variable
# Elm: MorseCodes.get : Dict String String
# Haskell: morseCodes ! ".--" (Codes are in a Map String String)
# Java: MorseCode.get(".--")
# Kotlin: MorseCode[".--"] ?: "" or MorseCode.getOrDefault(".--", "")
# Rust: self.morse_code
# Scala: morseCodes(".--")
# All the test strings would contain valid Morse code, so you may skip checking for errors and exceptions. In C#, tests will fail if the solution code throws an exception, please keep that in mind. This is mostly because otherwise the engine would simply ignore the tests, resulting in a "valid" solution.
#
# Good luck!
#
# After you complete this kata, you may try yourself at Decode the Morse code, advanced.


##############
# PSEUDOCODE #
##############
#
# set up an array called 'decoded_words' to collect the decoded words

  # group the morseCode into words by splitting morseCode by three spaces
  # and “left strip” to remove whitespace

  # we will call this split array 'morse_words'
  # iterate through morse_words
  # for each morse_word:
    #split by space to get and array of letters
    # iterate through through the letters
    	# change to a letter using the dictionary/library MORSE_CODE[] and map it to an array of words
    	# join the mapped letters and push the resulting word to the decoded_words array

  # join decoded_words by space and return it


#############
# SOLUTIONS #
#############

#BUILT IN LIBRARY:

MORSE_CODE = {
  ".-"=>"A",
  "-..."=>"B",
  "-.-."=>"C",
  "-.."=>"D",
  "."=>"E",
  "..-."=>"F",
  "--."=>"G",
  "...."=>"H",
  ".."=>"I",
  ".---"=>"J",
  "-.-"=>"K",
  ".-.."=>"L",
  "--"=>"M",
  "-."=>"N",
  "---"=>"O",
  ".--."=>"P",
  "--.-"=>"Q",
  ".-."=>"R",
  "..."=>"S",
  "-"=>"T",
  "..-"=>"U",
  "...-"=>"V",
  ".--"=>"W",
  "-..-"=>"X",
  "-.--"=>"Y",
  "--.."=>"Z",
  "-----"=>"0",
  ".----"=>"1",
  "..---"=>"2",
  "...--"=>"3",
  "....-"=>"4",
  "....."=>"5",
  "-...."=>"6",
  "--..."=>"7",
  "---.."=>"8",
  "----."=>"9",
  ".-.-.-"=>".",
  "--..--"=>",",
  "..--.."=>"?",
  ".----."=>"'",
  "-.-.--"=>"!",
  "-..-."=>"/",
  "-.--."=>"(",
  "-.--.-"=>")",
  ".-..."=>"&",
  "---..."=>"=>",
  "-.-.-."=>";",
  "-...-"=>"=",
  ".-.-."=>"+",
  "-....-"=>"-",
  "..--.-"=>"_",
  ".-..-."=>"\"",
  "...-..-"=>"$",
  ".--.-."=>"@",
  "...---..."=>"SOS"
 }

#***********#
# Attempt 1 #
#***********#

def decodeMorse(morseCode)
  decoded_words = []
  morse_words = morseCode.lstrip.split('   ')
  morse_words.each do |morse_word|
    decoded_word = morse_word.split(' ').map { |letter| MORSE_CODE[letter] }.join('')
    decoded_words.push(decoded_word)
  end

  decoded_words.join(' ')
end
